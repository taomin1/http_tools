# -*- coding: utf-8 -*-
#！/usr/bin/env python
import unittest
from center.baidu_interface import baidu_interface

class Test_Baidu(unittest.TestCase):
    def setUp(self):
        self.url = "https://www.baidu.com"
        self.baidu = baidu_interface()

    def test_baidu(self):
        response = self.baidu.get_baidu_index()
        self.assertEqual(response.status_code, 200)