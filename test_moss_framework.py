#! /usr/bin/env python

import json
import moss

from moss import MossDeviceOrchestrator
from moss import MossTaskOrchestrator
from moss.utils import pretty_print

neighbor_ip = 'fd35:1:1:2::8'
port_id = 'eth0'

@moss.framework.get_bgp_memory_usage()
def test_function(connection):
    pass


def main():
    device = MossDeviceOrchestrator(
        device_type = 'linux',
        ip = '127.0.0.1',
        username = 'root',
        password = 'moss-test',
    )

    print test_function(device.get_connection())

main()
