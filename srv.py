#!/usr/bin/env python
# coding:utf-8

import os
import logging.config

import yaml
import torndb
import tornado.ioloop
import tornado.options
import tornado.httpserver
import tornado.web
from tornado.options import define, options

from url import url
from application import settings


if not os.path.exists("logs"):
    os.makedirs("logs")
with open('conf/logging.yaml', 'r') as f1:
    logging.config.dictConfig(yaml.load(f1))
with open('conf/config.yaml', 'r') as f2:
    g_conf = yaml.load(f2)

define("port", default=g_conf["utils"]["port"], help="port", type=int)
define("mysql_host", default=g_conf["mysql"]["host"], help="database host")
define("mysql_user", default=g_conf["mysql"]["user"], help="database user")
define("mysql_password", default=g_conf["mysql"]["password"], help="database passwd")
define("mysql_database", default=g_conf["mysql"]["database"], help="database name")


class Application(tornado.web.Application):

    def __init__(self):
        tornado.web.Application.__init__(self, url, **settings)

        self.db = torndb.Connection(
            host=options.mysql_host,
            database=options.mysql_database,
            user=options.mysql_user,
            password=options.mysql_password)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
