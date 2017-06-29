#!/usr/bin/env python

from dev_ops.linux import get_ndp_table

def linux_get_ndp_table_stale_entries():
    def decorator(connection):
        def wrapper(connection):
            '''
            Summary:
            Returns the IPv6 Neighbor Discovery Protocol table in a JSON format
            and parses the output for stale entries.

            Arguments:
            connection:         object, MossDeviceOrchestrator

            Returns:
            dict
            '''

            task_info = {
                'namespace': 'ndp',
                'task': 'get_ndp_table_stale_entries',
                'platform': 'linux',
                'subtool': 'native'
            }

            output_dict = get_ndp_table(connection)

            if output_dict['result'] == 'fail':
                output_dict.update(task_info)
                return output_dict

            stale_entries_dict = {}

            for entry in output_dict['stdout']:
                if entry['state'] == 'STALE':
                    stale_entries_dict.update(entry)

            output_dict['stdout'] = stale_entries_dict
            output_dict.update(task_info)

            return output_dict

        return wrapper
    return decorator
