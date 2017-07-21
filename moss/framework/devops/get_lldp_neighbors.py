#!/usr/bin/env python

import re
from moss.framework.decorators import register

@register(platform = 'linux')
def linux_get_lldp_neighbors(connection):
    '''
    Utilises the Linux implementation of IEEE 802.1ab (LLDP) protocol to
    return link layer discovery information in an XML format.

    Example expected output of lldpctl -f xml:

    <?xml version="1.0" encoding="UTF-8"?>
    <lldp label="LLDP neighbors">
     <interface label="Interface" name="eth1" via="LLDP" rid="2" age="0 day, 00:00:34">
      <chassis label="Chassis">
       <id label="ChassisID" type="mac">16:cf:13:22:ce:a9</id>
       <name label="SysName">d1-p1-l2-r1</name>
       <descr label="SysDescr">Debian GNU/Linux 8 (jessie) Linux 4.4.0-31-generic #50~14.04.1-Ubuntu SMP Wed Jul 13 01:07:32 UTC 2016 x86_64</descr>
       <capability label="Capability" type="Bridge" enabled="off"/>
       <capability label="Capability" type="Router" enabled="on"/>
       <capability label="Capability" type="Wlan" enabled="off"/>
       <capability label="Capability" type="Station" enabled="on"/>
      </chassis>
      <port label="Port">
       <id label="PortID" type="mac">2a:d0:1a:0a:91:66</id>
       <descr label="PortDescr">eth1</descr>
      </port>
     </interface>
    </lldp>

    Arguments:
    connection:         object, MossDeviceOrchestrator object

    Returns:
    dict

    Depends:
    lldpd

    Example:
    "stdout": {
        "eth1": {
            "remote_chassis_ll_addr": "16:cf:13:22:ce:a9",
            "remote_hostname": "d1-p1-l2-r1",
            "remote_port_ll_addr": "2a:d0:1a:0a:91:66",
            "remote_port_id": "eth1"
        }
    }
    '''

    command = 'lldpctl -f xml'
    output = connection.send_command(command)

    if output is None or 'command not found' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    regexes = ['id\slabel.*"mac">(?P<remote_chassis_ll_addr>[^<]+)',
        'name\slabel.*"SysName">(?P<remote_hostname>[^<]+)',
        'id\slabel="PortID".*"mac">(?P<remote_port_ll_addr>[^<]+)',
        'descr\slabel="PortDescr">(?P<remote_port_id>[^<]+)'
    ]

    for line in output.splitlines():
        if 'interface label' in line:
            port_id = str(line.split()[2].split('=')[1].replace('"', ''))
            stdout[port_id] = {}

        for regex in regexes:
            match = re.search(regex, line)

            if match:
                stdout[port_id].update(match.groupdict())

    return {
        'result': 'success',
        'stdout': stdout
    }
