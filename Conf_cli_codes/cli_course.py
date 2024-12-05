import argparse

parser = argparse.ArgumentParser(description='This program is an example of command line interface in Python',
    epilog='Author: R. Thomas, 2024, UoS')


parser.add_argument('file', help='input data file to the program')          # position argument
parser.add_argument('file2', help='Configuration file to the program')      # position argument
parser.add_argument('-c', '--count', help='Number of counts per iteration') # option that takes a value
parser.add_argument('-n', help='Number of iteration')                       # option that takes a value
parser.add_argument('--max', help='Maximum population per iteration')       # option that takes a value

args = parser.parse_args()


print(args) # Gives the namespace content
print(args.file) #direct access to the 1st positional argument
print(args.max) #direct access to the max optional argument
