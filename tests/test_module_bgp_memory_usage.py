#! /usr/bin/env python

<<<<<<< HEAD
from moss import ModuleResult, execute_device_operation, module, register
=======
from moss.module import ModuleResult, execute_device_operation
from moss.register import register
>>>>>>> ab66192d9c3f61ae302e0d726ca94d413deaacbf

@register(platform = 'linux')
def test_module_bgp_memory_usage(connection):
    ''' Test module to run linux_get_interfaces_statistics and parse for a specific interface '''

    result = execute_device_operation('linux_get_bgp_memory_usage', connection)

    if result['result'] == 'fail':
        return ModuleResult.fail

    return ModuleResult.branch('test_module_system_uptime')
