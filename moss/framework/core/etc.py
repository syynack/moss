#!/usr/bin/env python

def diagnose_interfaces(stdout, offend_threshold=0):
    '''
    Summary:
    Written to work in tandem with get_interfaces_statistics devops script. Will inspect
    stdout and look for over zero or specified value in rx_drp, rx_err, tx_drp, tx_err.

    Arguments:
    stdout                  dict, output from get_interfaces_statistics
    offend_threshold        int, overwrite for 0 as the baseline for offenders to be determined

    Return:
    dict
    '''

    diagnose_elements = [
        'rx_drp',
        'rx_err',
        'tx_drp',
        'tx_err'
    ]

    diagnose_keys = {
        'rx_drp': 'recieve discards',
        'rx_err': 'recieve errors',
        'tx_drp': 'transmit discards',
        'tx_err': 'transmit errors'
    }

    result = {'interfaces': {}, 'offending_interfaces': []}
    stdout = stdout['stdout']

    if isinstance(stdout, dict):
        for interface in stdout:
            if isinstance(stdout[interface], dict):
                for element in diagnose_elements:
                    if int(stdout[interface][element]) > int(offend_threshold):
                        if interface not in result['offending_interfaces']:
                            result['offending_interfaces'].append(interface)

                        if not result['interfaces'].get(interface):
                            result['interfaces'][interface] = []

                        result['interfaces'][interface].append(element)

    if len(result['offending_interfaces']) > 0:
        result['result'] = 'fail'
    else:
        result['result'] = 'success'

    return result
