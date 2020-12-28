import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo',
                    default='badger')
parser.get_default('foo')
args = parser.parse_args()
parser.print_help()
