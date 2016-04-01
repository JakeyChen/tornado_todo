# coding:utf-8

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    '''
    All Handler's Base
    '''
    
    @property
    def db(self):
        return self.application.db

    def req(self, status, info):
        self.write({
            "status": status,
            "info": info
        })
