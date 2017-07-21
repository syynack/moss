#!/usr/bin/env python

import re
from moss.register import register

@register(platform = 'linux')

def linux_get_bgp_neighbors(connection):
    command = 'vtysh -c "show bgp neighbors"'
    output = connection.send_command(command)

    if output is None or 'failed' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    neighbor_regex = 'remote\sAS\s(?P<remote_as>[^,]),\slocal\sAS\s(?P<local_as>[^,]),\s(?P<type>.*)\slink'
    regexes = [
        'Member\sof\speer-group\s(?P<peer_group>.*)\sfor\ssession\sparameters',
        'BGP\sversion\s(?P<version>[^,]),\sremote\srouter\sID\s(?P<remote_router_id>[^\n]+)',
        'BGP\sstate\s=\s(?P<state>[^\n]+)',
        'Last\sread\s(?P<last_read>[^,]+),\sLast\swrite\s(?P<last_write>[^\n]+)',
        'Hold\stime\sis\s(?P<dead_time>[^,]+),\skeepalive\sinterval\sis\s(?P<hello_time>[^\s]+)\sseconds',
        'Inq\sdepth\s\is\s(?P<inq_depth>[^\n])',
        'Outq\sdepth\s\is\s(?P<outq_depth>[^\n])',
        'Opens:[\s]+(?P<opens_sent>[^\s]+)[\s]+(?P<opens_rcvd>[^\s])',
        'Notifications:[\s]+(?P<notifications_sent>[^\s]+)[\s]+(?P<notifications_rcvd>[^\s])',
        'Updates:[\s]+(?P<updates_sent>[^\s]+)[\s]+(?P<updates_rcvd>[^\s])',
        'Keepalives:[\s]+(?P<keepalives_sent>[^\s]+)[\s]+(?P<keepalives_rcvd>[^\s])',
        'Route\sRefresh:[\s]+(?P<route_refreshes_sent>[^\s]+)[\s]+(?P<route_refreshes_rcvd>[^\s])',
        'Capability:[\s]+(?P<capabilities_sent>[^\s]+)[\s]+(?P<capabilities_rcvd>[^\s])',
        'Total:[\s]+(?P<total_sent>[^\s]+)[\s]+(?P<total_rcvd>[^\s])',
        'Minimum\stime\sbetween\sadvertisement\sruns\sis\s(?P<min_advert_runs>[^\n]+)',
        'BGP\sConnect\sRetry\sTimer\sin\sSeconds:\s(?P<connect_retry_timer>[^\n])',
        'Next\sconnect\stimer\sdue\sin\s(?P<next_connect_retry_timer>[^\n]+)',
        'Read\sthread:\s(?P<read_thread>[^\s]+)\s\sWrite\sthread:\s(?P<write_thread>[^\n]+)'
    ]

    for line in output.splitlines():
        if 'BGP neighbor is' in line:
            line = line.split()
            neighbor_address = line[3][:-1]
            stdout[neighbor_address] = {}

            match = re.search(neighbor_regex, ' '.join(line))

            if match:
                stdout[neighbor_address].update(match.groupdict())
        else:
            for regex in regexes:
                match = re.search(regex, line)

                if match:
                    stdout[neighbor_address].update(match.groupdict())

    return {
        'result': 'success',
        'stdout': stdout
    }
