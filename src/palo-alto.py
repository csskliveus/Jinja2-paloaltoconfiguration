# Load palo alto templates

# 
#from yaml import load, dump
import yaml
from jinja2 import Environment, Template, FileSystemLoader

## --------------------------------------------------------------------------------------------------------------------
# vsys
config_data = yaml.load(open("../vsys-data.yml"),Loader=yaml.FullLoader) # loading yaml data

templateloader = FileSystemLoader("./templates/")
templateEnv    = Environment(loader=templateloader,trim_blocks='true',autoescape='true')

templateFile   = "palo-alto-vsys-working-template.xml"

template       = templateEnv.get_template(templateFile)
outputText     = template.render(config_data)  # 

with open("./templates/generated-vsys.xml", "w") as fh:
    fh.write(outputText)

## --------------------------------------------------------------------------------------------------------------------

## network
config_data = yaml.load(open("../network-data.yml"),Loader=yaml.FullLoader) # loading yaml data

# templateloader = FileSystemLoader("./templates/")
# templateEnv    = Environment(loader=templateloader,trim_blocks='true',autoescape='true')

templateFile   = "palo-alto-network-base-template.xml"

template       = templateEnv.get_template(templateFile)
outputText     = template.render(config_data)  # 

with open("./templates/generated-network.xml", "w") as fh:
    fh.write(outputText)

## --------------------------------------------------------------------------------------------------------------------

## main template
config_data = yaml.load(open("../data.yml"),Loader=yaml.FullLoader) # loading yaml data

# templateloader = FileSystemLoader("./templates/")
# templateEnv    = Environment(loader=templateloader,trim_blocks='true',autoescape='true')

templateFile   = "palo-alto-base-template.xml"  # palo-alto-base-working-template.xml

template       = templateEnv.get_template(templateFile)
outputText     = template.render(config_data)  # 

with open("./templates/generated-running-config.xml", "w") as fh:
    fh.write(outputText)

#print(outputText)