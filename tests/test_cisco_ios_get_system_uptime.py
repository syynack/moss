#!/usr/bin/env python

import pytest
import re

from moss.framework.devops.get_system_uptime import cisco_ios_get_system_uptime

CLI_OUTPUT = '''
Cisco IOS Software, 3700 Software (C3745-ADVIPSERVICESK9-M), Version 12.4(25d), RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2010 by Cisco Systems, Inc.
Compiled Wed 18-Aug-10 08:18 by prod_rel_team

ROM: ROMMON Emulation Microcode
ROM: 3700 Software (C3745-ADVIPSERVICESK9-M), Version 12.4(25d), RELEASE SOFTWARE (fc1)

R1 uptime is 8 minutes
System returned to ROM by unknown reload cause - suspect boot_data[BOOT_COUNT] 0x0, BOOT_COUNT 0, BOOTDATA 19
System image file is "tftp://255.255.255.255/unknown"


This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

Cisco 3745 (R7000) processor (revision 2.0) with 249856K/12288K bytes of memory.
Processor board ID FTX0945W0MY
R7000 CPU at 350MHz, Implementation 39, Rev 2.1, 256KB L2, 512KB L3 Cache
18 FastEthernet interfaces
DRAM configuration is 64 bits wide with parity enabled.
151K bytes of NVRAM.

Configuration register is 0x2102
'''

def _run_cisco_ios_get_system_uptime():
    output = CLI_OUTPUT

    if output is None or '% Incomplete command.' in output:
        return {
            'result': 'fail',
            'stdout': output
        }

    stdout = {}
    regex = 'uptime\sis\s(?P<uptime>.+?)\sminutes'

    for line in output.splitlines():
        data = re.search(regex, line)
        if data is not None:
            data = data.groupdict()
            stdout.update(data)

    return {
        'result': 'success',
        'stdout': stdout
    }


@pytest.mark.parametrize('expected_result', [({'result': 'success', 'stdout': {'uptime': '8'}})])
def test_cisco_ios_get_system_uptime(expected_result):
    result = _run_cisco_ios_get_system_uptime()
    assert result == expected_result
