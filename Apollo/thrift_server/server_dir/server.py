# -*- coding:utf-8 -*-
# User     shihao
# Ctime    2021/6/9

from __future__ import unicode_literals

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

import logging
import select
import threading
from six.moves import queue
import errno
# from django.db import close_old_connections

from ncBackupSvc import ncBackupSvc
from server_dir.processor import BackupSvcProcessor

EPMS_THRIFT_SSL_ON = False


class TServer(object):
    """Base interface for a server, which must have a serve() method.

    Three constructors for all servers:
    1) (processor, serverTransport)
    2) (processor, serverTransport, transportFactory, protocolFactory)
    3) (processor, serverTransport,
        inputTransportFactory, outputTransportFactory,
        inputProtocolFactory, outputProtocolFactory)
    """
    def __init__(self, *args):
        if len(args) == 2:
            self.__initArgs__(args[0], args[1],
                              TTransport.TTransportFactoryBase(),
                              TTransport.TTransportFactoryBase(),
                              TBinaryProtocol.TBinaryProtocolFactory(),
                              TBinaryProtocol.TBinaryProtocolFactory())
        elif len(args) == 4:
            self.__initArgs__(args[0], args[1], args[2], args[2], args[3], args[3])
        elif len(args) == 6:
            self.__initArgs__(args[0], args[1], args[2], args[3], args[4], args[5])

    def __initArgs__(self, processor, serverTransport,
                     inputTransportFactory, outputTransportFactory,
                     inputProtocolFactory, outputProtocolFactory):
        self.processor = processor
        self.serverTransport = serverTransport
        self.inputTransportFactory = inputTransportFactory
        self.outputTransportFactory = outputTransportFactory
        self.inputProtocolFactory = inputProtocolFactory
        self.outputProtocolFactory = outputProtocolFactory

    def serve(self):
        pass


class TThreadPoolServer(TServer):
    """Server with a fixed size pool of threads which service requests."""

    def __init__(self, *args, **kwargs):
        TServer.__init__(self, *args)
        self.clients = queue.Queue()
        self.threads = 10
        self.daemon = kwargs.get("daemon", False)
        self.logger = logging.getLogger('Run')
        self.enable_ssl = False

    def setEnableSSL(self, enable_ssl):
        self.enable_ssl = enable_ssl

    def setNumThreads(self, num):
        """Set the number of worker threads that should be created"""
        self.threads = num

    def serveThread(self):
        """Loop around getting clients from the shared queue and process them."""
        while True:
            try:
                client = self.clients.get()
                self.serveClient(client)
            except Exception as x:
                self.logger.exception('thrift error: {0}'.format(x))

    def serveClient(self, client):
        """Process input/output from a client for as long as possible"""
        if self.enable_ssl:
            try:
                client.handle.do_handshake()
                client.handle.getpeercert(False)
            except Exception as e:
                self.logger.exception('do_handshake err: %r' % e)
                client.handle.close()
                raise e
        itrans = self.inputTransportFactory.getTransport(client)
        otrans = self.outputTransportFactory.getTransport(client)
        iprot = self.inputProtocolFactory.getProtocol(itrans)
        oprot = self.outputProtocolFactory.getProtocol(otrans)
        try:
            while True:
                # close_old_connections()
                self.processor.process(iprot, oprot)
                # close_old_connections()
        except TTransport.TTransportException:
            pass
        except Exception as x:
            self.logger.exception('thrift error: {0}'.format(x))

        itrans.close()
        otrans.close()

    def _select(self):
        """Does select on open connections."""
        readable = []
        for sock in self.serverTransport:
            readable.append(sock.handle.fileno())
        writable = []
        print("33339999")
        try:
            res = select.select(readable, writable, readable)
        except Exception as e:
            res = None
            print("333399991%s" % [res, e])
        else:
            print("333399992%s" % [res])
        return res

    def serve(self):
        """Start a fixed number of worker threads and put client into a queue"""
        for i in range(self.threads):
            try:
                t = threading.Thread(target=self.serveThread)
                t.setDaemon(self.daemon)
                t.start()
                print("33337777")
            except Exception as x:
                self.logger.exception('thrift error: {0}'.format(x))

        # Pump the socket for clients
        serverTransports = dict()
        for serverTransport in self.serverTransport:
            serverTransport.listen()
            serverTransports[serverTransport.handle.fileno()] = serverTransport
        while True:
            try:
                print("33338888")
                rset, wset, xset = self._select()
            except select.error as e:
                self.logger.warn("err: %s" % e)
                code, msg = e.args
                if code == errno.EINTR:
                    continue
                raise

            for fd in rset:
                try:
                    client = serverTransports[fd].accept()
                    if not client:
                        continue
                    self.clients.put(client)
                except Exception as x:
                    self.logger.exception('thrift error: {0}'.format(x))


class ThriftServer(object):
    def __init__(self,
                 svc_processer=None,
                 thrift_class=ncBackupSvc,
                 port=8888):

        self._port = port
        self._handler = svc_processer() if svc_processer else None
        self._thrift_class = thrift_class

        self.logger = logging.getLogger('Run')

    def _start(self, threads):
        # ips = [SELF_IP, VIRTUAL_IP]
        # if is_ipv6(SELF_IP_EX):
        #     ips.append(SELF_IP_EX)
        # if is_ipv6(VIRTUAL_IP_EX):
        #     ips.append(VIRTUAL_IP_EX)
        #
        # loipv4 = '127.0.0.1'
        # loipv6 = "::1"
        # if is_ipv4(SELF_IP) and loipv4 not in ips:
        #     ips.append(loipv4)
        # if is_ipv6(SELF_IP_EX) and loipv6 not in ips:
        #     ips.append(loipv6)
        ips = ['192.168.1.3', '127.0.0.1']

        self.logger.info("thrift server ip list: %s" % ips)
        lsockets = []
        ipsets = set(ips)
        for ip in ipsets:
            if ip is not None:
                self.logger.info('ThriftServer run [%s:%d] [ssl:%s]' % (ip, self._port, EPMS_THRIFT_SSL_ON))
                if not EPMS_THRIFT_SSL_ON:
                    print("33332222")
                    transport = TSocket.TServerSocket(host=ip, port=self._port)
                else:
                    # from Common.thrift.thrift_ssl import thrift_wrap_ssl
                    # transport = thrift_wrap_ssl(host=ip, port=self._port, server_side=True)
                    transport = TSocket.TServerSocket(host=ip, port=self._port)
                lsockets.append(transport)

        import select
        import errno
        processor = self._thrift_class.Processor(self._handler)
        tfactory = TTransport.TFramedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        server = TThreadPoolServer(processor, lsockets, tfactory, pfactory)
        server.setEnableSSL(enable_ssl=EPMS_THRIFT_SSL_ON)
        server.setNumThreads(threads)
        print("33333333")

        while True:
            try:
                server.serve()
                print("33334444")
            except select.error as e:
                print("33335555")
                self.logger.error("err: %s" % e)
                code, msg = e.args
                if code == errno.EINTR:
                    continue
                raise
            except Exception as e:
                print("33336666")
                raise e

        self.logger.info('End the thrift server at %s:%s' % (ips, self._port))

    def start(self, threads):
        try:
            if self._handler is None:
                print("1111")
                self.logger.error("start thrift server...")
                print("2222")
                import importlib
                self._handler = BackupSvcProcessor()
                print("3333")
                self.logger.error("start thrift server threads")
                print("33331111")
                self._start(threads)
                print("4444")
                self.logger.error("start thrift server ok")
            else:
                self._start(threads)
        except Exception as e:
            self.logger.error('thrift server start error: %s' % e)


def start_thrift_server():
    ThriftServer().start(1)


if __name__ == '__main__':
    start_thrift_server()
