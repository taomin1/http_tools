# -*- coding: utf-8 -*-
#！/usr/bin/env python

"""
__author__ = "taomin"
__version__ = "0.0.1"
"""

"""
Change History

Version 0.0.1
"""

from core.http_tools import http_tools

class baidu_interface(http_tools):
    def get_baidu_index(self):
        self.url="http://www.baidu.com"
        response = self.get()
        return response