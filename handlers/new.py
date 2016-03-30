#-*- coding:utf-8 -*-

from base import BaseHandler


class NewHandler(BaseHandler):
    '''
    New Handler
    '''

    def post(self):
        title = self.get_argument("title")
        if not title:
            return None
        self.db.execute('''insert into todo 
                            (
                                todo_text
                            ) 
                            values
                            (
                                %s
                            )''', title)
        self.redirect("/")
