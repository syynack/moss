#! /usr/bin/env python

from moss.module import ModuleResult, execute_device_operation
from moss.register import register

@register(platform = 'linux')
def test_module_bgp_memory_usage(connection):
    ''' Test module to run linux_get_interfaces_statistics and parse for a specific interface '''

    result = execute_device_operation('linux_get_bgp_memory_usage', connection)

    if result['result'] == 'fail':
        return ModuleResult.fail

    return ModuleResult.branch('test_module_system_uptime')
