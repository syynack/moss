#! /usr/bin/env python

import sys
import time

class TaskOrchestrator(object):

    '''
    Summary:
    Constructs a TaskOrchestrator object holding variables for executing a series of
    moss framework tasks in sequence.

    Takes:
    task_order          list, list of functions to execute sequentially
    ignore_failures     bool, ignore returned failures
    device              object, Netmiko SSH object from device_orchestrator

    Returns:
    dict

    '''

    def __init__(self, task_order=[], ignore_failures=False, device=''):
        self.task_order = task_order
        self.ignore_failures = ignore_failures
        self.device = device


    def run(self):
        if not self.task_order:
            print 'task_order is empty. Define tasks in task_order for the module to run.'
            sys.exit()

        if self.device == '':
            print 'Could not find a valid device. Define a device from DeviceOrchestrator as device.'
            sys.exit()

        result_dict = {'tasks_ran': []}
        total_tasks_ran = 0

        connection = self.device.get_connection()

        start_time = time.time()
        for task in self.task_order:

            total_tasks_ran += 1

            try:
                result = globals()[task]()
            except KeyError as e:
                print 'Unable to find function "{}".'.format(task)
                sys.exit()

            decorator = result(connection)
            result = decorator(connection)

            if result['result'] == 'fail':
                if not ignore_failures:
                    print 'placeholder, needs to be coloured, task failed'

            # add colours

            result_dict['tasks_ran'].append({
                'task_namespace': result['namespace'],
                'task_id': result['task'],
                'result': result['result'],
                'stdout': result['stdout']
            })

        end_time = time.time()
        run_time = end_time - start_time
        result_dict['total_tasks_ran'] = total_tasks_ran
        result_dict['start_time'] = start_time
        result_dict['end_time'] = end_time
        result_dict['run_time'] = run_time

        return result_dict
