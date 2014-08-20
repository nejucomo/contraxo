import sys

from contraxo import argparse


def main(args = sys.argv[1:]):
    opts = argparse.parse_args(args)
    raise NotImplementedError('main with opts {0!r}'.format(opts))
