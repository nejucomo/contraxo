from textwrap import dedent
from StringIO import StringIO

from mock import call, patch

from contraxo import script
from contraxo.tests.utils import MockTestCaseBase


class ScriptTests (MockTestCaseBase):

    @patch('logging.getLogger')
    def test_load_valid(self, m_getLogger):
        self._load(
            """\
               {}
            """)

        self.checkCalls(m_getLogger, call('Script'))

    def test_load_invalid(self):
        self.assertRaises(ValueError, self._load, '\0 This is invalid JSON \0')

    def _load(self, s):
        return script.Script.load(StringIO(dedent(s)))
