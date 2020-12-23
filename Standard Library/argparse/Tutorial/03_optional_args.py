import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbose",
                    help="Increase output verbosity",
                    action="store_true")
args = parser.parse_args()

if args.verbose:
    print("Verbosity turrned on")
