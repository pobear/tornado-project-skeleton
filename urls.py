# -*- coding: utf-8 -*-
from app.handlers.event import EventHandler

from handlers import base


url_patterns = [
    (r"/", base.MainHandler),
    (r"/events/([a-z_]+)/", EventHandler),
]