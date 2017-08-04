#! /usr/bin/env python

# Created by moss-ctrl.
# This file should be used as a template for any user created modules.

from moss import ModuleResult, execute_device_operation, run, register, diagnose_interfaces

# ModuleResult can be used to influence the outcome of a task.
#    return ModuleResult.complete                   The module will complete successfully and the task will not proceed
#    return ModuleResult.branch('module_name')      Task will branch to module defined and continue from there
#    return ModuleResult.fail                       Module will be marked as a failure and the task will not continue
#    return ModuleResult.success                    Module will be marked as a success and the task will continue
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
# diagnose_interfaces can be used when executing get_interfaces_statistics to check if any interface is erroring or dicarding
#
#
# Common standards:
#       - the connection variable must be passed to each registered module.
#       - each registered module must be decorated with @register with the target platform specified.

PLATFORM = 'linux'

@register(platform = PLATFORM)
def shut_offending_interface(connection, context):
    ''' Example module to place an offending interface into an administrative down state in Quagga. '''

    for interface in context['offending_interfaces']:
        shut_interface_result = execute_device_operation(
            'linux_set_interface_admin_status',
            connection,
            status = 'down',
            interface = interface
        )

        if shut_interface_result['result'] == 'fail':
            return ModuleResult.fail
