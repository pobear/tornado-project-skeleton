# -*- coding: utf-8 -*-
import tornado.web

__author__ = 'pobear'


class BaseHandler(tornado.web.RequestHandler):
    db = None

    def initialize(self):
        self.db = self.settings["db"]
