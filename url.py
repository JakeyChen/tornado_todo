# coding:utf-8

import tornado.web
import application

url = [(r"^/(favicon\.ico)", tornado.web.StaticFileHandler,
        dict(path=application.settings['static_path']))]

url += [(r"^/", "handlers.index.IndexHandler")]
