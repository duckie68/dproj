#!/usr/bin/env python3

'''Script for project management'''

import os
import sys
import datetime
from configparser import ConfigParser

'''Setting variables'''

home = os.environ['HOME']
date = datetime.date.today()
year = date.year
data_directory = home + '/.local/share/dproj/skeletons/'
config_directory = home + '/.config/dproj/'


try:
    skeletons = [i for i in os.listdir(data_directory) if os.path.isdir(data_directory + i)]
except:
    print("User has no skeleton projects.  See https://github.com/dproj for instructions")

def test_data():
    '''Tests if a user config directory exists'''
    if os.path.isdir(config_directory):
        return
    else:
        make_config()

def make_config():
    '''Creates a user config directory and populates with common constants'''
    name = ''
    email = ''
    base = ''
    print("User has no configuration file")
    print("Creating configuraation directory in " + config_directory)
    os.mkdir(config_directory)
    print("Directory created.")
    name = input("Please input your full name ")
    email = input("Please input your email address ")
    print("Please input the base directory for all of your projects")
    base = input("Your templates will be generated in " + home + " + this directory ")
    print("Thank you. Now writing to " + config_directory + "initrc")
    config_object = ConfigParser()
    config_object["USERINFO"] = {
        'name': name,
        'email': email,
        'work_directory': base
    }
    with open(config_directory + 'initrc', 'w') as conf:
        config_object.write(conf)

'''Ensure a config file exists, then assign data to variables'''
test_data()
config_data = ConfigParser()
config_data.read(config_directory + 'initrc')
userinfo = config_data["USERINFO"]
name = userinfo['name']
email = userinfo['email']
work_directory = userinfo['work_directory']
