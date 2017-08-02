#! /usr/bin/env python

import logging

class Logger():

    def __init__(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        handler = logging.FileHandler('.moss/module_run.log')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s \033[1;32m%(name)s\033[0m \033[1;34m[%(levelname)s]\033[0m %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        self.logger = logger


    def log(self, message):
        self.logger.info(message)
