#-*- coding:utf-8 -*-

from base import BaseHandler


class EditHandler(BaseHandler):
    '''
    Edit Handler
    '''

    def get(self, id):
        todos = self.db.query("select * from todo where id=%s", int(id))
        todo = todos[0]
        if not todo:
            return None
        return self.render("edit.html", todo=todo)

    def post(self, id):
        todos = self.db.query("select * from todo where id=%s", int(id))
        todo = todos[0]
        if not todo:
            return None
        title = self.get_argument("title")
        self.db.execute('''update todo set 
                            todo_text=%s, 
                            post_date=now() 
                        where 
                            id=%s''', 
                        title, 
                        int(id))
        self.redirect("/")
