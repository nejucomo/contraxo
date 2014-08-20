import sys
import logging

from mock import call, patch

from contraxo import clargs
from contraxo.tests.utils import MockTestCaseBase, ArgStartsWith


class parse_args_Tests (MockTestCaseBase):

    @patch('logging.basicConfig')
    @patch('twisted.python.log.PythonLoggingObserver')
    @patch('sys.stderr')
    @patch('sys.stdout')
    def test_help(self, m_stdout, m_stderr, m_PythonLoggingObserver, m_basicConfig):

        self.assertRaises(SystemExit, clargs.parse_args, ['--help'])

        self.checkCalls(m_stdout, call.write(ArgStartsWith('usage: ')))
        self.checkCalls(m_stderr)
        self.checkCalls(m_basicConfig)
        self.checkCalls(m_PythonLoggingObserver)


    def test_implicit_source_stdin(self):
        self._test_no_options([])


    def test_explicit_source_stdin(self):
        self._test_no_options(['-'])


    def test_explicit_source_path(self):
        self._test_no_options(['./testcase.json'])


    @patch('argparse.FileType')
    @patch('logging.basicConfig')
    @patch('twisted.python.log.PythonLoggingObserver')
    @patch('sys.stderr')
    @patch('sys.stdout')
    def _test_no_options(self, args, m_stdout, m_stderr, m_PythonLoggingObserver, m_basicConfig, m_FileType):

        opts = clargs.parse_args(args)

        self.checkCalls(m_stdout)
        self.checkCalls(m_stderr)

        self.checkCalls(
            m_basicConfig,
            call(stream=sys.stdout,
                 format=clargs.LogFormat,
                 datefmt=clargs.LogDateFormat,
                 level=logging.INFO))

        self.checkCalls(
            m_PythonLoggingObserver,
            call(),
            call().start())

        if len(args) == 0:
            args = ['-']

        self.assertEqual(len(args), 1)

        [path] = args

        self.assertIs(opts.SOURCE, m_FileType.return_value.return_value)

