'''
This code is part of the Code design lecture.
It demonstrates how to read configuration files

Author: R.Thomas
Licence: CC-BY 4.0
'''

##Import the right library
import configparser

##Create parser object
parser = configparser.ConfigParser()

##Load the file
parser.read('config.ini')

###look at all sections
print(parser.sections())




