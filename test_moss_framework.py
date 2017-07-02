#! /usr/bin/env python

import json
import moss

from moss import MossDeviceOrchestrator

neighbor_ip = 'fd35:1:1:2::8'

@moss.framework.quagga_get_bgp_summary()
def test_function(connection):
    pass


def main():
    device = MossDeviceOrchestrator(
        device_type = 'linux',
        ip = 'localhost',
        username = 'root',
        password = 'moss-test',
    )

    # Getting results from task
    # task = TaskOrchestrator(
    #     task_order = [
    #         'get_system_uptime',
    #         'get_system_info'
    #     ],
    #     device = device
    # )
    #
    # output = task.run()
    #
    # print json.dumps(output, sort_keys=True, indent=4)

    # Getting results from decorator
    connection = device.get_connection()

    output = test_function(connection)

    print json.dumps(output, sort_keys=True, indent=4)


main()
