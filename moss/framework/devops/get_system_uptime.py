#!/usr/bin/env python

import re
from moss.framework.decorators import register

@register(platform = 'linux')
def linux_get_system_uptime(connection):
    '''
    Summary:
    Runs uptime on a Linux box to retrieve information regarding the uptime,
    users and CPU information.

    Example expected output of uptime:

     05:02:47 up 2 days,  7:38,  1 user,  load average: 0.00, 0.00, 0.00

    Arguments:
    connection:         object, MossDeviceOrchestrator object

    Returns:
    dict

    Example:
    "stdout": {
        "avg_15_min_load": "0.00",
        "avg_1_min_load": "0.00",
        "avg_5_min_load": "0.00",
        "current_time": "05:03:28",
        "uptime": "2 days",
        "users": "2"
    }
    '''

    command = 'uptime'
    output = connection.send_command(command)

    if output is None or 'not found' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    regexes = [
        '\s(?P<current_time>[0-9]{2}:[0-9]{2}:[0-9]{2})\sup',
        '\sup(?P<uptime>[^,]+.+?),.*user',
        '(?P<users>[^,]+)user.*load\saverage:',
        'load\saverage:(?P<avg_1_min_load>[^,]+),(?P<avg_5_min_load>[^,]+),(?P<avg_15_min_load>[^\n]+)'
    ]

    for line in output.splitlines():
        for regex in regexes:
            data = re.search(regex, line, re.MULTILINE)

            if data is not None:
                stdout.update(data.groupdict())

    for key, element in stdout.iteritems():
        stdout[key] = element.strip()

        if key == 'users':
            stdout['users'] = int(element)

        if 'load' in key:
            stdout[key] = float(element)

    return {
        'result': 'success',
        'stdout': stdout
    }


@register(platform = 'juniper')
def juniper_get_system_uptime(connection):
    '''
    Summary:
    Returns a dict containing uptime information from JunOS.

    Example ouput of 'show system uptime' is:

    Current time: 2017-09-08 22:04:43 UTC
    System booted: 2017-09-08 22:03:27 UTC (00:01:16 ago)
    Protocols started: 2017-09-08 22:03:38 UTC (00:01:05 ago)
    Last configured: 2017-09-08 21:34:14 UTC (00:30:29 ago) by root
    10:04PM  up 1 min, 1 user, load averages: 0.64, 0.32, 0.13

    Returns:
    dict

    Example:
    'stdout': {
        'current_date': '2017-09-08',
        'current_time': '22:04:43',
        'current_time_zone': 'UTC',
        'booted_date': '2017-09-08',
        'booted_time': '22:03:27',
        'booted_time_zone': 'UTC',
        'booted_last': '00:01:16',
        'protocols_date': '2017-09-08',
        'protocols_time': '22:03:38',
        'protocols_time_zone': 'UTC',
        'protocols_last': '00:01:05',
        'configured_date': '2017-09-08',
        'configured_time': '21:34:14',
        'configured_time_zone': 'UTC',
        'configured_last': '00:30:29',
        'configured_by': 'root'
    }
    '''

    command = 'show system uptime'
    output = connection.send_command(command)

    if output is None or 'unknown command.' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    regexes = [
        'Current\stime:\s(?P<current_date>[^\s]+)\s(?P<current_time>[^\s]+)\s(?P<current_time_zone>.*)',
        'System\sbooted:\s(?P<booted_date>[^\s]+)\s(?P<booted_time>[^\s]+)\s(?P<booted_time_zone>[^\s]+)\s\((?P<booted_last>[^\s]+)\sago\)',
        'Protocols\sstarted:\s(?P<protocols_date>[^\s]+)\s(?P<protocols_time>[^\s]+)\s(?P<protocols_time_zone>[^\s]+)\s\((?P<protocols_last>[^\s]+)\sago\)',
        'Last\sconfigured:\s(?P<configured_date>[^\s]+)\s(?P<configured_time>[^\s]+)\s(?P<configured_time_zone>[^\s]+)\s\((?P<configured_last>[^\s]+)\sago\)\sby\s(?P<configured_by>.*)'
    ]

    for line in output.splitlines():
        for regex in regexes:
            data = re.search(regex, line)
            if data is not None:
                data = data.groupdict()
                stdout.update(data)

    return {
        'result': 'success',
        'stdout': stdout
    }
