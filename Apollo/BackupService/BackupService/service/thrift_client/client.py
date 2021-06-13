# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket
from thrift.transport import TTransport

from ncException.ttypes import ncException


class ThriftClient(object):
    def __init__(self, ip, port, transport=TTransport.TFramedTransport, timeout_ms=30 * 1000):
        self._ip = ip
        self._port = port
        self._transport = transport
        self._timeout_ms = timeout_ms

    def _request(self, service, func, *args, **kwargs):
        """请求

        每次在这里构造Socket, 发起请求
        构造函数只是简单的参数初始化

        :param service: XXService.Client   这是模块(file)
        :type func: str | unicode
        :param func: 附属在Client下的方法
        :param args:
        :param kwargs:
        :return:
        """
        transport = TSocket.TSocket(self._ip, self._port)
        transport.setTimeout(self._timeout_ms)
        transport = self._transport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = service.Client(protocol)
        try:
            transport.open()
            result = getattr(client, func)(*args, **kwargs)
            return result
        except ncException as e:
            raise e
        except Exception as e:
            raise e
        finally:
            transport.close()

    def request(self, service, func, *args, **kwargs):
        count = 0
        limits = 1
        while 3:
            try:
                count += 1
                return self._request(service, func, *args, **kwargs)
            except ncException as e:
                raise e
            except Exception as e:
                # print 'thrift client err: ', e
                if count < limits:
                    continue
                else:
                    raise e

    def set_ip(self, value):
        self._ip = value

        return self

    def set_port(self, value):
        self._port = value

        return self

    def set_timeout(self, value):
        self._timeout_ms = value

        return self

    def __repr__(self):
        return 'ThriftClient(%s, %s, %s)' % (self._ip, self._port, self._timeout_ms)
