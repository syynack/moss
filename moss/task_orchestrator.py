#! /usr/bin/env python

import json
import sys

from utils import *
from framework.decorators import *


class MossTaskOrchestrator(object):

    '''
    Summary:
    Constructs a TaskOrchestrator object holding variables for executing a series of
    moss framework tasks in sequence.

    Arguments:
    task_order          list, list of functions to execute sequentially
    device              object, Netmiko SSH object from device_orchestrator

    Returns:
    dict
    '''

    def __init__(self, device=None, verbose=False):
        self.device = device
        self.verbose = verbose
        self.task = {"task_order": []}


    def add_task(self, task_name=None, argument=None, success_outcome='success', success_next_task=None, failure_next_task=None, log=True):
        '''
        Summary:
        Constructs a task for the overall TaskOrchestrator

        Arguments:
        task_name           string, name of the task to be executed e.g. get_system_uptime
        Arguments           string, argument for task that relies on parsing output
        success_outcome     string, success or fail, which outcome of the task is the expected outcome
        success_next_task   string, next task to be executed if there is an expected outcome (default: next task)
        failure_next_task   string, next task to be executed if there is an unexpected outcome
        print               bool, print the progress of the task
        '''

        task_data = {
            "task_name": task_name,
            "argument": argument,
            "success_outcome": success_outcome,
            "success_next_task": success_next_task,
            "failure_next_task": failure_next_task,
            "logging": log
        }

        self.task['task_order'].append(task_data)


    def dryrun():
        pass


    def run(self):
        connection = self.device.get_connection()

        start_banner('Task Start')
        start_header(self.task)

        result_dict = {'tasks': []}
        total_tasks_ran = 0
        overall_start_time = timer()

        for task in self.task['task_order']:
            task_start_time = timer()
            task_start_header(task['task_name'])
            try:
                result = globals()[task['task_name']]()
            except KeyError as e:
                print colour('Unable to find function "{}".'.format(task), 'red', bold=True)
                sys.exit()

            decorator = result(connection)

            if task['argument']:
                result = decorator(connection, task['argument'])
            else:
                result = decorator(connection)

            task_end_header(result['result'])
            task_end_time = timer()
            task_run_time = task_end_time - task_start_time
            total_tasks_ran += 1

            task_result_dict = {
                'task_namespace': result['namespace'],
                'task_id': result['task'],
                'result': result['result'],
                'stdout': result['stdout'],
                'start_time': task_start_time,
                'end_time': task_end_time,
                'run_time': task_run_time
            }

            if self.verbose:
                pretty_print(task_result_dict)

            result_dict['tasks'].append(task_result_dict)

        overall_end_time = timer()
        overall_run_time = overall_end_time - overall_start_time

        result_dict.update({
            'task_start_time':overall_start_time,
            'task_end_time': task_end_time,
            'task_run_time': overall_run_time,
            'tasks_ran': total_tasks_ran
        })

        task_failure = False

        for task in result_dict['tasks']:
            if task['result'] == 'fail':
                task_failure = True

        if task_failure:
            end_banner('fail')
        else:
            end_banner('success')

        return result_dict


    def show_steps(self):
        return self.task['task_order']
