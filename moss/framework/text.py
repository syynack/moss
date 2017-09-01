
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

# Created by moss-ctrl.
# This file should be used as a template for any user created modules.

from moss import ModuleResult, execute_device_operation, run, register, diagnose_interfaces

# ModuleResult can be used to influence the outcome of a task.
#    ModuleResult.end                Module will be marked as successful but task will not continue
#    ModuleResult.branch             Module will branch to another module
#    ModuleResult.fail               Module will be marked as a failure and task will not continue
#    ModuleResult.success            Module will be marked as a success and will continue (this is implicit)
#    ModuleResult.retry              Module will be retried
# It is not required that a module result must be returned, by default the module will
# be marked as a success if not specified otherwise.
#
#
# execute_device_operation is a function designed to allow the module to run devops scripts e.g:
# result = execute_device_operation('linux_get_system_info', connection)
#
# The devops script name and connection are mandatory arguments, if the script takes more than those arguments,
# others can be passed in the form of kwargs e.g:
# result = execute_device_operation('linux_get_system_info', connection, port_id = 'xe1')
#
#
# module is to be used as a decorator for functions if the module is complex and the user demands more structure.
# @module('linux_get_system_info')
# def get_system_info(connection):
#     pass
#
# devops arguments are treated in the same way as execute_device_operation e.g:
# @run('linux_get_system_info', port_id = 'xe1')
# def get_system_info(connection):
#     pass
#
#
# register is used to add modules to the moss registry. If a moudle has not been registered moss will not be
# able to run it. Functions that must be executed as module must be decorated with register e.g:
# @register(platform = 'cisco_ios')
# def get_cisco_ios_version(connection):
#     pass
#
#
# diagnose_interfaces can be used when executing get_interfaces_statistics to check if any interface is erroring or discarding

PLATFORM = ''

@register(platform = PLATFORM)
def module_name(connection, context):
    return ModuleResult.success


'''
