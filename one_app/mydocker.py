__author__ = 'Administrator'
#coding=utf-8
from docker import Client

cli =Client(base_url="tcp://s2.95xd.com:2375")
print cli.images()
print(cli.containers())