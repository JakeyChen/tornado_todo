#-*- coding:utf-8 -*-

from base import BaseHandler


class DeleteHandler(BaseHandler):
    def get(self, id):
        todo = self.db.query("select * from todo where id=%s", int(id))
        if not todo:
            return None
        self.db.execute("delete from todo where id=%s", int(id))
        self.redirect("/")
