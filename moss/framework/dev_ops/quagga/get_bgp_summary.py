#!/usr/bin/env python

import re

def get_bgp_summary(connection):
    command = 'vtysh -c "show bgp summary"'
    output = connection.send_command(command)

    if output is None or 'failed' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {"summary": []}
    info_regexes = [
        'identifier\s(?P<bgp_rid>([0-9]{1,3}\.){3}[0-9]{1,3}),\slocal\sAS\snumber\s(?P<local_as>[^\s]+)\svrf-id\s(?P<vrf>[^\n]+)',
        'BGP\stable\sversion\s(?P<table_ver>[^\n]+)',
        'RIB\sentries\s(?P<rib_entries>[^,]),\susing\s(?P<rib_memory_usage>.*)\sof\smemory',
        'Peers\s(?P<total_peers>[^,]+),\susing\s(?P<peer_memory_usage>.*)\sof\smemory',
        'Peer\sgroups\s(?P<total_peer_groups>[^,]),\susing\s(?P<peer_group_memory_usage>.*)\sof\smemory'
    ]

    neighbor_regex = '(?P<neighbor_ip>.*)\s\s(?P<version>4)[\s]+(?P<as>[^\s]+)[\s]+(?P<msg_recv>[^\s]+)[\s]+' \
                     '(?P<msg_sent>[^\s]+)[\s]+(?P<table_ver>[^\s]+)[\s]+(?P<inq>[^\s]+)[\s]+' \
                     '(?P<outq>[^\s]+)[\s]+(?P<up_down>[^\s]+)[\s]+(?P<state_pfx_recv>[^\s]+)'

    for line in output.splitlines():
        neighbor_match = re.match(neighbor_regex, line, re.MULTILINE)

        if neighbor_match:
            stdout['summary'].append(neighbor_match.groupdict())
        else:
            for regex in info_regexes:
                info_match = re.search(regex, line)

                if info_match:
                    stdout.update(info_match.groupdict())

    return {
        'result': 'success',
        'stdout': stdout
    }
