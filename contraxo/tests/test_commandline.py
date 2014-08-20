from mock import call, patch

from contraxo import commandline
from contraxo.tests.utils import MockTestCaseBase


class parse_args_Tests (MockTestCaseBase):

    @patch('contraxo.clargs.parse_args')
    @patch('contraxo.simulator.Simulator')
    def test_help(self, m_Simulator, m_parse_args):

        commandline.main([])

        self.checkCalls(m_parse_args, call([]))
        self.checkCalls(m_Simulator, call())
