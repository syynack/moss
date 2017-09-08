#!/usr/bin/env python

import re
from moss.framework.decorators import register

@register(platform = 'linux')
def linux_get_bgp_summary(connection):
    '''
    Summary:
    Returns a dict containing BGP summary information retrieved from Quagga.

    Example expected output of vtysh -c "show ip bgp summary" is:

    BGP router identifier 1.1.1.1, local AS number 1
    RIB entries 0, using 0 bytes of memory
    Peers 16, using 71 KiB of memory
    Peer groups 1, using 32 bytes of memory

    Neighbor        V    AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
    fd35:1:1:2::1   4   200       0       0        0    0    0 never    Active
    fd35:1:1:2::2   4   200       0       0        0    0    0 never    Active

    Total number of neighbors 2

    Returns:
    dict

    Depends:
    Quagga

    Example:
    "stdout": {
        "peer_group_memory_usage": "32 bytes",
        "peer_memory_usage": "71 KiB",
        "rib_entries": "0",
        "rib_memory_usage": "0 bytes",
        "summary": [
            {
                "as": "200",
                "inq": "0",
                "msg_recv": "0",
                "msg_sent": "0",
                "neighbor_ip": "fd35:1:1:2::1 ",
                "outq": "0",
                "state_pfx_recv": "Active",
                "table_ver": "0",
                "up_down": "never",
                "version": "4"
            },
            {
                "as": "200",
                "inq": "0",
                "msg_recv": "0",
                "msg_sent": "0",
                "neighbor_ip": "fd35:1:1:2::2 ",
                "outq": "0",
                "state_pfx_recv": "Active",
                "table_ver": "0",
                "up_down": "never",
                "version": "4"
            }
        ],
        "total_peer_groups": "1",
        "total_peers": "2"
    }
    '''

    command = 'vtysh -c "show ip bgp summary"'
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
