#!/usr/bin/env python
# coding=utf-8
"""

@athor:weifeng.guo 
@data:2019/6/21 17:15
@filename:Twisted_server

"""
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory


class SimpleLogger(Protocol):

    def connectionMade(self):
        print('Gor connection from', self.transport.client)

    def connectionLost(self, reason):
        print(self.transport.client, 'disconnected')

    def dataReceived(self, data):
        print(data)


factory = Factory()
factory.protocol = SimpleLogger
reactor.listenTCP(1234,factory)
reactor.run()