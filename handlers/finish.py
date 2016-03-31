#-*- coding:utf-8 -*-

from base import BaseHandler


class FinishHandler(BaseHandler):
    '''
    Finish Handler
    '''
    
    def get(self, id):
        todo = self.db.query("select * from todo where id=%s", int(id))
        if not todo:
            return None
        status = self.get_argument("status", "yes")
        if status == "yes":
            finished = 1
        elif status == "no":
            finished = 0
        else:
            return None
        self.db.execute("update todo set finished=%s where id=%s", finished, id)
        self.redirect("/")
