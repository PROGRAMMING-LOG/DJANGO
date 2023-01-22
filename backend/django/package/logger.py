#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.handlers

class Logger:
    def __init__(self, name=__name__):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            "[%(asctime)s] [%(process)d] [%(name)s] [%(levelname)s] %(message)s"
        )

        # stdout
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # fileout
        # handler = logging.handlers.RotatingFileHandler(
        #     filename='logger.log',
        #     maxBytes=1048576,
        #     backupCount=3
        # )
        # handler.setLevel(logging.DEBUG)
        # handler.setFormatter(formatter)
        # self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
