import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--subh',
                    required=True,
                    action='store_true',
                    help='foo the bars before frobbling')

parser.add_argument('--rich',
                    nargs='+',
                    default=50,
                    help='one of the bars to be frobbled')

parser.add_argument('--momo',
                    nargs='?',
                    type=int,
                    default=42,
                    help='the bar to %(prog)s (default: %(default)s)')

# print(parser.parse_args(['--foo', 'BAR']))

args = parser.parse_args()
