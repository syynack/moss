#!/usr/bin/env python

from dev_ops.linux import get_system_info

def linux_get_system_info():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Runs 'uname' with additional on a linux box to return the system
            information: kernel name, hostname, kernel release, architecture,
            processor, hardware_platform, operating_system

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'system',
                'task': 'get_system_info',
                'platform': 'linux',
                'subtool': 'native'
            }
            
            output_dict = get_system_info(connection)
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
