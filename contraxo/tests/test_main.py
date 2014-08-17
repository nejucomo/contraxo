import sys
import logging

from mock import call, patch

from contraxo import main
from contraxo.tests.utils import MockTestCaseBase, ArgStartsWith


class parse_args_Tests (MockTestCaseBase):

    @patch('logging.basicConfig')
    @patch('twisted.python.log.PythonLoggingObserver')
    @patch('sys.stderr')
    @patch('sys.stdout')
    def test_help(self, m_stdout, m_stderr, m_PythonLoggingObserver, m_basicConfig):

        self.assertRaises(SystemExit, main.parse_args, ['--help'])

        self.checkCalls(m_stdout, call.write(ArgStartsWith('usage: ')))
        self.checkCalls(m_stderr)
        self.checkCalls(m_basicConfig)
        self.checkCalls(m_PythonLoggingObserver)

    @patch('logging.basicConfig')
    @patch('twisted.python.log.PythonLoggingObserver')
    @patch('sys.stderr')
    @patch('sys.stdout')
    def test_no_args(self, m_stdout, m_stderr, m_PythonLoggingObserver, m_basicConfig):

        opts = main.parse_args([])

        self.assertEqual(opts.SOURCE_ROOT, '.')

        self.checkCalls(m_stdout)
        self.checkCalls(m_stderr)

        self.checkCalls(
            m_basicConfig,
            call(stream=sys.stdout,
                 format=main.LogFormat,
                 datefmt=main.LogDateFormat,
                 level=logging.INFO))

        self.checkCalls(
            m_PythonLoggingObserver,
            call(),
            call().start())
