import json

from contraxo.log import LogMixin


class Script (LogMixin):

    @classmethod
    def load(cls, stream):
        json.load(stream)
        return cls()
