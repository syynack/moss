#!/usr/bin/env python

from moss.framework.decorators import register

@register(platform = 'juniper')
def juniper_set_bgp_local_preference(connection, group = None, local_pref = 0, delete = False):
    '''
    Summary:
    Set the Border Gateway Protocol Local Preference path selection attribute on a Juniper
    device.

    Arguments:
    group                   str, name of BGP group to apply local pref
    local_pref              int, value of local pref to be set
    delete                  bool, delete the configuration statement rather than set

    Returns:
    dict
    '''

    if group is None:
        return {
            'result': 'fail',
            'reason': 'BGP group is not defined.'
        }

    if not connection.check_config_mode():
        connection.config_mode()

    if not delete:
        command = 'set protocols bgp group {} local-preference {}'.format(group, local_pref)
    else:
        command = 'delete protocols bgp group {} local-preference {}'.format(group, local_pref)
        
    result = connection.send_command(command)

    if 'missing argument' in result:
        return {
            'result': 'fail',
            'reason': 'Unable to execute command',
            'stdout': result
        }

    result = connection.commit(and_quit = True, comment = 'MOSS: LOCAL_PREF {} APPLIED TO {}.'.format(local_pref, group))

    return {
        'result': 'success'
    }
