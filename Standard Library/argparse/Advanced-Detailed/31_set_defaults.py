import argparse

# Used to put some default values in the command line
parser = argparse.ArgumentParser()
parser.add_argument('fooo', type=int)
parser.set_defaults(bar=42,
                    baz='badger')
print(parser.parse_args(['736']))
# Parser level defau;ts always override argument level defaults
parser.add_argument('--foo',
                    default='bar')
parser.set_defaults(foo='spam')
print(parser.parse_args([]))
