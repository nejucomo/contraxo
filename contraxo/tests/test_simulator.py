from mock import call, patch

from contraxo import simulator
from contraxo.tests.utils import MockTestCaseBase


class SimulatorTests (MockTestCaseBase):

    @patch('logging.getLogger')
    def test___init__(self, m_getLogger):

        simulator.Simulator()

        self.checkCalls(m_getLogger, call('Simulator'))
