#! /usr/bin/env python

import sys
from netmiko import ConnectHandler

class MossDeviceOrchestrator(object):

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

    def __init__(self, device_type='', ip='', username='', password='', port=22, timeout=8, session_timeout=60):
        self.device_type = device_type
        self.ip = ip
        self.username = username
        self.password = password
        self.port = port
        self.timeout = timeout
        self.session_timeout = session_timeout


    def get_connection(self):
        try:
            return ConnectHandler(
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
        except:
            print 'Unable to connect to {} on port {}'.format(self.ip, self.port)
            sys.exit()
