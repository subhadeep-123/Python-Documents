import argparse

"""
By default, ArgumentParser groups command-line arguments into “positional arguments” and “optional arguments” 
when displaying help messages. When there is a better conceptual grouping of arguments than this default one, 
appropriate groups can be created using the add_argument_group() method:
"""
parser = argparse.ArgumentParser(prog='PROG',
                                 add_help=False)
group1 = parser.add_argument_group('Group 1')
group1.add_argument('-f',
                    '--foo',
                    help='foo help')
group2 = parser.add_argument_group('Group 2')
group2.add_argument('bar',
                    help='bar help')
parser.print_help()
