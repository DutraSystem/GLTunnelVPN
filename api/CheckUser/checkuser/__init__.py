import argparse
import logging

logger = logging.getLogger(__name__)

__version__ = '2.2.13'
__author__ = 'DutraSystem'
__email__ = 'contato.dutrasystem@gmail.com'

args = argparse.ArgumentParser(description='Checker for OpenVPN and SSH')
args.add_argument(
    '-v',
    '--version',
    action='version',
    version='%(prog)s ' + __version__,
)
