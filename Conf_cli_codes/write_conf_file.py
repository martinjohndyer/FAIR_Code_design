'''
This code is part of the Code design lecture.
It demonstrates how to wirte configuration files programatically.

Author: R.Thomas
Licence: CC-BY 4.0
'''

##Import the right library
from configparser import ConfigParser

##Create parser object
config = ConfigParser()


## Create config file. For each section in the file, you will create a dictionary
config['simulation'] = {'time_step': 1.0, 'total_time': 200.0}
config['environment'] = {'gravity': 9.81, 'air_resistance': 0.02}
config['initial_conditions'] = {'velocity': 5.0, 'angle': 30.0, 'height': 0.5}

##And finally  you will save it

with open('config_file_program.ini', 'w') as configfile: ##This open the condif_file_program.ini in write mode
    config.write(configfile)
