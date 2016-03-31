#-*- coding:utf-8 -*-

from base import BaseHandler


class NewHandler(BaseHandler):
    '''
    New Handler
    '''

    def post(self):
        todo_text = self.get_argument("todo_text")
        if not todo_text:
            return None
        self.db.execute('''insert into todo 
                            (
                                todo_text
                            ) 
                            values
                            (
                                %s
                            )''', todo_text)
        self.redirect("/")
