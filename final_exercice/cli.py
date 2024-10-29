import argparse

parser = argparse.ArgumentParser(prog='My program',
                                 description='This program is an example of command line interface in Python',
                                 epilog='Author: R. Thomas, 2024, UoS')


parser.add_argument('file', help='input data file to the program')     # positional argument
parser.add_argument('file2', help='Configuration file to the program') # positional argument
parser.add_argument('-c', '--count', help=' Number of counts per iteration')  # option that takes a value
parser.add_argument('-n', help='Number of iteration')                   # option that takes a value
parser.add_argument('--max', help='Maximum population per iteration')   # option that takes a value
args = parser.parse_args()

print(args)
print(args.file)
print(args.count)
print(args.max)

