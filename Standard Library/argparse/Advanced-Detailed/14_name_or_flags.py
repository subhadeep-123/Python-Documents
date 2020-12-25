import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-f',
                    '--foo')
parser.add_argument('bar')
parser.parse_args(['BAR'])

print(parser.parse_args(['BAR']))
print(parser.parse_args(['BAR', '--foo', 'FOO']))
print(parser.parse_args(['--foo', 'FOO']))
