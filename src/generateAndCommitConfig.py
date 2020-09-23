#!/usr/bin/python
# Load palo alto templates

# 
#from yaml import load, dump
import yaml
from jinja2 import Environment, Template, FileSystemLoader
import subprocess

## --------------------------------------------------------------------------------------------------------------------
# vsys
config_data = yaml.load(open("../vsys-data.yml"),Loader=yaml.FullLoader) # loading yaml data

templateloader = FileSystemLoader("./templates/")
templateEnv    = Environment(loader=templateloader,trim_blocks='true',autoescape='true')

templateFile   = "vsys-working-template.xml"

template       = templateEnv.get_template(templateFile)
outputText     = template.render(config_data)  # 

with open("./templates/generated-vsys.xml", "w") as fh:
    fh.write(outputText)

print("vsys template is generated")
print("\n")

## --------------------------------------------------------------------------------------------------------------------

## network
config_data = yaml.load(open("../network-data.yml"),Loader=yaml.FullLoader) # loading yaml data

# templateloader = FileSystemLoader("./templates/")
# templateEnv    = Environment(loader=templateloader,trim_blocks='true',autoescape='true')

templateFile   = "network-base-template.xml"

template       = templateEnv.get_template(templateFile)
outputText     = template.render(config_data)  # 

with open("./templates/generated-network.xml", "w") as fh:
    fh.write(outputText)

print("network template is generated")
print("\n")

## --------------------------------------------------------------------------------------------------------------------
# 
# To Do - Export running configuration from palo-alto. [we have current ]
# Get password hash from running-config for selected user [1 user].
# Replace phash in the template.

## main template
config_data = yaml.load(open("../data.yml"),Loader=yaml.FullLoader) # loading yaml data

# templateloader = FileSystemLoader("./templates/")
# templateEnv    = Environment(loader=templateloader,trim_blocks='true',autoescape='true')

templateFile   = "base-template.xml"  # palo-alto-base-working-template.xml

template       = templateEnv.get_template(templateFile)
outputText     = template.render(config_data)  # 

with open("./templates/generated-running-config.xml", "w") as fh:
    fh.write(outputText)

print("template 'generated-running-config.xml' is generated. Please check templates folder")
print("\n")

print("calling shell script to upload configuration into palo-alto")
print("\n")
call_with_args="bash ./commitconfiguration.sh '%s' '%s' '%s' '%s'" %('1.1.1.1', 'testuser', 'test', 'generated-running-config.xml')
print(call_with_args)

subprocess.call(call_with_args,shell=True)
