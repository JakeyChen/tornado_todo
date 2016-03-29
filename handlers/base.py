# coding:utf-8

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    '''
    All Handler's Base
    '''
    @property
    def db(self):
        '''
        dal
        '''
        return self.application.db
