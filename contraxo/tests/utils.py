from twisted.trial.unittest import TestCase

class MockTestCaseBase (TestCase):

    def checkCalls(self, obj, *calls):
        self.assertEqual(obj.mock_calls, list(calls))


class ArgCb (object):
    def __init__(self, cb, desc=None):
        self._cb = cb
        if desc is None:
            desc = repr(cb)
        self._desc = desc

    def __repr__(self):
        return self._desc

    def __eq__(self, other):
        return self._cb(other)


def ArgStartsWith(prefix):
    return ArgCb(lambda s: s.startswith(prefix), '{0!r}...'.format(prefix))
