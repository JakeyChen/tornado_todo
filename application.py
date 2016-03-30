# coding:utf-8

import os
import uuid
import base64

import tornado.web

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    xsrf_cookies=False,
    cookie_secret=base64.b64encode(uuid.uuid4().bytes+uuid.uuid4().bytes),
    login_url="/login",
    debug=True,
)
