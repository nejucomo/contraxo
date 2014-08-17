from mock import call, patch

from contraxo.main import main
from contraxo.tests.utils import MockTestCaseBase, ArgStartsWith


class main_Tests (MockTestCaseBase):

    @patch('logging.basicConfig')
    @patch('twisted.python.log.PythonLoggingObserver')
    @patch('sys.stderr')
    @patch('sys.stdout')
    def test_help(self, m_stdout, m_stderr, m_PythonLoggingObserver, m_basicConfig):

        self.assertRaises(SystemExit, main, ['--help'])

        self.checkCalls(m_stdout, call.write(ArgStartsWith('usage: ')))
        self.checkCalls(m_stderr)
        self.checkCalls(m_basicConfig)
        self.checkCalls(m_PythonLoggingObserver)

        #self.checkCall(
        #    m_PythonLoggingObserver,
        #    [call(),
        #     call().start()])
