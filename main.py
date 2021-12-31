import argparse
import logging

from helper import NUMBER_OF_BATTLES_PER_ROUND, NUMBER_OF_ROUNDS, TYPES_FILE_NAME
from sim import sim

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Determine which pokemon types are the strongest')
    parser.add_argument('-log', '--loglevel', type=str, default='warning',
                        help='Logging level, options: debug, info, warning, error, critical')

    args = parser.parse_args()
    logging.basicConfig(level=args.loglevel.upper())

    sim(NUMBER_OF_BATTLES_PER_ROUND, NUMBER_OF_ROUNDS, TYPES_FILE_NAME, True, True)