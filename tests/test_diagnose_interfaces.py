#!/usr/bin/env python

import pytest

from moss.framework.core.etc import diagnose_interfaces

@pytest.mark.parametrize('stdout,expected_result,offend_threshold', [
    ({
        "stdout": {
            "eth0": {
                "collisions": "0",
                "link_encapsulation": "Ethernet",
                "mtu": "1480",
                "rx_bytes": "0",
                "rx_drp": "1000",
                "rx_err": "1000",
                "rx_frm": "0",
                "rx_ok": "0",
                "rx_ovr": "0",
                "rx_total": "0.0 B",
                "tx_bytes": "0",
                "tx_car": "0",
                "tx_drp": "1000",
                "tx_err": "1000",
                "tx_ok": "0",
                "tx_ovr": "0",
                "tx_queue_length": "1",
                "tx_total": "0.0 B"
                }
            }
        },
    {'interfaces': {'eth0': ['rx_drp', 'rx_err', 'tx_drp', 'tx_err']}, 'offending_interfaces': ['eth0'], 'result': 'fail'},
    0
    ),
    ({
        "stdout": {
            "eth0": {
                "collisions": "0",
                "link_encapsulation": "Ethernet",
                "mtu": "1480",
                "rx_bytes": "0",
                "rx_drp": "0",
                "rx_err": "0",
                "rx_frm": "0",
                "rx_ok": "0",
                "rx_ovr": "0",
                "rx_total": "0.0 B",
                "tx_bytes": "0",
                "tx_car": "0",
                "tx_drp": "0",
                "tx_err": "0",
                "tx_ok": "0",
                "tx_ovr": "0",
                "tx_queue_length": "1",
                "tx_total": "0.0 B"
                }
            }
        },
    {'interfaces': {}, 'offending_interfaces': [], 'result': 'success'},
    0
    ),
])
def test_diagnose_interfaces(stdout, expected_result, offend_threshold):
    result = diagnose_interfaces(stdout, offend_threshold)
    assert result == expected_result
