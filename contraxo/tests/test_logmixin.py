from mock import call, patch

from contraxo import log
from contraxo.tests.utils import MockTestCaseBase


class LogMixinTests (MockTestCaseBase):

    @patch('logging.getLogger')
    def test___init__(self, m_getLogger):

        log.LogMixin()

        self.checkCalls(m_getLogger, call('LogMixin'))
