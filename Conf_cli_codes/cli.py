'''
This code is part of the Code design lecture.
It demonstrates how to read configuration files

This code works with the file config.ini provided next to this current file.

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

##You can also check that a section exists
print(parser.has_section('simulation'))
print(parser.has_section('Finalstate'))

####Get all items in a section
options_in_simulation = parser.options('simulation')
print(options_in_simulation)


items_in_simulation = parser.items('simulation')
print(items_in_simulation)

###And check what are inside the sections
print(parser['simulation']['time_step']) 
print(parser.get('simulation', 'time_step'))




