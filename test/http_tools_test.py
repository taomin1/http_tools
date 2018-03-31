# -*- coding: utf-8 -*-
#！/usr/bin/env python

from core.http_tools import http_tools

class test_http_tools(http_tools):
    def getbaidu(self):
        self.url="http://www.baidu.com"
        r = self.get().text


    def test_post(self):
        self.url = "http://httpbin.org/post"
        self.data = {
            'key1' : 'value1',
        }
        r = self.post()


if __name__=="__main__":
    test_http_tools().test_post()