import argparse


def echo():
    parser = argparse.ArgumentParser()
    parser.add_argument("echo",
                        help="echo the string you use here")
    args = parser.parse_args()
    return args.echo


def square():
    parser = argparse.ArgumentParser()
    parser.add_argument("square",
                        help="Displays a square of a given number",
                        type=int)
    args = parser.parse_args()
    return (args.square**2)


if __name__ == '__main__':
    print(square())
