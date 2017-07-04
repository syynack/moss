#! /usr/bin/env python

import json
import moss

from moss import MossDeviceOrchestrator

neighbor_ip = 'fd35:1:1:2::8'
port_id = 'eth0'

@moss.framework.get_ipv6_route_table()
def test_function(connection):
    pass


def main():
    device = MossDeviceOrchestrator(
        device_type = 'linux',
        ip = 'localhost',
        username = 'root',
        password = 'moss-test',
    )

    connection = device.get_connection()
    output = test_function(connection)

    print json.dumps(output, sort_keys=True, indent=4)


main()
