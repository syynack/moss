#! /usr/bin/env python

# Created by moss-ctrl.
# This file should be used as a template for any user created modules.

from moss import ModuleResult, execute_device_operation, run, register

# ModuleResult can be used to influence the outcome of a task.
#    return ModuleResult.quit                       module will not be considered a failure, but will not continue
#    return ModuleResult.branch('module_name')      task will branch to module defined and continue from there
#    return ModuleResult.fail                       module will be marked as a failure and the task will not continue
#    return ModuleResult.success                    module will be marked as a success and the task will continue
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
# @module('linux_get_system_info', port_id = 'xe1')
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
# Common standards:
#       - the connection variable must be passed to each registered module.
#       - each registered module must be decorated with @register with the target platform specified.

PLATFORM = 'linux'

@register(platform = PLATFORM)
def test_module_system_uptime(connection):
    ''' Test module for testing the way for executing modules '''

    result = execute_device_operation('linux_get_system_uptime', connection)

    if result['result'] == 'fail':
        return ModuleResult.fail

    if result['stdout']['users'] > 1:
        return ModuleResult.fail
