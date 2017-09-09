#!/usr/bin/env python

from moss.framework.decorators import register

@register(platform = 'juniper')
def juniper_set_bgp_med(connection, group = None, policy_statement = None):
    '''
    Summary:
    Sets the Border Gateway Protocol Multiple Exit Descriminator for a specific
    predefined group of neighbors.

    Arguments:
    group                   str, name of BGP group to apply policy
    policy_statement        str, name of policy statement to apply to group

    Returns:
    dict
    '''

    if group is None or policy_statement is None:
        return {
            'result': 'fail',
            'reason': 'group or policy_statement is not defined.'
        }

    if not connection.check_config_mode():
        connection.config_mode()

    command = 'set protocols bgp group {} export {}'.format(group, policy_statement)
    result = connection.send_command(command)

    if 'missing argument' in result:
        return {
            'result': 'fail',
            'reason': 'Unable to execute command',
            'stdout': result
        }

    result = connection.commit(and_quit = True, comment = 'MOSS: POLICY {} APPLIED TO {}.'.format(policy_statement, group))

    return {
        'result': 'success'
    }
