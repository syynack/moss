# -*- coding: utf-8 -*-

# Linux operations

# System
from .linux_commands import linux_get_system_info
from .linux_commands import linux_get_system_uptime

# BGP
from .quagga_commands import quagga_get_bgp_memory_usage
from .quagga_commands import quagga_get_bgp_summary
from .quagga_commands import quagga_get_bgp_neighbors
from .quagga_commands import quagga_get_bgp_neighbor

# OSPFv3
from .quagga_commands import quagga_get_ipv6_ospf_interface
from .quagga_commands import quagga_get_ipv6_ospf_interfaces
from .quagga_commands import quagga_get_ipv6_ospf_neighbor_brief
from .quagga_commands import quagga_get_ipv6_ospf_neighbors_brief
from .quagga_commands import quagga_get_ipv6_ospf_neighbor_detail
from .quagga_commands import quagga_get_ipv6_ospf_neighbors_detail

# RIB
from .quagga_commands import quagga_get_ipv6_route_table

# NDP
from .linux_commands import linux_get_ndp_table
from .linux_commands import linux_get_ndp_table_stale_entries
from .linux_commands import linux_get_ndp_table_reachable_entries

# MAC
from .linux_commands import linux_get_interfaces_mac_address

# LLDP
from .linux_commands import linux_get_lldp_neighbors
from .linux_commands import linux_get_lldp_interface

# IPv6
from .linux_commands import linux_get_ipv6_addresses

# Interfaces
from .linux_commands import linux_get_interfaces_statistics
from .linux_commands import linux_get_interface_statistics
from .quagga_commands import quagga_get_interfaces_description
from .quagga_commands import quagga_get_interface_description
