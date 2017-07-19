#! /usr/bin/env python

from moss import ModuleResult, execute_device_operation, module, register

@register(platform = 'linux')
def test_module_system_uptime(connection):
    ''' Test module for testing the way for executing modules '''

    result = execute_device_operation('linux_get_system_uptime', connection)

    if result['result'] == 'fail':
        return ModuleResult.fail

    if result['stdout']['users'] > 1:
        return ModuleResult.fail

    return ModuleResult.success
