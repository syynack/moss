#!/usr/bin/env python

from moss.framework.decorators import register

@register(platform = 'cisco_ios', group = 'devops')
def cisco_ios_get_facts(connection):
    if connection.check_enable_mode() == False:
        connection.enable()

    command = 'show version'
    output = connection.send_command(command)

    return output
