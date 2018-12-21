#coding=utf-8
"""
@athor:weifeng.guo 
@data:2018/11/8 17:10
@filename:readmin
"""
from redminelib import Redmine

class RedmineApi(object):

    def __init__(self):
        self.url = "http://issues.cnexlabs.com/"
        self.key = "e6fcfb5985f7efe4d31000bf52b1db013ff4576c"
        self.login()

    def login(self):
        self.redmine = Redmine(self.url, key= self.key)
        print("****")
        # print(self.redmine.all())

if __name__ == "__main__":
    a = RedmineApi()