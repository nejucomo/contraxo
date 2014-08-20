from mock import call, patch

from contraxo import commandline
from contraxo.tests.utils import MockTestCaseBase


class main_Tests (MockTestCaseBase):

    @patch('contraxo.clargs.parse_args')
    @patch('contraxo.script.Script')
    @patch('contraxo.simulator.Simulator')
    def test_no_args(self, m_Simulator, m_Script, m_parse_args):

        commandline.main([])

        self.checkCalls(
            m_parse_args,
            call([]))

        self.checkCalls(
            m_Simulator,
            call())

        self.checkCalls(
            m_Script,
            call.load(m_parse_args().SOURCE),
            call.load().execute(m_Simulator()))
