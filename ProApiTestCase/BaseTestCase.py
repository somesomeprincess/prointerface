#coding:utf-8
import unittest

from ProUtils import HeartBeat


class BaseTestCase(unittest.TestCase):
    while True:
        if (HeartBeat.HeartBeat().IsConnect()):
            break
    def tearDown(self):
        pass
