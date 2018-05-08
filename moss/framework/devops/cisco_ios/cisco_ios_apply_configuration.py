#!/usr/bin/env python

from moss.framework.decorators import register

@register(vendor = 'cisco_ios')
def cisco_ios_apply_configuration(connection, config_statements):
    if not isinstance(config_statements, list):
        return {
            'result': 'fail',
            'stdout': 'Configuration statements must be in a list.'
        }

    output = connection.send_config_set(config_statements)

    if 'Invalid input detected' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    return {
        'result': 'success',
        'stdout': output.splitlines()
    }