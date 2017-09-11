#!/usr/bin/env python

import re

from moss.framework.decorators import register

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


@register(platform = 'juniper')
def juniper_get_bgp_neighbors(connection):
    command = 'show bgp neighbor'
    output = connection.send_command(command)

    if output is None or 'error' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = []
    regex = 'Peer:\s(?P<peer_connection>[^\s]+)\sAS\s(?P<peer_as>[^\s]+).+Local:\s(?P<local_connection>[^\s]+)\sAS\s(?P<local_as>[^\s]+)' \
            'Type:\s(?P<type>[^\s]+).+State:\s(?P<state>[^\s]+).+Flags:\s<(?P<flags>.*)>' \
            'Last\sState:\s(?P<last_state>[^\s]+).+Last\sEvent:\s(?P<last_event>.+)' \
            'Last\sError:\s(?P<last_error>.+)' \
            'Export:\s\[\s(?P<export>.*)\s\]' \
            'Options:\s<(?P<options>.*)>' \
            'Holdtime:\s(?P<holdtime>[^\s]+)\sPreference:\s(?P<preference>[^\s]+)\sLocal\sAS:\s(?P<local_as>[^\s]+)\sLocal\sSystem\sAS:\s(?P<local_sys_as>.+)' \
            'Number\sof\sflaps:\s(?P<number_of_flaps>.+)' \
            'Last\sflap\sevent:\s(?P<last_flap_event>.+)' \
            'Peer\sID:\s(?P<peer_id>[^\s]+).+Local\sID:\s(?P<local_id>[^\s]+).+Active\sHoldtime:\s(?P<active_holdtime>.+)' \
            'Keepalive\sInterval:\s(?P<keepalive_interval>[^\s]+).+Peer\sindex:\s(?P<peer_index>[^\s]+)' \
            'BFD:\s(?P<bfd_status>.+)' \
            'Local\sInterface:\s(?P<local_interface>[^\s]+)' \
            'NLRI\sfor\srestart\sconfigured\son\speer:\s(?P<configured_peer_nlri>[^\s]+)' \
            'NLRI\sadvertised\sby\speer:\s(?P<advertised_peer_nlri>[^\s]+)' \
            'NLRI\sfor\sthis\ssession:\s(?P<session_nlri>[^\s]+)' \
            'Stale\sroutes\sfrom\speer\sare\skept\sfor:\s(?P<stale_route_lifetime>[^\s]+)' \
            'RIB\sState:\s(?P<rib_state>.+)' \
            'Send\sstate:\s(?P<send_state>.+)' \
            'Active\sprefixes:[\s]+(?P<active_prefixes>[^\s]+)' \
            'Received\sprefixes:[\s]+(?P<received_prefixes>[^\s]+)' \
            'Accepted\sprefixes:[\s]+(?P<accepted_prefixes>[^\s]+)' \
            'Suppressed\sdue\sto\sdamping:[\s]+(?P<dampened_prefixes>[^\s]+)' \
            'Advertised\sprefixes:[\s]+(?P<advertised_prefixes>[^\s]+)' \
            'Input\smessages:.+Total\s(?P<input_total>[^\s]+).+Updates\s(?P<input_updates>[^\s]+).+Refreshes\s(?P<input_refreshes>[^\s]+)\sOctets\s(?P<input_octects>[^\s]+)' \
            'Output\smessages:.+Total\s(?P<input_total>[^\s]+).+Updates\s(?P<input_updates>[^\s]+).+Refreshes\s(?P<input_refreshes>[^\s]+)\sOctets\s(?P<input_octects>[^\s]+)'

    for line in output.splitlines():
        match = re.match(regex, line, re.MULTILINE)

        if match is not None:
            stdout.append(match.groupdict())

    return {
        'result': 'success',
        'stdout': stdout
    }
