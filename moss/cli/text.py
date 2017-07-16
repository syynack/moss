
ENDPOINTS_BASE_TEXT = '''# This file is used to define endpoint information to be used when executing
# tasks. This information is what shall be used when attempting to connect
# to the target endpoints.


# Authentication
# Define a global password to be used for all device connections
global_password: ''

# Define a global username to be used for all device connections
global_username: ''


# Endpoints
# Define a global os if all the endpoints run the same operating system
global_os: ''

# Define endpoint information
endpoints:

# Example
- os: 'linux'
  ip: '192.168.0.1'

- os: 'cisco_ios'
  ip: '192.168.0.2'
'''

TASK_BASE_TEXT = '''# This file is used to define task stages to be executed within the task.
# Here you will be able to define:
#   - module                The name of the task module to be executed in this stage
#                           (all task modules can be viewed by doing cli.py list-modules).
#
#   - argument              To be used when the task module requires an argument, for
#                           example get_bgp_neighbor requires to neighbor_ip argument.
#
#   - success_outcome       Define either 'success' or 'failure' as the success_outcome, the
#                           default option is 'success'.
#
#   - failure_next_module   Define when you wish the stage to branch to another stage if
#                           an outcome not matching the success_outcome is returned.
#
#   - focus                 Define an element of stdout from the module to focus on.
#                           For example:
#
#                           focus:
#                               neighbor_rid: 'fd35:1:1:2::8'
#
#                           will check if there is an occurrence of fd35:1:1:2::8 in stdout,
#                           if there is a match focus_outcome will be marked as True.
#
#   - focus_next_module     Module to branch to if focus matches
#
#   - final                 Used to mark the task stage as a final stage. Can be used more
#                           than once.


# Task
task:

# First stage example
- module: 'get_interfaces_descriptions'
  focus:
    admin_status: 'down'
  focus_outcome: 'fail'

# Add more stages
'''
