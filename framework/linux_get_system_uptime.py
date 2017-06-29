#!/usr/bin/env python

from dev_ops.linux import get_system_uptime

def linux_get_system_uptime():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Runs 'uptime' on a linux box to return the uptime status as well
            as CPU load, users, and current time

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''
            task_info = {
                'namespace': 'system',
                'task': 'get_system_uptime',
                'platform': 'linux',
                'subtool': 'native'
            }
            
            output_dict = get_system_uptime(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
