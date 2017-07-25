
ENDPOINTS_BASE_TEXT = '''# This file is used to define endpoint information to be used when executing
# tasks. This information is what shall be used when attempting to connect
# to the target endpoints.


# Authentication
# Define a global password to be used for all device connections
global_password: ''

# Define a global username to be used for all device connections
global_username: ''


# Endpoints
# Define a global os if all the endpoints run the same operating system
global_os: ''

# Define endpoint information
endpoints:

# Example
- os: 'linux'
  ip: '192.168.0.1'

- os: 'cisco_ios'
  ip: '192.168.0.2'
'''

TASK_BASE_TEXT = '''# This file is used to define task stages to be executed within the task.

# Task
task:

# Example
- 'get_interfaces_descriptions'
- 'get_system_uptime'

'''

MODULE_BASE_TEXT = '''#! /usr/bin/env python

# This file should be used as a template for any user created modules
from moss.register import register

PLATFORM = ''
COMMAND = ''


@register(platform = PLATFORM)
def module_name(connection):
    command = connection.send_command(COMMAND)
'''
