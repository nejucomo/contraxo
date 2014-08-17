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


    def test_implicit_source_root(self):
        opts = self._test_no_options([])
        self.assertEqual(opts.SOURCE_ROOT, '.')


    def test_explicit_source_root(self):
        relpath = './path/to/test/cases'
        opts = self._test_no_options([relpath])
        self.assertEqual(opts.SOURCE_ROOT, relpath)


    @patch('logging.basicConfig')
    @patch('twisted.python.log.PythonLoggingObserver')
    @patch('sys.stderr')
    @patch('sys.stdout')
    def _test_no_options(self, args, m_stdout, m_stderr, m_PythonLoggingObserver, m_basicConfig):

        opts = main.parse_args(args)

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

        return opts

