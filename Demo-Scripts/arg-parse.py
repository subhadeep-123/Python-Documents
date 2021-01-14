import time
import argparse
import textwrap


class Operations(object):
    def __init__(self):
        self.result = None

    def sum(self, a, b):
        self.result = a + b
        time.sleep(1)
        return self.result

    def sub(self, a, b):
        self.result = a - b
        time.sleep(1)
        return self.result

    def mult(self, a, b):
        self.result = a * b
        time.sleep(1)
        return self.result

    def div(self, a, b):
        self.result = a / b
        time.sleep(1)
        return self.result


if __name__ == "__main__":
    paser = argparse.ArgumentParser(prog='TLA',
                                    usage='%(prog)s [Options] -sm || --sum ...',
                                    description=textwrap.dedent('''
                                        This Program can used for 
                                        various mathematical operations
                                    '''),
                                    add_help=True,
                                    allow_abbrev=False,
                                    formatter_class=argparse.RawDescriptionHelpFormatter
                                    )
    paser.add_argument('-sm',
                       '--sum',
                       nargs=2,
                       type=int,
                       #    action='store_true',
                       help='Use it for Addition')
    paser.add_argument('-su',
                       '--sub',
                       nargs=2,
                       type=int,
                       #    action='store_true',
                       help='Use it for Substraction')
    paser.add_argument('-mu',
                       '--mult',
                       nargs=2,
                       type=int,
                       #    action='store_true',
                       help='Use it for Multiplication')
    paser.add_argument('-dv',
                       '--div',
                       nargs=2,
                       type=int,
                       #    action='store_true',
                       help='Use it for Division')
    paser.add_argument('-a',
                       '--all',
                       nargs=2,
                       type=int,
                       #    action='store_true',
                       help='Use it for Doing Everything at once')
    try:
        args = paser.parse_args()
    except argparse.ArgumentError:
        print("Caught an exception")
    obj = Operations()
    if args.sum:
        print(
            f"The Result of Addition is - {obj.sum(args.sum[0], args.sum[1])}")
    elif args.sub:
        print(
            f"The Result of Substraction is - {obj.sub(args.sub[0], args.sub[1])}")
    elif args.mult:
        print(
            f"The Result of Multiplication is - {obj.mult(args.mult[0], args.mult[1])}")
    elif args.div:
        print(
            f"The Result of Division is - {obj.div(args.div[0], args.div[1])}")
    elif args.all:
        print(
            f"The Result of Addition is - {obj.sum(args.all[0], args.all[1])}")
        print(
            f"The Result of Substraction is - {obj.sub(args.all[0], args.all[1])}")
        print(
            f"The Result of Multiplication is - {obj.mult(args.all[0], args.all[1])}")
        print(
            f"The Result of Division is - {obj.div(args.all[0], args.all[1])}")
    else:
        paser.print_help()
