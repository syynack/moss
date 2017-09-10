#!/usr/bin/env python

from moss.framework.decorators import register

@register(platform = 'juniper')
def juniper_set_ospf_overload(connection, timeout = None):
    '''
    Summary:
    Sets OSPFv2 overload on a Juniper box for traffic engineering purposes.

    Arguments:
    timeout                 int, OSPFv2 overload timeout

    Returns:
    dict
    '''

    if not connection.check_config_mode():
        connection.config_mode()

    command = 'set protocols ospf overload' if not timeout else 'set protocols ospf overload timeout {}'.format(timeout)
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
