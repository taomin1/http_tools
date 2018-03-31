# -*- coding: utf-8 -*-
#！/usr/bin/env python

import requests
import json

class http_tools:

    def __init__(self):
        self.url = ""
        self.cookies = {}
        self.param = {}
        self.data = {}
        self.headers = {}

    def get(self):
        print('CONSOLE:  ' + self.url)
        print('METHOD:GET')
        print('PARAM:'+json.dumps(self.param))
        res = requests.get(self.url)
        print("Response:\n"+res.text)
        return res

    def post(self):
        print('CONSOLE:  ' + self.url)
        print('METHOD:POST')
        print('PARAM:' + json.dumps(self.param))
        print('Data:'+json.dumps(self.data))
        self.headers = {"Content-Type":"applicationjson"}
        res = requests.post(url=self.url,data=self.data,headers=self.headers)
        print("Response:\n"+res.text)
        return res