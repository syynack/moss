#!/usr/bin/env python

from moss.framework.decorators import register

@register(platform = ['cisco_ios', 'cisco_asa', 'cisco_nxos', 'juniper', 'linux'])
def run_shell_command(connection, command = None):
    '''
    Summary:
    Essentially a wrapper for netmiko send_command.

    Arguments:
    command                 string, command to be sent to the device.

    Return:
    str
    '''

    result = connection.send_command(command)
    return result
