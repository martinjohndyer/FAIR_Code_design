import argparse

parser = argparse.ArgumentParser(description='This program is an example of command line interface in Python',
    epilog='Author: R. Thomas, 2024, UoS')


parser.add_argument('file')               # positional argument (mandatory)
parser.add_argument('file2')              # positional argument (mandatory)
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-n')                 # option that takes a value
parser.add_argument('--max')              # option that takes a value

args = parser.parse_args()
