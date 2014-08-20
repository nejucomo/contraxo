import sys

from contraxo import clargs
from contraxo import simulator


def main(args = sys.argv[1:]):
    clargs.parse_args(args)
    simulator.Simulator()
