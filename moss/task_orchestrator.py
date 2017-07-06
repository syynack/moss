#! /usr/bin/env python

import json
import sys

from utils import *
from core import *


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


    def add_task(self, task_name=None, argument=None, success_outcome='success', final=False, failure_next_task=None, log=True):
        '''
        Summary:
        Constructs a task for the overall TaskOrchestrator

        Arguments:
        task_name           string, name of the task to be executed e.g. get_system_uptime
        argument            string, argument for task that relies on parsing output
        success_outcome     string, success or fail, which outcome of the task is the expected outcome
        final               bool, mark the task as the final task
        failure_next_task   string, next task to be executed if there is an unexpected outcome
        '''

        task_data = {
            "task_name": task_name,
            "argument": argument,
            "success_outcome": success_outcome,
            "final": final,
            "failure_next_task": failure_next_task,
            "logging": log
        }

        self.task['task_order'].append(task_data)


    def dryrun():
        pass


    def run(self):
        connection = self.device.get_connection()

        start_banner()
        start_header(self.task)

        task_order = update_task_list(self.task['task_order'])
        result_dict = {'tasks': []}
        start_time = timer()

        next_task = task_order[0]

        while next_task != 'end':
            result = run_task(connection, next_task)
            result_dict['tasks'].append(result)

            if next_task['final']:
                break

            next_task_name = result['next_task']

            if next_task_name != 'end':
                task_index = [index for index, task in enumerate(task_order) if next_task_name in task['task_name']]
                next_task = task_order[task_index[0]]
            else:
                next_task = next_task_name

        end_time = timer()
        run_time = runtime(start_time, end_time)

        result_dict.update({
            'start_time': start_time,
            'end_time': end_time,
            'run_time': run_time
        })

        end_banner(result_dict['tasks'][-1]['result'])
        return result_dict


    def show_steps(self):
        return self.task['task_order']
