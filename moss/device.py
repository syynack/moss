#! /usr/bin/env python

import sys

from utils import colour
from netmiko import ConnectHandler

class Device(object):

    '''
    Summary:
    Returns netmiko SSH connection to device using variables as defined
    Paramater defaults set as per http://netmiko.readthedocs.io/en/latest/classes/base_connection.html

    Takes:
    device_type:        string, running OS on the device e.g. linux, cisco_ios, juniper
    ip:                 string, IPv4/v6 address of target device
    username:           string, username to authenticate against
    password:           string, password to authenticate with
    port:               int, port to connect to
    timeout:            int, global connection timeout
    session_timeout:    int, timeout for parallel requests

    Returns:
    MossDeviceOrchestrator object

    '''

    def __init__(self, device_type='', ip='', username='', password='', port=22, timeout=20, session_timeout=60):
        self.device_type = device_type
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.session_timeout = session_timeout


    def get_connection(self):
        try:
            connection = ConnectHandler(
                device_type = self.device_type,
                ip = self.ip,
                username = self.username,
                password = self.password,
                port = self.port,
                timeout = self.timeout,
                session_timeout = self.session_timeout
            )
        except ValueError as e:
            print '\n{} is not a currently supported device. Currently supported devices are: \n{}' \
                .format(self.device_type, ', '.join(str(e).split()[6:]))
            sys.exit()

        return connection


    def close(self, connection):
        if connection.username == 'root' and connection.device_type == 'linux':
            # Disconnecting from a Linux box with user root is currently not supported, see https://github.com/ktbyers/netmiko/issues/492
            # if the issue is closed, matt was lazy. Please update this.
            return

        try:
            connection.disconnect()
        except:
            raise
