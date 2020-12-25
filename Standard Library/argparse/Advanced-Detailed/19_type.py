import argparse
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument('count',
                    type=int)
parser.add_argument('dist',
                    type=float)
parser.add_argument('st',
                    type=ascii)
parser.add_argument('code_point',
                    type=ord)
parser.add_argument('source_file',
                    type=open)
parser.add_argument('dest',
                    type=argparse.FileType('w',
                                           encoding='latin-1'))
parser.add_argument('datapath',
                    type=pathlib.Path)
