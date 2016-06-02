# -*- coding: utf-8 -*-
import motor

import os.path

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)
define("address", default="0.0.0.0", help="run on the given port", type=str)
define("debug", default=False, help="debug mode")
define("config", default=None, help="tornado config file")

options.parse_command_line()

db = motor.motor_tornado.MotorClient().test
settings = {
    "debug": options.debug,
    "cookie_secret": "askdfjpo83q47r9haskldfjh8",
    "login_url": "/login",
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "xsrf_cookies": False,
    "db": db,
}

