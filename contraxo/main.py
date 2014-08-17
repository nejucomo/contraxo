import sys
import argparse
import logging
from twisted.python import log as txlog


DESCRIPTION = """
contraxo - Build Ethereum contracts and execute deterministic regression tests.
"""


def main(args = sys.argv[1:]):
    opts = parse_args(args)
    raise NotImplementedError('main with opts {0!r}'.format(opts))


def parse_args(args):
    p = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter)

    p.add_argument(
        '--log-level',
        dest='loglevel',
        default='DEBUG',
        choices=['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'],
        help='Set logging level.')

    p.add_argument(
        'SOURCE_ROOT',
        default='.',
        help='Source root directory.')

    opts = p.parse_args(args)

    logging.basicConfig(
        stream=sys.stdout,
        format='%(asctime)s %(levelname) 5s %(name)s | %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S%z',
        level=getattr(logging, opts.loglevel))

    txlog.PythonLoggingObserver().start()

    return opts


