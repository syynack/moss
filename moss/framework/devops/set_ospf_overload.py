#!/usr/bin/env python

from moss.framework.decorators import register

@register(platform = 'juniper')
def juniper_set_ospf_overload(connection, timeout = None, delete = False):
    '''
    Summary:
    Sets OSPFv2 overload on a Juniper box for traffic engineering purposes.

    Arguments:
    timeout                 int, OSPFv2 overload timeout, must be betweeen 60 and 1800
    delete                  bool, delete the configuration statement rather than set

    Returns:
    dict
    '''

    if int(timeout) > 1800 or int(timeout) < 60:
        return {
            'result': 'fail',
            'reason': 'Timeout must be between 60 and 1800.'
        }

    if not connection.check_config_mode():
        connection.config_mode()

    if not delete:
        command = 'set protocols ospf overload' if not timeout else 'set protocols ospf overload timeout {}'.format(timeout)
    else:
        command = 'delete protocols ospf overload'

    result = connection.send_command(command)

    if 'missing argument' in result or 'unknown command' in result:
        return {
            'result': 'fail',
            'reason': 'Unable to execute command',
            'stdout': result
        }

    result = connection.commit(and_quit = True, comment = 'MOSS: OSPF OVERLOAD APPLIED.')

    return {
        'result': 'success'
    }
