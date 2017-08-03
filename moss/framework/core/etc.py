#!/usr/bin/env python

def diagnose_interfaces(stdout, offend_threshold=None):
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

    results = {}

    if isinstance(stdout, dict):
        for interface in stdout:
            if isinstance(interface, dict):
                for key in diagnose_elements:
                    interfaces_statistics = None

                    try:
                        interfaces_statistics = stdout[interface][key]
                    except:
                        pass

                    if interfaces_statistics is not None:
                        results[interface] = {'increasing': []}
                        if offend_threshold is not None:
                            if int(interfaces_statistics) > int(offend_threshold):
                                results[interface]['increasing'].append(diagnose_keys[key])
                        else:
                            if int(interfaces_statistics) > 0:
                                results[interface]['increasing'].append(diagnose_keys[key])

    for interface in result:
        if result[interface]['increasing'] > 0:
            results['offending_interfaces'] = True

    return results
