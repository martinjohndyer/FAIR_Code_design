##Import the package
import configparser

###create the object
config = configparser.ConfigParser()

##read the file
config.read('conf_fruit.ini')

#print(config.sections())
#-->['fruits', 'vegetables']

config['fruits']['oranges'] = str(5)
config['vegetables']['beetroots'] = str(2)

config['pastries'] = {'croissants': '3'}


print(config.sections())

with open('new_conf_fruits', 'w') as openconfig:
    config.write(openconfig)