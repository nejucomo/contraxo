import logging


class Simulator (object):
    def __init__(self):
        self._log = logging.getLogger(type(self).__name__)
