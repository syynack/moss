#!/usr/bin/env python

import pytest
import re

CLI_OUTPUT = '''
Current time: 2017-09-08 22:04:43 UTC
System booted: 2017-09-08 22:03:27 UTC (00:01:16 ago)
Protocols started: 2017-09-08 22:03:38 UTC (00:01:05 ago)
Last configured: 2017-09-08 21:34:14 UTC (00:30:29 ago) by root
10:04PM  up 1 min, 1 user, load averages: 0.64, 0.32, 0.13

'''

def _run_juniper_get_system_uptime():
    command = 'show system uptime'
    output = CLI_OUTPUT

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


@pytest.mark.parametrize('expected_result', [
    ({
        'result': 'success',
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
    })
])
def test_juniper_get_system_uptime(expected_result):
    result = _run_juniper_get_system_uptime()
    print result
    assert result == expected_result
