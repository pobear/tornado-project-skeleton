# -*- coding: utf-8 -*-
from tornado import gen

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    # @tornado.web.authenticated
    @gen.coroutine
    def get(self):
        db = self.settings['db']
        message = yield db.patchmind_messages.find_one({'name': 'pobear'})
        print message
        self.render('index.html')
