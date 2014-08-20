import sys

from contraxo import clargs
from contraxo import simulator
from contraxo import script


def main(args = sys.argv[1:]):
    opts = clargs.parse_args(args)
    sim = simulator.Simulator()
    scr = script.Script.load(opts.SOURCE)
    scr.execute(sim)
