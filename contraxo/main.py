import sys
import argparse
import logging
from twisted.python import log as txlog


Description = """
contraxo - Build Ethereum contracts and execute deterministic regression tests.
"""

LogFormat = '%(asctime)s %(levelname) 5s %(name)s | %(message)s'
LogDateFormat = '%Y-%m-%dT%H:%M:%S%z'


def main(args = sys.argv[1:]):
    opts = parse_args(args)
    raise NotImplementedError('main with opts {0!r}'.format(opts))


def parse_args(args):
    p = argparse.ArgumentParser(
        description=Description,
        formatter_class=argparse.RawTextHelpFormatter)

    p.add_argument(
        '--log-level',
        dest='loglevel',
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'],
        help='Set logging level.')

    p.add_argument(
        'SOURCE_ROOT',
        default='.',
        nargs='?',
        help='Source root directory.')

    opts = p.parse_args(args)

    logging.basicConfig(
        stream=sys.stdout,
        format=LogFormat,
        datefmt=LogDateFormat,
        level=getattr(logging, opts.loglevel))

    txlog.PythonLoggingObserver().start()

    return opts


