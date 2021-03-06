#-*- coding:utf-8 -*-

from base import BaseHandler


class IndexHandler(BaseHandler):
    '''
    Index Handler
    '''

    def get(self):
        todos = self.db.query('''select 
                                    * 
                                from 
                                    todo
                                order by 
                                    finished''')
        self.render("index.html", todos=todos)
