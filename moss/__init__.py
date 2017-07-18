#! /usr/bin/env python

import modules

from .register import REGISTER

__all__ = [
    REGISTER
]

from .device import Device

# BGP
from .decorators import get_bgp_memory_usage, get_bgp_neighbor, get_bgp_neighbors, get_bgp_summary

# Interfaces
from .decorators import get_interface_description, get_interfaces_description, get_interface_statistics, \
                        get_interfaces_statistics

# IPv6
from .decorators import get_ipv6_addresses

# LLDP
from .decorators import get_lldp_interface, get_lldp_neighbors

# MAC
from .decorators import get_interfaces_mac_address

# NDP
from .decorators import get_ndp_table_reachable_entries, get_ndp_table_stale_entries, get_ndp_table

# OSPFv3
from .decorators import get_ipv6_ospf_interface, get_ipv6_ospf_interfaces, get_ipv6_ospf_neighbor_brief, \
                        get_ipv6_ospf_neighbor_detail, get_ipv6_ospf_neighbors_brief, get_ipv6_ospf_neighbors_detail

# RIB
from .decorators import get_ipv6_route_table

# System
from .decorators import get_system_info, get_system_uptime
