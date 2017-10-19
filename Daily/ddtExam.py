import unittest
from ddt import ddt,data,file_data,unpack

@ddt
class FooTestCase(unittest.TestCase):
    def test_undecorated(self):
        self.assertTrue(1<2)
    @data(1,2)
    def test_lalala(self,da):
        self.assertTrue(da<3)

    @data([1,2],[4,3])
    @unpack
    def test_bba(self,one,two):
        self.assertTrue(one>two)
