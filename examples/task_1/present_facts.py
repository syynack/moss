#! /usr/bin/env python

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

PLATFORM = 'cisco_ios'

@register(platform = PLATFORM)
def present_facts(connection, context):
    execute_device_operation('cisco_ios_get_facts', connection)




#! /usr/bin/env python

# Created by framework-cli.
# This file should be used as a template for any user created modules.

from framework import ModuleResult, execute_device_operation

# ModuleResult can be used to influence the outcome of a task.
#    ModuleResult.success            Module will be marked as a success and will continue (this is implicit)
#    ModuleResult.fail               Module will be marked as a failure and task will not continue
#    ModuleResult.branch             Module will branch to another module
#    ModuleResult.retry              Module will be retried
#    ModuleResult.end                Module will be marked as successful but task will not continue

@register(vendor = '')
def module_template(connection, store):
    return ModuleResult.success
