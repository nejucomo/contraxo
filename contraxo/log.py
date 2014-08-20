import logging


class LogMixin (object):
    def __init__(self):
        self._log = logging.getLogger(type(self).__name__)
