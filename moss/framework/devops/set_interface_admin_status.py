#! /usr/bin/env python

from moss.framework.decorators import register

@register(platform = 'linux')
def linux_set_interface_admin_status(connection, status = 'down', interface = None):
    '''
    Summary:
    Set an interface adminstrative status in Quagga.

    Arguments:
    status              string, up/down
    interface           string, interface name

    Returns
    dict
    '''

    commands = {
        'down': 'vtysh -c "conf t" -c "interface {}" -c "shutdown"'.format(interface),
        'up': 'vtysh -c "conf t" -c "interface {}" -c "no shutdown"'.format(interface)
    }

    if interface is None:
        return {
            'result': 'fail',
            'reason': 'No interface specified'
        }

    try:
        result = connection.send_command(commands[status.lower()])
    except KeyError as e:
        return {
            'result': 'fail',
            'reason': '{} is not an option'.format(status)
        }

    if "Can't shutdown interface" in result or "Can't up interface" in result:
        return {
            'result': 'fail',
            'reason': result
        }

    command = 'vtysh -c "show interface description" | grep {}'.format(interface)
    verification = connection.send_command(command)

    admin_status = verification.split()[1]

    if admin_status == status.lower():
        return {
            'result': 'success',
            'reason': verification
        }
    else:
        return {
            'result': 'fail',
            'reason': verification
        }
