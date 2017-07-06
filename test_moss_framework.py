#! /usr/bin/env python

import json
import moss

from moss import MossDeviceOrchestrator
from moss import MossTaskOrchestrator
from moss.utils import pretty_print

neighbor_ip = 'fd35:1:1:2::8'
port_id = 'eth0'

@moss.framework.get_ipv6_route_table()
def test_function(connection):
    pass


def main():
    device = MossDeviceOrchestrator(
        device_type = 'linux',
        ip = '127.0.0.1',
        username = 'root',
        password = 'moss-test',
    )

    task = MossTaskOrchestrator(
        device = device
    )

    task.add_task(task_name = 'get_system_uptime')
    task.add_task(task_name = 'get_system_info')
    task.add_task(task_name = 'get_interface_description', argument = 'eth0')
    task.add_task(task_name = 'get_interface_statistics', argument = 'eth0', failure_next_task = 'get_bgp_memory_usage')
    task.add_task(task_name = 'get_ipv6_addresses')
    task.add_task(task_name = 'get_bgp_memory_usage')

    #print task.show_steps()

    result = task.run()
    #pretty_print(result)

main()
