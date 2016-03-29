#-*- coding:utf-8 -*-

from base import BaseHandler


class IndexHandler(BaseHandler):
    '''
    Index Handler
    '''

    def get(self):
        self.write("Index")
