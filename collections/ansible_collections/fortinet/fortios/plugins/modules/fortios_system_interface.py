#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_system_interface
short_description: Configure interfaces in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify system feature and interface category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.4.0
version_added: "2.8"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Hongbin Lu (@fgtdev-hblu)
    - Frank Shen (@frankshen01)
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

requirements:
    - ansible>=2.9.0
options:
    access_token:
        description:
            - Token-based authentication.
              Generated from GUI of Fortigate.
        type: str
        required: false
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root

    state:
        description:
            - Indicates whether to create or remove the object.
              This attribute was present already in previous version in a deeper level.
              It has been moved out to this outer level.
        type: str
        required: false
        choices:
            - present
            - absent
        version_added: 2.9
    system_interface:
        description:
            - Configure interfaces.
        default: null
        type: dict
        suboptions:
            state:
                description:
                    - B(Deprecated)
                    - Starting with Ansible 2.9 we recommend using the top-level 'state' parameter.
                    - HORIZONTALLINE
                    - Indicates whether to create or remove the object.
                type: str
                required: false
                choices:
                    - present
                    - absent
            ac_name:
                description:
                    - PPPoE server name.
                type: str
            aggregate:
                description:
                    - Aggregate interface.
                type: str
            algorithm:
                description:
                    - Frame distribution algorithm.
                type: str
                choices:
                    - L2
                    - L3
                    - L4
            alias:
                description:
                    - Alias will be displayed with the interface name to make it easier to distinguish.
                type: str
            allowaccess:
                description:
                    - Permitted types of management access to this interface.
                type: list
                choices:
                    - ping
                    - https
                    - ssh
                    - snmp
                    - http
                    - telnet
                    - fgfm
                    - radius-acct
                    - probe-response
                    - fabric
                    - ftm
            ap_discover:
                description:
                    - Enable/disable automatic registration of unknown FortiAP devices.
                type: str
                choices:
                    - enable
                    - disable
            arpforward:
                description:
                    - Enable/disable ARP forwarding.
                type: str
                choices:
                    - enable
                    - disable
            auth_type:
                description:
                    - PPP authentication type to use.
                type: str
                choices:
                    - auto
                    - pap
                    - chap
                    - mschapv1
                    - mschapv2
            auto_auth_extension_device:
                description:
                    - Enable/disable automatic authorization of dedicated Fortinet extension device on this interface.
                type: str
                choices:
                    - enable
                    - disable
            bandwidth_measure_time:
                description:
                    - Bandwidth measure time
                type: int
            bfd:
                description:
                    - Bidirectional Forwarding Detection (BFD) settings.
                type: str
                choices:
                    - global
                    - enable
                    - disable
            bfd_desired_min_tx:
                description:
                    - BFD desired minimal transmit interval.
                type: int
            bfd_detect_mult:
                description:
                    - BFD detection multiplier.
                type: int
            bfd_required_min_rx:
                description:
                    - BFD required minimal receive interval.
                type: int
            broadcast_forward:
                description:
                    - Enable/disable broadcast forwarding.
                type: str
                choices:
                    - enable
                    - disable
            cli_conn_status:
                description:
                    - CLI connection status.
                type: int
            client_options:
                description:
                    - DHCP client options.
                type: list
                suboptions:
                    code:
                        description:
                            - DHCP client option code.
                        type: int
                    id:
                        description:
                            - ID.
                        required: true
                        type: int
                    ip:
                        description:
                            - DHCP option IPs.
                        type: str
                    type:
                        description:
                            - DHCP client option type.
                        type: str
                        choices:
                            - hex
                            - string
                            - ip
                            - fqdn
                    value:
                        description:
                            - DHCP client option value.
                        type: str
            color:
                description:
                    - Color of icon on the GUI.
                type: int
            dedicated_to:
                description:
                    - Configure interface for single purpose.
                type: str
                choices:
                    - none
                    - management
            defaultgw:
                description:
                    - Enable to get the gateway IP from the DHCP or PPPoE server.
                type: str
                choices:
                    - enable
                    - disable
            description:
                description:
                    - Description.
                type: str
            detected_peer_mtu:
                description:
                    - MTU of detected peer (0 - 4294967295).
                type: int
            detectprotocol:
                description:
                    - Protocols used to detect the server.
                type: str
                choices:
                    - ping
                    - tcp-echo
                    - udp-echo
            detectserver:
                description:
                    - Gateway"s ping server for this IP.
                type: str
            device_identification:
                description:
                    - Enable/disable passively gathering of device identity information about the devices on the network connected to this interface.
                type: str
                choices:
                    - enable
                    - disable
            device_user_identification:
                description:
                    - Enable/disable passive gathering of user identity information about users on this interface.
                type: str
                choices:
                    - enable
                    - disable
            devindex:
                description:
                    - Device Index.
                type: int
            dhcp_client_identifier:
                description:
                    - DHCP client identifier.
                type: str
            dhcp_relay_agent_option:
                description:
                    - Enable/disable DHCP relay agent option.
                type: str
                choices:
                    - enable
                    - disable
            dhcp_relay_ip:
                description:
                    - DHCP relay IP address.
                type: str
            dhcp_relay_service:
                description:
                    - Enable/disable allowing this interface to act as a DHCP relay.
                type: str
                choices:
                    - disable
                    - enable
            dhcp_relay_type:
                description:
                    - DHCP relay type (regular or IPsec).
                type: str
                choices:
                    - regular
                    - ipsec
            dhcp_renew_time:
                description:
                    - DHCP renew time in seconds (300-604800), 0 means use the renew time provided by the server.
                type: int
            disc_retry_timeout:
                description:
                    - Time in seconds to wait before retrying to start a PPPoE discovery, 0 means no timeout.
                type: int
            disconnect_threshold:
                description:
                    - Time in milliseconds to wait before sending a notification that this interface is down or disconnected.
                type: int
            distance:
                description:
                    - Distance for routes learned through PPPoE or DHCP, lower distance indicates preferred route.
                type: int
            dns_server_override:
                description:
                    - Enable/disable use DNS acquired by DHCP or PPPoE.
                type: str
                choices:
                    - enable
                    - disable
            drop_fragment:
                description:
                    - Enable/disable drop fragment packets.
                type: str
                choices:
                    - enable
                    - disable
            drop_overlapped_fragment:
                description:
                    - Enable/disable drop overlapped fragment packets.
                type: str
                choices:
                    - enable
                    - disable
            egress_shaping_profile:
                description:
                    - Outgoing traffic shaping profile. Source firewall.shaping-profile.profile-name.
                type: str
            estimated_downstream_bandwidth:
                description:
                    - Estimated maximum downstream bandwidth (kbps). Used to estimate link utilization.
                type: int
            estimated_upstream_bandwidth:
                description:
                    - Estimated maximum upstream bandwidth (kbps). Used to estimate link utilization.
                type: int
            explicit_ftp_proxy:
                description:
                    - Enable/disable the explicit FTP proxy on this interface.
                type: str
                choices:
                    - enable
                    - disable
            explicit_web_proxy:
                description:
                    - Enable/disable the explicit web proxy on this interface.
                type: str
                choices:
                    - enable
                    - disable
            external:
                description:
                    - Enable/disable identifying the interface as an external interface (which usually means it"s connected to the Internet).
                type: str
                choices:
                    - enable
                    - disable
            fail_action_on_extender:
                description:
                    - Action on extender when interface fail .
                type: str
                choices:
                    - soft-restart
                    - hard-restart
                    - reboot
            fail_alert_interfaces:
                description:
                    - Names of the FortiGate interfaces to which the link failure alert is sent.
                type: list
                suboptions:
                    name:
                        description:
                            - Names of the non-virtual interface. Source system.interface.name.
                        required: true
                        type: str
            fail_alert_method:
                description:
                    - Select link-failed-signal or link-down method to alert about a failed link.
                type: str
                choices:
                    - link-failed-signal
                    - link-down
            fail_detect:
                description:
                    - Enable/disable fail detection features for this interface.
                type: str
                choices:
                    - enable
                    - disable
            fail_detect_option:
                description:
                    - Options for detecting that this interface has failed.
                type: str
                choices:
                    - detectserver
                    - link-down
            fortilink:
                description:
                    - Enable FortiLink to dedicate this interface to manage other Fortinet devices.
                type: str
                choices:
                    - enable
                    - disable
            fortilink_backup_link:
                description:
                    - fortilink split interface backup link.
                type: int
            fortilink_neighbor_detect:
                description:
                    - Protocol for FortiGate neighbor discovery.
                type: str
                choices:
                    - lldp
                    - fortilink
            fortilink_split_interface:
                description:
                    - Enable/disable FortiLink split interface to connect member link to different FortiSwitch in stack for uplink redundancy.
                type: str
                choices:
                    - enable
                    - disable
            fortilink_stacking:
                description:
                    - Enable/disable FortiLink switch-stacking on this interface.
                type: str
                choices:
                    - enable
                    - disable
            forward_domain:
                description:
                    - Transparent mode forward domain.
                type: int
            gwdetect:
                description:
                    - Enable/disable detect gateway alive for first.
                type: str
                choices:
                    - enable
                    - disable
            ha_priority:
                description:
                    - HA election priority for the PING server.
                type: int
            icmp_accept_redirect:
                description:
                    - Enable/disable ICMP accept redirect.
                type: str
                choices:
                    - enable
                    - disable
            icmp_send_redirect:
                description:
                    - Enable/disable ICMP send redirect.
                type: str
                choices:
                    - enable
                    - disable
            ident_accept:
                description:
                    - Enable/disable authentication for this interface.
                type: str
                choices:
                    - enable
                    - disable
            idle_timeout:
                description:
                    - PPPoE auto disconnect after idle timeout seconds, 0 means no timeout.
                type: int
            inbandwidth:
                description:
                    - Bandwidth limit for incoming traffic (0 - 16776000 kbps), 0 means unlimited.
                type: int
            ingress_shaping_profile:
                description:
                    - Incoming traffic shaping profile. Source firewall.shaping-profile.profile-name.
                type: str
            ingress_spillover_threshold:
                description:
                    - Ingress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.
                type: int
            interface:
                description:
                    - Interface name. Source system.interface.name.
                type: str
            internal:
                description:
                    - Implicitly created.
                type: int
            ip:
                description:
                    - 'Interface IPv4 address and subnet mask, syntax: X.X.X.X/24.'
                type: str
            ip_managed_by_fortiipam:
                description:
                    - Enable/disable automatic IP address assignment of this interface by FortiIPAM.
                type: str
                choices:
                    - enable
                    - disable
            ipmac:
                description:
                    - Enable/disable IP/MAC binding.
                type: str
                choices:
                    - enable
                    - disable
            ips_sniffer_mode:
                description:
                    - Enable/disable the use of this interface as a one-armed sniffer.
                type: str
                choices:
                    - enable
                    - disable
            ipunnumbered:
                description:
                    - Unnumbered IP used for PPPoE interfaces for which no unique local address is provided.
                type: str
            ipv6:
                description:
                    - IPv6 of interface.
                type: dict
                suboptions:
                    autoconf:
                        description:
                            - Enable/disable address auto config.
                        type: str
                        choices:
                            - enable
                            - disable
                    dhcp6_client_options:
                        description:
                            - DHCPv6 client options.
                        type: str
                        choices:
                            - rapid
                            - iapd
                            - iana
                    dhcp6_information_request:
                        description:
                            - Enable/disable DHCPv6 information request.
                        type: str
                        choices:
                            - enable
                            - disable
                    dhcp6_prefix_delegation:
                        description:
                            - Enable/disable DHCPv6 prefix delegation.
                        type: str
                        choices:
                            - enable
                            - disable
                    dhcp6_prefix_hint:
                        description:
                            - DHCPv6 prefix that will be used as a hint to the upstream DHCPv6 server.
                        type: str
                    dhcp6_prefix_hint_plt:
                        description:
                            - DHCPv6 prefix hint preferred life time (sec), 0 means unlimited lease time.
                        type: int
                    dhcp6_prefix_hint_vlt:
                        description:
                            - DHCPv6 prefix hint valid life time (sec).
                        type: int
                    dhcp6_relay_ip:
                        description:
                            - DHCPv6 relay IP address.
                        type: str
                    dhcp6_relay_service:
                        description:
                            - Enable/disable DHCPv6 relay.
                        type: str
                        choices:
                            - disable
                            - enable
                    dhcp6_relay_type:
                        description:
                            - DHCPv6 relay type.
                        type: str
                        choices:
                            - regular
                    ip6_address:
                        description:
                            - 'Primary IPv6 address prefix, syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx'
                        type: str
                    ip6_allowaccess:
                        description:
                            - Allow management access to the interface.
                        type: list
                        choices:
                            - ping
                            - https
                            - ssh
                            - snmp
                            - http
                            - telnet
                            - fgfm
                            - fabric
                    ip6_default_life:
                        description:
                            - Default life (sec).
                        type: int
                    ip6_delegated_prefix_list:
                        description:
                            - Advertised IPv6 delegated prefix list.
                        type: list
                        suboptions:
                            autonomous_flag:
                                description:
                                    - Enable/disable the autonomous flag.
                                type: str
                                choices:
                                    - enable
                                    - disable
                            onlink_flag:
                                description:
                                    - Enable/disable the onlink flag.
                                type: str
                                choices:
                                    - enable
                                    - disable
                            prefix_id:
                                description:
                                    - Prefix ID.
                                type: int
                            rdnss:
                                description:
                                    - Recursive DNS server option.
                                type: str
                            rdnss_service:
                                description:
                                    - Recursive DNS service option.
                                type: str
                                choices:
                                    - delegated
                                    - default
                                    - specify
                            subnet:
                                description:
                                    -  Add subnet ID to routing prefix.
                                type: str
                            upstream_interface:
                                description:
                                    - Name of the interface that provides delegated information. Source system.interface.name.
                                type: str
                    ip6_dns_server_override:
                        description:
                            - Enable/disable using the DNS server acquired by DHCP.
                        type: str
                        choices:
                            - enable
                            - disable
                    ip6_extra_addr:
                        description:
                            - Extra IPv6 address prefixes of interface.
                        type: list
                        suboptions:
                            prefix:
                                description:
                                    - IPv6 address prefix.
                                required: true
                                type: str
                    ip6_hop_limit:
                        description:
                            - Hop limit (0 means unspecified).
                        type: int
                    ip6_link_mtu:
                        description:
                            - IPv6 link MTU.
                        type: int
                    ip6_manage_flag:
                        description:
                            - Enable/disable the managed flag.
                        type: str
                        choices:
                            - enable
                            - disable
                    ip6_max_interval:
                        description:
                            - IPv6 maximum interval (4 to 1800 sec).
                        type: int
                    ip6_min_interval:
                        description:
                            - IPv6 minimum interval (3 to 1350 sec).
                        type: int
                    ip6_mode:
                        description:
                            - Addressing mode (static, DHCP, delegated).
                        type: str
                        choices:
                            - static
                            - dhcp
                            - pppoe
                            - delegated
                    ip6_other_flag:
                        description:
                            - Enable/disable the other IPv6 flag.
                        type: str
                        choices:
                            - enable
                            - disable
                    ip6_prefix_list:
                        description:
                            - Advertised prefix list.
                        type: list
                        suboptions:
                            autonomous_flag:
                                description:
                                    - Enable/disable the autonomous flag.
                                type: str
                                choices:
                                    - enable
                                    - disable
                            dnssl:
                                description:
                                    - DNS search list option.
                                type: list
                                suboptions:
                                    domain:
                                        description:
                                            - Domain name.
                                        required: true
                                        type: str
                            onlink_flag:
                                description:
                                    - Enable/disable the onlink flag.
                                type: str
                                choices:
                                    - enable
                                    - disable
                            preferred_life_time:
                                description:
                                    - Preferred life time (sec).
                                type: int
                            prefix:
                                description:
                                    - IPv6 prefix.
                                required: true
                                type: str
                            rdnss:
                                description:
                                    - Recursive DNS server option.
                                type: str
                            valid_life_time:
                                description:
                                    - Valid life time (sec).
                                type: int
                    ip6_reachable_time:
                        description:
                            - IPv6 reachable time (milliseconds; 0 means unspecified).
                        type: int
                    ip6_retrans_time:
                        description:
                            - IPv6 retransmit time (milliseconds; 0 means unspecified).
                        type: int
                    ip6_send_adv:
                        description:
                            - Enable/disable sending advertisements about the interface.
                        type: str
                        choices:
                            - enable
                            - disable
                    ip6_subnet:
                        description:
                            - ' Subnet to routing prefix, syntax: xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx:xxxx/xxx'
                        type: str
                    ip6_upstream_interface:
                        description:
                            - Interface name providing delegated information. Source system.interface.name.
                        type: str
                    nd_cert:
                        description:
                            - Neighbor discovery certificate. Source certificate.local.name.
                        type: str
                    nd_cga_modifier:
                        description:
                            - Neighbor discovery CGA modifier.
                        type: str
                    nd_mode:
                        description:
                            - Neighbor discovery mode.
                        type: str
                        choices:
                            - basic
                            - SEND-compatible
                    nd_security_level:
                        description:
                            - Neighbor discovery security level (0 - 7; 0 = least secure).
                        type: int
                    nd_timestamp_delta:
                        description:
                            - Neighbor discovery timestamp delta value (1 - 3600 sec; ).
                        type: int
                    nd_timestamp_fuzz:
                        description:
                            - Neighbor discovery timestamp fuzz factor (1 - 60 sec; ).
                        type: int
                    vrip6_link_local:
                        description:
                            - Link-local IPv6 address of virtual router.
                        type: str
                    vrrp_virtual_mac6:
                        description:
                            - Enable/disable virtual MAC for VRRP.
                        type: str
                        choices:
                            - enable
                            - disable
                    vrrp6:
                        description:
                            - IPv6 VRRP configuration.
                        type: list
                        suboptions:
                            accept_mode:
                                description:
                                    - Enable/disable accept mode.
                                type: str
                                choices:
                                    - enable
                                    - disable
                            adv_interval:
                                description:
                                    - Advertisement interval (1 - 255 seconds).
                                type: int
                            preempt:
                                description:
                                    - Enable/disable preempt mode.
                                type: str
                                choices:
                                    - enable
                                    - disable
                            priority:
                                description:
                                    - Priority of the virtual router (1 - 255).
                                type: int
                            start_time:
                                description:
                                    - Startup time (1 - 255 seconds).
                                type: int
                            status:
                                description:
                                    - Enable/disable VRRP.
                                type: str
                                choices:
                                    - enable
                                    - disable
                            vrdst6:
                                description:
                                    - Monitor the route to this destination.
                                type: str
                            vrgrp:
                                description:
                                    - VRRP group ID (1 - 65535).
                                type: int
                            vrid:
                                description:
                                    - Virtual router identifier (1 - 255).
                                required: true
                                type: int
                            vrip6:
                                description:
                                    - IPv6 address of the virtual router.
                                type: str
            l2forward:
                description:
                    - Enable/disable l2 forwarding.
                type: str
                choices:
                    - enable
                    - disable
            lacp_ha_slave:
                description:
                    - LACP HA slave.
                type: str
                choices:
                    - enable
                    - disable
            lacp_mode:
                description:
                    - LACP mode.
                type: str
                choices:
                    - static
                    - passive
                    - active
            lacp_speed:
                description:
                    - How often the interface sends LACP messages.
                type: str
                choices:
                    - slow
                    - fast
            lcp_echo_interval:
                description:
                    - Time in seconds between PPPoE Link Control Protocol (LCP) echo requests.
                type: int
            lcp_max_echo_fails:
                description:
                    - Maximum missed LCP echo messages before disconnect.
                type: int
            link_up_delay:
                description:
                    - Number of milliseconds to wait before considering a link is up.
                type: int
            lldp_network_policy:
                description:
                    - LLDP-MED network policy profile. Source system.lldp.network-policy.name.
                type: str
            lldp_reception:
                description:
                    - Enable/disable Link Layer Discovery Protocol (LLDP) reception.
                type: str
                choices:
                    - enable
                    - disable
                    - vdom
            lldp_transmission:
                description:
                    - Enable/disable Link Layer Discovery Protocol (LLDP) transmission.
                type: str
                choices:
                    - enable
                    - disable
                    - vdom
            macaddr:
                description:
                    - Change the interface"s MAC address.
                type: str
            managed_subnetwork_size:
                description:
                    - Number of IP addresses to be allocated by FortiIPAM and used by this FortiGate unit"s DHCP server settings.
                type: str
                choices:
                    - 256
                    - 512
                    - 1024
                    - 2048
                    - 4096
                    - 8192
                    - 16384
                    - 32768
                    - 65536
            management_ip:
                description:
                    - High Availability in-band management IP address of this interface.
                type: str
            measured_downstream_bandwidth:
                description:
                    - Measured downstream bandwidth (kbps).
                type: int
            measured_upstream_bandwidth:
                description:
                    - Measured upstream bandwidth (kbps).
                type: int
            member:
                description:
                    - Physical interfaces that belong to the aggregate or redundant interface.
                type: list
                suboptions:
                    interface_name:
                        description:
                            - Physical interface name. Source system.interface.name.
                        type: str
            min_links:
                description:
                    - Minimum number of aggregated ports that must be up.
                type: int
            min_links_down:
                description:
                    - Action to take when less than the configured minimum number of links are active.
                type: str
                choices:
                    - operational
                    - administrative
            mode:
                description:
                    - Addressing mode (static, DHCP, PPPoE).
                type: str
                choices:
                    - static
                    - dhcp
                    - pppoe
            monitor_bandwidth:
                description:
                    - Enable monitoring bandwidth on this interface.
                type: str
                choices:
                    - enable
                    - disable
            mtu:
                description:
                    - MTU value for this interface.
                type: int
            mtu_override:
                description:
                    - Enable to set a custom MTU for this interface.
                type: str
                choices:
                    - enable
                    - disable
            name:
                description:
                    - Name.
                required: true
                type: str
            ndiscforward:
                description:
                    - Enable/disable NDISC forwarding.
                type: str
                choices:
                    - enable
                    - disable
            netbios_forward:
                description:
                    - Enable/disable NETBIOS forwarding.
                type: str
                choices:
                    - disable
                    - enable
            netflow_sampler:
                description:
                    - Enable/disable NetFlow on this interface and set the data that NetFlow collects (rx, tx, or both).
                type: str
                choices:
                    - disable
                    - tx
                    - rx
                    - both
            outbandwidth:
                description:
                    - Bandwidth limit for outgoing traffic (0 - 16776000 kbps), 0 means unlimited.
                type: int
            padt_retry_timeout:
                description:
                    - PPPoE Active Discovery Terminate (PADT) used to terminate sessions after an idle time.
                type: int
            password:
                description:
                    - PPPoE account"s password.
                type: str
            ping_serv_status:
                description:
                    - PING server status.
                type: int
            polling_interval:
                description:
                    - sFlow polling interval (1 - 255 sec).
                type: int
            pppoe_unnumbered_negotiate:
                description:
                    - Enable/disable PPPoE unnumbered negotiation.
                type: str
                choices:
                    - enable
                    - disable
            pptp_auth_type:
                description:
                    - PPTP authentication type.
                type: str
                choices:
                    - auto
                    - pap
                    - chap
                    - mschapv1
                    - mschapv2
            pptp_client:
                description:
                    - Enable/disable PPTP client.
                type: str
                choices:
                    - enable
                    - disable
            pptp_password:
                description:
                    - PPTP password.
                type: str
            pptp_server_ip:
                description:
                    - PPTP server IP address.
                type: str
            pptp_timeout:
                description:
                    - Idle timer in minutes (0 for disabled).
                type: int
            pptp_user:
                description:
                    - PPTP user name.
                type: str
            preserve_session_route:
                description:
                    - Enable/disable preservation of session route when dirty.
                type: str
                choices:
                    - enable
                    - disable
            priority:
                description:
                    - Priority of learned routes.
                type: int
            priority_override:
                description:
                    - Enable/disable fail back to higher priority port once recovered.
                type: str
                choices:
                    - enable
                    - disable
            proxy_captive_portal:
                description:
                    - Enable/disable proxy captive portal on this interface.
                type: str
                choices:
                    - enable
                    - disable
            redundant_interface:
                description:
                    - Redundant interface.
                type: str
            remote_ip:
                description:
                    - Remote IP address of tunnel.
                type: str
            replacemsg_override_group:
                description:
                    - Replacement message override group.
                type: str
            ring_rx:
                description:
                    - RX ring size.
                type: int
            ring_tx:
                description:
                    - TX ring size.
                type: int
            role:
                description:
                    - Interface role.
                type: str
                choices:
                    - lan
                    - wan
                    - dmz
                    - undefined
            sample_direction:
                description:
                    - Data that NetFlow collects (rx, tx, or both).
                type: str
                choices:
                    - tx
                    - rx
                    - both
            sample_rate:
                description:
                    - sFlow sample rate (10 - 99999).
                type: int
            secondary_IP:
                description:
                    - Enable/disable adding a secondary IP to this interface.
                type: str
                choices:
                    - enable
                    - disable
            secondaryip:
                description:
                    - Second IP address of interface.
                type: list
                suboptions:
                    allowaccess:
                        description:
                            - Management access settings for the secondary IP address.
                        type: str
                        choices:
                            - ping
                            - https
                            - ssh
                            - snmp
                            - http
                            - telnet
                            - fgfm
                            - radius-acct
                            - probe-response
                            - fabric
                            - ftm
                    detectprotocol:
                        description:
                            - Protocols used to detect the server.
                        type: str
                        choices:
                            - ping
                            - tcp-echo
                            - udp-echo
                    detectserver:
                        description:
                            - Gateway"s ping server for this IP.
                        type: str
                    gwdetect:
                        description:
                            - Enable/disable detect gateway alive for first.
                        type: str
                        choices:
                            - enable
                            - disable
                    ha_priority:
                        description:
                            - HA election priority for the PING server.
                        type: int
                    id:
                        description:
                            - ID.
                        required: true
                        type: int
                    ip:
                        description:
                            - Secondary IP address of the interface.
                        type: str
                    ping_serv_status:
                        description:
                            - PING server status.
                        type: int
            security_exempt_list:
                description:
                    - Name of security-exempt-list.
                type: str
            security_external_logout:
                description:
                    - URL of external authentication logout server.
                type: str
            security_external_web:
                description:
                    - URL of external authentication web server.
                type: str
            security_groups:
                description:
                    - User groups that can authenticate with the captive portal.
                type: list
                suboptions:
                    name:
                        description:
                            - Names of user groups that can authenticate with the captive portal.
                        required: true
                        type: str
            security_mac_auth_bypass:
                description:
                    - Enable/disable MAC authentication bypass.
                type: str
                choices:
                    - mac-auth-only
                    - enable
                    - disable
            security_mode:
                description:
                    - Turn on captive portal authentication for this interface.
                type: str
                choices:
                    - none
                    - captive-portal
                    - 802.1X
            security_redirect_url:
                description:
                    - URL redirection after disclaimer/authentication.
                type: str
            service_name:
                description:
                    - PPPoE service name.
                type: str
            sflow_sampler:
                description:
                    - Enable/disable sFlow on this interface.
                type: str
                choices:
                    - enable
                    - disable
            snmp_index:
                description:
                    - Permanent SNMP Index of the interface.
                type: int
            speed:
                description:
                    - Interface speed. The default setting and the options available depend on the interface hardware.
                type: str
                choices:
                    - auto
                    - 10full
                    - 10half
                    - 100full
                    - 100half
                    - 1000full
                    - 1000half
                    - 1000auto
            spillover_threshold:
                description:
                    - Egress Spillover threshold (0 - 16776000 kbps), 0 means unlimited.
                type: int
            src_check:
                description:
                    - Enable/disable source IP check.
                type: str
                choices:
                    - enable
                    - disable
            status:
                description:
                    - Bring the interface up or shut the interface down.
                type: str
                choices:
                    - up
                    - down
            stpforward:
                description:
                    - Enable/disable STP forwarding.
                type: str
                choices:
                    - enable
                    - disable
            stpforward_mode:
                description:
                    - Configure STP forwarding mode.
                type: str
                choices:
                    - rpl-all-ext-id
                    - rpl-bridge-ext-id
                    - rpl-nothing
            subst:
                description:
                    - Enable to always send packets from this interface to a destination MAC address.
                type: str
                choices:
                    - enable
                    - disable
            substitute_dst_mac:
                description:
                    - Destination MAC address that all packets are sent to from this interface.
                type: str
            swc_vlan:
                description:
                    - Creation status for switch-controller VLANs.
                type: int
            switch:
                description:
                    - Contained in switch.
                type: str
            switch_controller_access_vlan:
                description:
                    - Block FortiSwitch port-to-port traffic.
                type: str
                choices:
                    - enable
                    - disable
            switch_controller_arp_inspection:
                description:
                    - Enable/disable FortiSwitch ARP inspection.
                type: str
                choices:
                    - enable
                    - disable
            switch_controller_dhcp_snooping:
                description:
                    - Switch controller DHCP snooping.
                type: str
                choices:
                    - enable
                    - disable
            switch_controller_dhcp_snooping_option82:
                description:
                    - Switch controller DHCP snooping option82.
                type: str
                choices:
                    - enable
                    - disable
            switch_controller_dhcp_snooping_verify_mac:
                description:
                    - Switch controller DHCP snooping verify MAC.
                type: str
                choices:
                    - enable
                    - disable
            switch_controller_feature:
                description:
                    - Interface"s purpose when assigning traffic (read only).
                type: str
                choices:
                    - none
                    - default-vlan
                    - quarantine
                    - rspan
                    - voice
                    - video
                    - nac
            switch_controller_igmp_snooping:
                description:
                    - Switch controller IGMP snooping.
                type: str
                choices:
                    - enable
                    - disable
            switch_controller_igmp_snooping_fast_leave:
                description:
                    - Switch controller IGMP snooping fast-leave.
                type: str
                choices:
                    - enable
                    - disable
            switch_controller_igmp_snooping_proxy:
                description:
                    - Switch controller IGMP snooping proxy.
                type: str
                choices:
                    - enable
                    - disable
            switch_controller_learning_limit:
                description:
                    - Limit the number of dynamic MAC addresses on this VLAN (1 - 128, 0 = no limit, default).
                type: int
            switch_controller_mgmt_vlan:
                description:
                    - VLAN to use for FortiLink management purposes.
                type: int
            switch_controller_nac:
                description:
                    - Integrated NAC settings for managed FortiSwitch. Source switch-controller.nac-settings.name.
                type: str
            switch_controller_rspan_mode:
                description:
                    - Stop Layer2 MAC learning and interception of BPDUs and other packets on this interface.
                type: str
                choices:
                    - disable
                    - enable
            switch_controller_traffic_policy:
                description:
                    - Switch controller traffic policy for the VLAN. Source switch-controller.traffic-policy.name.
                type: str
            tagging:
                description:
                    - Config object tagging.
                type: list
                suboptions:
                    category:
                        description:
                            - Tag category. Source system.object-tagging.category.
                        type: str
                    name:
                        description:
                            - Tagging entry name.
                        required: true
                        type: str
                    tags:
                        description:
                            - Tags.
                        type: list
                        suboptions:
                            name:
                                description:
                                    - Tag name. Source system.object-tagging.tags.name.
                                required: true
                                type: str
            tcp_mss:
                description:
                    - TCP maximum segment size. 0 means do not change segment size.
                type: int
            trust_ip_1:
                description:
                    - Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
                type: str
            trust_ip_2:
                description:
                    - Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
                type: str
            trust_ip_3:
                description:
                    - Trusted host for dedicated management traffic (0.0.0.0/24 for all hosts).
                type: str
            trust_ip6_1:
                description:
                    - 'Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).'
                type: str
            trust_ip6_2:
                description:
                    - 'Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).'
                type: str
            trust_ip6_3:
                description:
                    - 'Trusted IPv6 host for dedicated management traffic (::/0 for all hosts).'
                type: str
            type:
                description:
                    - Interface type.
                type: str
                choices:
                    - physical
                    - vlan
                    - aggregate
                    - redundant
                    - tunnel
                    - vdom-link
                    - loopback
                    - switch
                    - vap-switch
                    - wl-mesh
                    - fext-wan
                    - vxlan
                    - geneve
                    - hdlc
                    - switch-vlan
                    - emac-vlan
            username:
                description:
                    - Username of the PPPoE account, provided by your ISP.
                type: str
            vdom:
                description:
                    - Interface is in this virtual domain (VDOM). Source system.vdom.name.
                type: str
            vindex:
                description:
                    - Switch control interface VLAN ID.
                type: int
            vlan_protocol:
                description:
                    - Ethernet protocol of VLAN.
                type: str
                choices:
                    - 8021q
                    - 8021ad
            vlanforward:
                description:
                    - Enable/disable traffic forwarding between VLANs on this interface.
                type: str
                choices:
                    - enable
                    - disable
            vlanid:
                description:
                    - VLAN ID (1 - 4094).
                type: int
            vrf:
                description:
                    - Virtual Routing Forwarding ID.
                type: int
            vrrp:
                description:
                    - VRRP configuration.
                type: list
                suboptions:
                    accept_mode:
                        description:
                            - Enable/disable accept mode.
                        type: str
                        choices:
                            - enable
                            - disable
                    adv_interval:
                        description:
                            - Advertisement interval (1 - 255 seconds).
                        type: int
                    ignore_default_route:
                        description:
                            - Enable/disable ignoring of default route when checking destination.
                        type: str
                        choices:
                            - enable
                            - disable
                    preempt:
                        description:
                            - Enable/disable preempt mode.
                        type: str
                        choices:
                            - enable
                            - disable
                    priority:
                        description:
                            - Priority of the virtual router (1 - 255).
                        type: int
                    proxy_arp:
                        description:
                            - VRRP Proxy ARP configuration.
                        type: list
                        suboptions:
                            id:
                                description:
                                    - ID.
                                required: true
                                type: int
                            ip:
                                description:
                                    - Set IP addresses of proxy ARP.
                                type: str
                    start_time:
                        description:
                            - Startup time (1 - 255 seconds).
                        type: int
                    status:
                        description:
                            - Enable/disable this VRRP configuration.
                        type: str
                        choices:
                            - enable
                            - disable
                    version:
                        description:
                            - VRRP version.
                        type: str
                        choices:
                            - 2
                            - 3
                    vrdst:
                        description:
                            - Monitor the route to this destination.
                        type: str
                    vrdst_priority:
                        description:
                            - Priority of the virtual router when the virtual router destination becomes unreachable (0 - 254).
                        type: int
                    vrgrp:
                        description:
                            - VRRP group ID (1 - 65535).
                        type: int
                    vrid:
                        description:
                            - Virtual router identifier (1 - 255).
                        required: true
                        type: int
                    vrip:
                        description:
                            - IP address of the virtual router.
                        type: str
            vrrp_virtual_mac:
                description:
                    - Enable/disable use of virtual MAC for VRRP.
                type: str
                choices:
                    - enable
                    - disable
            wccp:
                description:
                    - Enable/disable WCCP on this interface. Used for encapsulated WCCP communication between WCCP clients and servers.
                type: str
                choices:
                    - enable
                    - disable
            weight:
                description:
                    - Default weight for static routes (if route has no weight configured).
                type: int
            wins_ip:
                description:
                    - WINS server IP.
                type: str
'''

EXAMPLES = '''
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure interfaces.
    fortios_system_interface:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_interface:
        ac_name: "<your_own_value>"
        aggregate: "<your_own_value>"
        algorithm: "L2"
        alias: "<your_own_value>"
        allowaccess: "ping"
        ap_discover: "enable"
        arpforward: "enable"
        auth_type: "auto"
        auto_auth_extension_device: "enable"
        bandwidth_measure_time: "12"
        bfd: "global"
        bfd_desired_min_tx: "14"
        bfd_detect_mult: "15"
        bfd_required_min_rx: "16"
        broadcast_forward: "enable"
        cli_conn_status: "18"
        client_options:
         -
            code: "20"
            id:  "21"
            ip: "<your_own_value>"
            type: "hex"
            value: "<your_own_value>"
        color: "25"
        dedicated_to: "none"
        defaultgw: "enable"
        description: "<your_own_value>"
        detected_peer_mtu: "29"
        detectprotocol: "ping"
        detectserver: "<your_own_value>"
        device_identification: "enable"
        device_user_identification: "enable"
        devindex: "34"
        dhcp_client_identifier:  "myId_35"
        dhcp_relay_agent_option: "enable"
        dhcp_relay_ip: "<your_own_value>"
        dhcp_relay_service: "disable"
        dhcp_relay_type: "regular"
        dhcp_renew_time: "40"
        disc_retry_timeout: "41"
        disconnect_threshold: "42"
        distance: "43"
        dns_server_override: "enable"
        drop_fragment: "enable"
        drop_overlapped_fragment: "enable"
        egress_shaping_profile: "<your_own_value> (source firewall.shaping-profile.profile-name)"
        estimated_downstream_bandwidth: "48"
        estimated_upstream_bandwidth: "49"
        explicit_ftp_proxy: "enable"
        explicit_web_proxy: "enable"
        external: "enable"
        fail_action_on_extender: "soft-restart"
        fail_alert_interfaces:
         -
            name: "default_name_55 (source system.interface.name)"
        fail_alert_method: "link-failed-signal"
        fail_detect: "enable"
        fail_detect_option: "detectserver"
        fortilink: "enable"
        fortilink_backup_link: "60"
        fortilink_neighbor_detect: "lldp"
        fortilink_split_interface: "enable"
        fortilink_stacking: "enable"
        forward_domain: "64"
        gwdetect: "enable"
        ha_priority: "66"
        icmp_accept_redirect: "enable"
        icmp_send_redirect: "enable"
        ident_accept: "enable"
        idle_timeout: "70"
        inbandwidth: "71"
        ingress_shaping_profile: "<your_own_value> (source firewall.shaping-profile.profile-name)"
        ingress_spillover_threshold: "73"
        interface: "<your_own_value> (source system.interface.name)"
        internal: "75"
        ip: "<your_own_value>"
        ip_managed_by_fortiipam: "enable"
        ipmac: "enable"
        ips_sniffer_mode: "enable"
        ipunnumbered: "<your_own_value>"
        ipv6:
            autoconf: "enable"
            dhcp6_client_options: "rapid"
            dhcp6_information_request: "enable"
            dhcp6_prefix_delegation: "enable"
            dhcp6_prefix_hint: "<your_own_value>"
            dhcp6_prefix_hint_plt: "87"
            dhcp6_prefix_hint_vlt: "88"
            dhcp6_relay_ip: "<your_own_value>"
            dhcp6_relay_service: "disable"
            dhcp6_relay_type: "regular"
            ip6_address: "<your_own_value>"
            ip6_allowaccess: "ping"
            ip6_default_life: "94"
            ip6_delegated_prefix_list:
             -
                autonomous_flag: "enable"
                onlink_flag: "enable"
                prefix_id: "98"
                rdnss: "<your_own_value>"
                rdnss_service: "delegated"
                subnet: "<your_own_value>"
                upstream_interface: "<your_own_value> (source system.interface.name)"
            ip6_dns_server_override: "enable"
            ip6_extra_addr:
             -
                prefix: "<your_own_value>"
            ip6_hop_limit: "106"
            ip6_link_mtu: "107"
            ip6_manage_flag: "enable"
            ip6_max_interval: "109"
            ip6_min_interval: "110"
            ip6_mode: "static"
            ip6_other_flag: "enable"
            ip6_prefix_list:
             -
                autonomous_flag: "enable"
                dnssl:
                 -
                    domain: "<your_own_value>"
                onlink_flag: "enable"
                preferred_life_time: "118"
                prefix: "<your_own_value>"
                rdnss: "<your_own_value>"
                valid_life_time: "121"
            ip6_reachable_time: "122"
            ip6_retrans_time: "123"
            ip6_send_adv: "enable"
            ip6_subnet: "<your_own_value>"
            ip6_upstream_interface: "<your_own_value> (source system.interface.name)"
            nd_cert: "<your_own_value> (source certificate.local.name)"
            nd_cga_modifier: "<your_own_value>"
            nd_mode: "basic"
            nd_security_level: "130"
            nd_timestamp_delta: "131"
            nd_timestamp_fuzz: "132"
            vrip6_link_local: "<your_own_value>"
            vrrp_virtual_mac6: "enable"
            vrrp6:
             -
                accept_mode: "enable"
                adv_interval: "137"
                preempt: "enable"
                priority: "139"
                start_time: "140"
                status: "enable"
                vrdst6: "<your_own_value>"
                vrgrp: "143"
                vrid: "144"
                vrip6: "<your_own_value>"
        l2forward: "enable"
        lacp_ha_slave: "enable"
        lacp_mode: "static"
        lacp_speed: "slow"
        lcp_echo_interval: "150"
        lcp_max_echo_fails: "151"
        link_up_delay: "152"
        lldp_network_policy: "<your_own_value> (source system.lldp.network-policy.name)"
        lldp_reception: "enable"
        lldp_transmission: "enable"
        macaddr: "<your_own_value>"
        managed_subnetwork_size: "256"
        management_ip: "<your_own_value>"
        measured_downstream_bandwidth: "159"
        measured_upstream_bandwidth: "160"
        member:
         -
            interface_name: "<your_own_value> (source system.interface.name)"
        min_links: "163"
        min_links_down: "operational"
        mode: "static"
        monitor_bandwidth: "enable"
        mtu: "167"
        mtu_override: "enable"
        name: "default_name_169"
        ndiscforward: "enable"
        netbios_forward: "disable"
        netflow_sampler: "disable"
        outbandwidth: "173"
        padt_retry_timeout: "174"
        password: "<your_own_value>"
        ping_serv_status: "176"
        polling_interval: "177"
        pppoe_unnumbered_negotiate: "enable"
        pptp_auth_type: "auto"
        pptp_client: "enable"
        pptp_password: "<your_own_value>"
        pptp_server_ip: "<your_own_value>"
        pptp_timeout: "183"
        pptp_user: "<your_own_value>"
        preserve_session_route: "enable"
        priority: "186"
        priority_override: "enable"
        proxy_captive_portal: "enable"
        redundant_interface: "<your_own_value>"
        remote_ip: "<your_own_value>"
        replacemsg_override_group: "<your_own_value>"
        ring_rx: "192"
        ring_tx: "193"
        role: "lan"
        sample_direction: "tx"
        sample_rate: "196"
        secondary_IP: "enable"
        secondaryip:
         -
            allowaccess: "ping"
            detectprotocol: "ping"
            detectserver: "<your_own_value>"
            gwdetect: "enable"
            ha_priority: "203"
            id:  "204"
            ip: "<your_own_value>"
            ping_serv_status: "206"
        security_exempt_list: "<your_own_value>"
        security_external_logout: "<your_own_value>"
        security_external_web: "<your_own_value>"
        security_groups:
         -
            name: "default_name_211"
        security_mac_auth_bypass: "mac-auth-only"
        security_mode: "none"
        security_redirect_url: "<your_own_value>"
        service_name: "<your_own_value>"
        sflow_sampler: "enable"
        snmp_index: "217"
        speed: "auto"
        spillover_threshold: "219"
        src_check: "enable"
        status: "up"
        stpforward: "enable"
        stpforward_mode: "rpl-all-ext-id"
        subst: "enable"
        substitute_dst_mac: "<your_own_value>"
        swc_vlan: "226"
        switch: "<your_own_value>"
        switch_controller_access_vlan: "enable"
        switch_controller_arp_inspection: "enable"
        switch_controller_dhcp_snooping: "enable"
        switch_controller_dhcp_snooping_option82: "enable"
        switch_controller_dhcp_snooping_verify_mac: "enable"
        switch_controller_feature: "none"
        switch_controller_igmp_snooping: "enable"
        switch_controller_igmp_snooping_fast_leave: "enable"
        switch_controller_igmp_snooping_proxy: "enable"
        switch_controller_learning_limit: "237"
        switch_controller_mgmt_vlan: "238"
        switch_controller_nac: "<your_own_value> (source switch-controller.nac-settings.name)"
        switch_controller_rspan_mode: "disable"
        switch_controller_traffic_policy: "<your_own_value> (source switch-controller.traffic-policy.name)"
        tagging:
         -
            category: "<your_own_value> (source system.object-tagging.category)"
            name: "default_name_244"
            tags:
             -
                name: "default_name_246 (source system.object-tagging.tags.name)"
        tcp_mss: "247"
        trust_ip_1: "<your_own_value>"
        trust_ip_2: "<your_own_value>"
        trust_ip_3: "<your_own_value>"
        trust_ip6_1: "<your_own_value>"
        trust_ip6_2: "<your_own_value>"
        trust_ip6_3: "<your_own_value>"
        type: "physical"
        username: "<your_own_value>"
        vdom: "<your_own_value> (source system.vdom.name)"
        vindex: "257"
        vlan_protocol: "8021q"
        vlanforward: "enable"
        vlanid: "260"
        vrf: "261"
        vrrp:
         -
            accept_mode: "enable"
            adv_interval: "264"
            ignore_default_route: "enable"
            preempt: "enable"
            priority: "267"
            proxy_arp:
             -
                id:  "269"
                ip: "<your_own_value>"
            start_time: "271"
            status: "enable"
            version: "2"
            vrdst: "<your_own_value>"
            vrdst_priority: "275"
            vrgrp: "276"
            vrid: "277"
            vrip: "<your_own_value>"
        vrrp_virtual_mac: "enable"
        wccp: "enable"
        weight: "281"
        wins_ip: "<your_own_value>"

'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import FortiOSHandler
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import check_legacy_fortiosapi
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import FAIL_SOCKET_MSG


def filter_system_interface_data(json):
    option_list = ['ac_name', 'aggregate', 'algorithm',
                   'alias', 'allowaccess', 'ap_discover',
                   'arpforward', 'auth_type', 'auto_auth_extension_device',
                   'bandwidth_measure_time', 'bfd', 'bfd_desired_min_tx',
                   'bfd_detect_mult', 'bfd_required_min_rx', 'broadcast_forward',
                   'cli_conn_status', 'client_options', 'color',
                   'dedicated_to', 'defaultgw', 'description',
                   'detected_peer_mtu', 'detectprotocol', 'detectserver',
                   'device_identification', 'device_user_identification', 'devindex',
                   'dhcp_client_identifier', 'dhcp_relay_agent_option', 'dhcp_relay_ip',
                   'dhcp_relay_service', 'dhcp_relay_type', 'dhcp_renew_time',
                   'disc_retry_timeout', 'disconnect_threshold', 'distance',
                   'dns_server_override', 'drop_fragment', 'drop_overlapped_fragment',
                   'egress_shaping_profile', 'estimated_downstream_bandwidth', 'estimated_upstream_bandwidth',
                   'explicit_ftp_proxy', 'explicit_web_proxy', 'external',
                   'fail_action_on_extender', 'fail_alert_interfaces', 'fail_alert_method',
                   'fail_detect', 'fail_detect_option', 'fortilink',
                   'fortilink_backup_link', 'fortilink_neighbor_detect', 'fortilink_split_interface',
                   'fortilink_stacking', 'forward_domain', 'gwdetect',
                   'ha_priority', 'icmp_accept_redirect', 'icmp_send_redirect',
                   'ident_accept', 'idle_timeout', 'inbandwidth',
                   'ingress_shaping_profile', 'ingress_spillover_threshold', 'interface',
                   'internal', 'ip', 'ip_managed_by_fortiipam',
                   'ipmac', 'ips_sniffer_mode', 'ipunnumbered',
                   'ipv6', 'l2forward', 'lacp_ha_slave',
                   'lacp_mode', 'lacp_speed', 'lcp_echo_interval',
                   'lcp_max_echo_fails', 'link_up_delay', 'lldp_network_policy',
                   'lldp_reception', 'lldp_transmission', 'macaddr',
                   'managed_subnetwork_size', 'management_ip', 'measured_downstream_bandwidth',
                   'measured_upstream_bandwidth', 'member', 'min_links',
                   'min_links_down', 'mode', 'monitor_bandwidth',
                   'mtu', 'mtu_override', 'name',
                   'ndiscforward', 'netbios_forward', 'netflow_sampler',
                   'outbandwidth', 'padt_retry_timeout', 'password',
                   'ping_serv_status', 'polling_interval', 'pppoe_unnumbered_negotiate',
                   'pptp_auth_type', 'pptp_client', 'pptp_password',
                   'pptp_server_ip', 'pptp_timeout', 'pptp_user',
                   'preserve_session_route', 'priority', 'priority_override',
                   'proxy_captive_portal', 'redundant_interface', 'remote_ip',
                   'replacemsg_override_group', 'ring_rx', 'ring_tx',
                   'role', 'sample_direction', 'sample_rate',
                   'secondary_IP', 'secondaryip', 'security_exempt_list',
                   'security_external_logout', 'security_external_web', 'security_groups',
                   'security_mac_auth_bypass', 'security_mode', 'security_redirect_url',
                   'service_name', 'sflow_sampler', 'snmp_index',
                   'speed', 'spillover_threshold', 'src_check',
                   'status', 'stpforward', 'stpforward_mode',
                   'subst', 'substitute_dst_mac', 'swc_vlan',
                   'switch', 'switch_controller_access_vlan', 'switch_controller_arp_inspection',
                   'switch_controller_dhcp_snooping', 'switch_controller_dhcp_snooping_option82', 'switch_controller_dhcp_snooping_verify_mac',
                   'switch_controller_feature', 'switch_controller_igmp_snooping', 'switch_controller_igmp_snooping_fast_leave',
                   'switch_controller_igmp_snooping_proxy', 'switch_controller_learning_limit', 'switch_controller_mgmt_vlan',
                   'switch_controller_nac', 'switch_controller_rspan_mode', 'switch_controller_traffic_policy',
                   'tagging', 'tcp_mss', 'trust_ip_1',
                   'trust_ip_2', 'trust_ip_3', 'trust_ip6_1',
                   'trust_ip6_2', 'trust_ip6_3', 'type',
                   'username', 'vdom', 'vindex',
                   'vlan_protocol', 'vlanforward', 'vlanid',
                   'vrf', 'vrrp', 'vrrp_virtual_mac',
                   'wccp', 'weight', 'wins_ip']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def flatten_multilists_attributes(data):
    multilist_attrs = [[u'allowaccess'], [u'ipv6', u'ip6_allowaccess']]

    for attr in multilist_attrs:
        try:
            path = "data['" + "']['".join(elem for elem in attr) + "']"
            current_val = eval(path)
            flattened_val = ' '.join(elem for elem in current_val)
            exec(path + '= flattened_val')
        except BaseException:
            pass

    return data


def underscore_to_hyphen(data):
    if isinstance(data, list):
        for i, elem in enumerate(data):
            data[i] = underscore_to_hyphen(elem)
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace('_', '-')] = underscore_to_hyphen(v)
        data = new_data

    return data


def serialize(data):
    if isinstance(data, str) and ' ' in data:
        return serialize(data.split(' '))
    if isinstance(data, list) and len(data) > 0:
        if isinstance(data[0], dict):
            list_to_order = []
            for dt in data:
                ret = {}
                for key, value in dt.items():
                    ret[key] = serialize(value)
                list_to_order.append(ret)

            return sorted(list_to_order, key=lambda dt: str(dt.items()))
        else:
            return sorted(data)

    if isinstance(data, dict):
        result = {}
        for key, value in data.items():
            result[key] = serialize(value)

        return result

    return data


def is_same_comparison(reorder_current, reorder_filtered):
    for key, value in reorder_filtered.items():
        if key not in reorder_current:
            return False

        if isinstance(value, dict):
            if not is_same_comparison(reorder_current[key], value):
                return False
        elif isinstance(value, list):
            if len(value) != len(reorder_current[key]):
                return False
            if isinstance(value[0], dict):
                for current_dict in reorder_current[key]:
                    if not is_same_comparison(current_dict, value[0]):
                        return False
            elif reorder_current[key] != value:
                return False
        elif reorder_current[key] != value:
            return False

    return True


def system_interface(data, fos, check_mode=False):

    vdom = data['vdom']
    if 'state' in data and data['state']:
        state = data['state']
    elif 'state' in data['system_interface'] and data['system_interface']['state']:
        state = data['system_interface']['state']
    else:
        state = True
    system_interface_data = data['system_interface']
    system_interface_data = flatten_multilists_attributes(system_interface_data)
    filtered_data = underscore_to_hyphen(filter_system_interface_data(system_interface_data))

    # check_mode starts from here
    if check_mode:
        mkey = fos.get_mkey('system', 'interface', filtered_data, vdom=vdom)
        current_data = fos.get('system', 'interface', vdom=vdom, mkey=mkey)
        is_existed = current_data and current_data.get('http_status') == 200 \
            and isinstance(current_data.get('results'), list) \
            and len(current_data['results']) > 0

        # 2. if it exists and the state is 'present' then compare current settings with desired
        if state == 'present':
            if mkey is None:
                return False, True, filtered_data

            # if mkey exists then compare each other
            # record exits and they're matched or not
            if is_existed:
                is_same = is_same_comparison(
                    serialize(current_data['results'][0]), serialize(filtered_data))
                return False, not is_same, filtered_data

            # record does not exist
            return False, True, filtered_data

        if state == 'absent':
            if mkey is None:
                return False, False, filtered_data

            if is_existed:
                return False, True, filtered_data
            return False, False, filtered_data

        return True, False, {'reason: ': 'Must provide state parameter'}

    if state == "present":
        return fos.set('system',
                       'interface',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('system',
                          'interface',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_system(data, fos, check_mode):

    if data['system_interface']:
        resp = system_interface(data, fos, check_mode)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('system_interface'))
    if check_mode:
        return resp
    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = 'name'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": False, "type": "str",
                  "choices": ["present", "absent"]},
        "system_interface": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "state": {"required": False, "type": "str",
                          "choices": ["present", "absent"]},
                "ac_name": {"required": False, "type": "str"},
                "aggregate": {"required": False, "type": "str"},
                "algorithm": {"required": False, "type": "str",
                              "choices": ["L2",
                                          "L3",
                                          "L4"]},
                "alias": {"required": False, "type": "str"},
                "allowaccess": {"required": False, "type": "list",
                                "choices": ["ping",
                                            "https",
                                            "ssh",
                                            "snmp",
                                            "http",
                                            "telnet",
                                            "fgfm",
                                            "radius-acct",
                                            "probe-response",
                                            "fabric",
                                            "ftm"]},
                "ap_discover": {"required": False, "type": "str",
                                "choices": ["enable",
                                            "disable"]},
                "arpforward": {"required": False, "type": "str",
                               "choices": ["enable",
                                           "disable"]},
                "auth_type": {"required": False, "type": "str",
                              "choices": ["auto",
                                          "pap",
                                          "chap",
                                          "mschapv1",
                                          "mschapv2"]},
                "auto_auth_extension_device": {"required": False, "type": "str",
                                               "choices": ["enable",
                                                           "disable"]},
                "bandwidth_measure_time": {"required": False, "type": "int"},
                "bfd": {"required": False, "type": "str",
                        "choices": ["global",
                                    "enable",
                                    "disable"]},
                "bfd_desired_min_tx": {"required": False, "type": "int"},
                "bfd_detect_mult": {"required": False, "type": "int"},
                "bfd_required_min_rx": {"required": False, "type": "int"},
                "broadcast_forward": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable"]},
                "cli_conn_status": {"required": False, "type": "int"},
                "client_options": {"required": False, "type": "list",
                                   "options": {
                                       "code": {"required": False, "type": "int"},
                                       "id": {"required": True, "type": "int"},
                                       "ip": {"required": False, "type": "str"},
                                       "type": {"required": False, "type": "str",
                                                "choices": ["hex",
                                                            "string",
                                                            "ip",
                                                            "fqdn"]},
                                       "value": {"required": False, "type": "str"}
                                   }},
                "color": {"required": False, "type": "int"},
                "dedicated_to": {"required": False, "type": "str",
                                 "choices": ["none",
                                             "management"]},
                "defaultgw": {"required": False, "type": "str",
                              "choices": ["enable",
                                          "disable"]},
                "description": {"required": False, "type": "str"},
                "detected_peer_mtu": {"required": False, "type": "int"},
                "detectprotocol": {"required": False, "type": "str",
                                   "choices": ["ping",
                                               "tcp-echo",
                                               "udp-echo"]},
                "detectserver": {"required": False, "type": "str"},
                "device_identification": {"required": False, "type": "str",
                                          "choices": ["enable",
                                                      "disable"]},
                "device_user_identification": {"required": False, "type": "str",
                                               "choices": ["enable",
                                                           "disable"]},
                "devindex": {"required": False, "type": "int"},
                "dhcp_client_identifier": {"required": False, "type": "str"},
                "dhcp_relay_agent_option": {"required": False, "type": "str",
                                            "choices": ["enable",
                                                        "disable"]},
                "dhcp_relay_ip": {"required": False, "type": "str"},
                "dhcp_relay_service": {"required": False, "type": "str",
                                       "choices": ["disable",
                                                   "enable"]},
                "dhcp_relay_type": {"required": False, "type": "str",
                                    "choices": ["regular",
                                                "ipsec"]},
                "dhcp_renew_time": {"required": False, "type": "int"},
                "disc_retry_timeout": {"required": False, "type": "int"},
                "disconnect_threshold": {"required": False, "type": "int"},
                "distance": {"required": False, "type": "int"},
                "dns_server_override": {"required": False, "type": "str",
                                        "choices": ["enable",
                                                    "disable"]},
                "drop_fragment": {"required": False, "type": "str",
                                  "choices": ["enable",
                                              "disable"]},
                "drop_overlapped_fragment": {"required": False, "type": "str",
                                             "choices": ["enable",
                                                         "disable"]},
                "egress_shaping_profile": {"required": False, "type": "str"},
                "estimated_downstream_bandwidth": {"required": False, "type": "int"},
                "estimated_upstream_bandwidth": {"required": False, "type": "int"},
                "explicit_ftp_proxy": {"required": False, "type": "str",
                                       "choices": ["enable",
                                                   "disable"]},
                "explicit_web_proxy": {"required": False, "type": "str",
                                       "choices": ["enable",
                                                   "disable"]},
                "external": {"required": False, "type": "str",
                             "choices": ["enable",
                                         "disable"]},
                "fail_action_on_extender": {"required": False, "type": "str",
                                            "choices": ["soft-restart",
                                                        "hard-restart",
                                                        "reboot"]},
                "fail_alert_interfaces": {"required": False, "type": "list",
                                          "options": {
                                              "name": {"required": True, "type": "str"}
                                          }},
                "fail_alert_method": {"required": False, "type": "str",
                                      "choices": ["link-failed-signal",
                                                  "link-down"]},
                "fail_detect": {"required": False, "type": "str",
                                "choices": ["enable",
                                            "disable"]},
                "fail_detect_option": {"required": False, "type": "str",
                                       "choices": ["detectserver",
                                                   "link-down"]},
                "fortilink": {"required": False, "type": "str",
                              "choices": ["enable",
                                          "disable"]},
                "fortilink_backup_link": {"required": False, "type": "int"},
                "fortilink_neighbor_detect": {"required": False, "type": "str",
                                              "choices": ["lldp",
                                                          "fortilink"]},
                "fortilink_split_interface": {"required": False, "type": "str",
                                              "choices": ["enable",
                                                          "disable"]},
                "fortilink_stacking": {"required": False, "type": "str",
                                       "choices": ["enable",
                                                   "disable"]},
                "forward_domain": {"required": False, "type": "int"},
                "gwdetect": {"required": False, "type": "str",
                             "choices": ["enable",
                                         "disable"]},
                "ha_priority": {"required": False, "type": "int"},
                "icmp_accept_redirect": {"required": False, "type": "str",
                                         "choices": ["enable",
                                                     "disable"]},
                "icmp_send_redirect": {"required": False, "type": "str",
                                       "choices": ["enable",
                                                   "disable"]},
                "ident_accept": {"required": False, "type": "str",
                                 "choices": ["enable",
                                             "disable"]},
                "idle_timeout": {"required": False, "type": "int"},
                "inbandwidth": {"required": False, "type": "int"},
                "ingress_shaping_profile": {"required": False, "type": "str"},
                "ingress_spillover_threshold": {"required": False, "type": "int"},
                "interface": {"required": False, "type": "str"},
                "internal": {"required": False, "type": "int"},
                "ip": {"required": False, "type": "str"},
                "ip_managed_by_fortiipam": {"required": False, "type": "str",
                                            "choices": ["enable",
                                                        "disable"]},
                "ipmac": {"required": False, "type": "str",
                          "choices": ["enable",
                                      "disable"]},
                "ips_sniffer_mode": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "ipunnumbered": {"required": False, "type": "str"},
                "ipv6": {"required": False, "type": "dict",
                         "options": {
                             "autoconf": {"required": False, "type": "str",
                                          "choices": ["enable",
                                                      "disable"]},
                             "dhcp6_client_options": {"required": False, "type": "str",
                                                      "choices": ["rapid",
                                                                  "iapd",
                                                                  "iana"]},
                             "dhcp6_information_request": {"required": False, "type": "str",
                                                           "choices": ["enable",
                                                                       "disable"]},
                             "dhcp6_prefix_delegation": {"required": False, "type": "str",
                                                         "choices": ["enable",
                                                                     "disable"]},
                             "dhcp6_prefix_hint": {"required": False, "type": "str"},
                             "dhcp6_prefix_hint_plt": {"required": False, "type": "int"},
                             "dhcp6_prefix_hint_vlt": {"required": False, "type": "int"},
                             "dhcp6_relay_ip": {"required": False, "type": "str"},
                             "dhcp6_relay_service": {"required": False, "type": "str",
                                                     "choices": ["disable",
                                                                 "enable"]},
                             "dhcp6_relay_type": {"required": False, "type": "str",
                                                  "choices": ["regular"]},
                             "ip6_address": {"required": False, "type": "str"},
                             "ip6_allowaccess": {"required": False, "type": "list",
                                                 "choices": ["ping",
                                                             "https",
                                                             "ssh",
                                                             "snmp",
                                                             "http",
                                                             "telnet",
                                                             "fgfm",
                                                             "fabric"]},
                             "ip6_default_life": {"required": False, "type": "int"},
                             "ip6_delegated_prefix_list": {"required": False, "type": "list",
                                                           "options": {
                                                               "autonomous_flag": {"required": False, "type": "str",
                                                                                   "choices": ["enable",
                                                                                               "disable"]},
                                                               "onlink_flag": {"required": False, "type": "str",
                                                                               "choices": ["enable",
                                                                                           "disable"]},
                                                               "prefix_id": {"required": False, "type": "int"},
                                                               "rdnss": {"required": False, "type": "str"},
                                                               "rdnss_service": {"required": False, "type": "str",
                                                                                 "choices": ["delegated",
                                                                                             "default",
                                                                                             "specify"]},
                                                               "subnet": {"required": False, "type": "str"},
                                                               "upstream_interface": {"required": False, "type": "str"}
                                                           }},
                             "ip6_dns_server_override": {"required": False, "type": "str",
                                                         "choices": ["enable",
                                                                     "disable"]},
                             "ip6_extra_addr": {"required": False, "type": "list",
                                                "options": {
                                                    "prefix": {"required": True, "type": "str"}
                                                }},
                             "ip6_hop_limit": {"required": False, "type": "int"},
                             "ip6_link_mtu": {"required": False, "type": "int"},
                             "ip6_manage_flag": {"required": False, "type": "str",
                                                 "choices": ["enable",
                                                             "disable"]},
                             "ip6_max_interval": {"required": False, "type": "int"},
                             "ip6_min_interval": {"required": False, "type": "int"},
                             "ip6_mode": {"required": False, "type": "str",
                                          "choices": ["static",
                                                      "dhcp",
                                                      "pppoe",
                                                      "delegated"]},
                             "ip6_other_flag": {"required": False, "type": "str",
                                                "choices": ["enable",
                                                            "disable"]},
                             "ip6_prefix_list": {"required": False, "type": "list",
                                                 "options": {
                                                     "autonomous_flag": {"required": False, "type": "str",
                                                                         "choices": ["enable",
                                                                                     "disable"]},
                                                     "dnssl": {"required": False, "type": "list",
                                                               "options": {
                                                                   "domain": {"required": True, "type": "str"}
                                                               }},
                                                     "onlink_flag": {"required": False, "type": "str",
                                                                     "choices": ["enable",
                                                                                 "disable"]},
                                                     "preferred_life_time": {"required": False, "type": "int"},
                                                     "prefix": {"required": True, "type": "str"},
                                                     "rdnss": {"required": False, "type": "str"},
                                                     "valid_life_time": {"required": False, "type": "int"}
                                                 }},
                             "ip6_reachable_time": {"required": False, "type": "int"},
                             "ip6_retrans_time": {"required": False, "type": "int"},
                             "ip6_send_adv": {"required": False, "type": "str",
                                              "choices": ["enable",
                                                          "disable"]},
                             "ip6_subnet": {"required": False, "type": "str"},
                             "ip6_upstream_interface": {"required": False, "type": "str"},
                             "nd_cert": {"required": False, "type": "str"},
                             "nd_cga_modifier": {"required": False, "type": "str"},
                             "nd_mode": {"required": False, "type": "str",
                                         "choices": ["basic",
                                                     "SEND-compatible"]},
                             "nd_security_level": {"required": False, "type": "int"},
                             "nd_timestamp_delta": {"required": False, "type": "int"},
                             "nd_timestamp_fuzz": {"required": False, "type": "int"},
                             "vrip6_link_local": {"required": False, "type": "str"},
                             "vrrp_virtual_mac6": {"required": False, "type": "str",
                                                   "choices": ["enable",
                                                               "disable"]},
                             "vrrp6": {"required": False, "type": "list",
                                       "options": {
                                           "accept_mode": {"required": False, "type": "str",
                                                           "choices": ["enable",
                                                                       "disable"]},
                                           "adv_interval": {"required": False, "type": "int"},
                                           "preempt": {"required": False, "type": "str",
                                                       "choices": ["enable",
                                                                   "disable"]},
                                           "priority": {"required": False, "type": "int"},
                                           "start_time": {"required": False, "type": "int"},
                                           "status": {"required": False, "type": "str",
                                                      "choices": ["enable",
                                                                  "disable"]},
                                           "vrdst6": {"required": False, "type": "str"},
                                           "vrgrp": {"required": False, "type": "int"},
                                           "vrid": {"required": True, "type": "int"},
                                           "vrip6": {"required": False, "type": "str"}
                                       }}
                         }},
                "l2forward": {"required": False, "type": "str",
                              "choices": ["enable",
                                          "disable"]},
                "lacp_ha_slave": {"required": False, "type": "str",
                                  "choices": ["enable",
                                              "disable"]},
                "lacp_mode": {"required": False, "type": "str",
                              "choices": ["static",
                                          "passive",
                                          "active"]},
                "lacp_speed": {"required": False, "type": "str",
                               "choices": ["slow",
                                           "fast"]},
                "lcp_echo_interval": {"required": False, "type": "int"},
                "lcp_max_echo_fails": {"required": False, "type": "int"},
                "link_up_delay": {"required": False, "type": "int"},
                "lldp_network_policy": {"required": False, "type": "str"},
                "lldp_reception": {"required": False, "type": "str",
                                   "choices": ["enable",
                                               "disable",
                                               "vdom"]},
                "lldp_transmission": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable",
                                                  "vdom"]},
                "macaddr": {"required": False, "type": "str"},
                "managed_subnetwork_size": {"required": False, "type": "str",
                                            "choices": ["256",
                                                        "512",
                                                        "1024",
                                                        "2048",
                                                        "4096",
                                                        "8192",
                                                        "16384",
                                                        "32768",
                                                        "65536"]},
                "management_ip": {"required": False, "type": "str"},
                "measured_downstream_bandwidth": {"required": False, "type": "int"},
                "measured_upstream_bandwidth": {"required": False, "type": "int"},
                "member": {"required": False, "type": "list",
                           "options": {
                               "interface_name": {"required": False, "type": "str"}
                           }},
                "min_links": {"required": False, "type": "int"},
                "min_links_down": {"required": False, "type": "str",
                                   "choices": ["operational",
                                               "administrative"]},
                "mode": {"required": False, "type": "str",
                         "choices": ["static",
                                     "dhcp",
                                     "pppoe"]},
                "monitor_bandwidth": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable"]},
                "mtu": {"required": False, "type": "int"},
                "mtu_override": {"required": False, "type": "str",
                                 "choices": ["enable",
                                             "disable"]},
                "name": {"required": True, "type": "str"},
                "ndiscforward": {"required": False, "type": "str",
                                 "choices": ["enable",
                                             "disable"]},
                "netbios_forward": {"required": False, "type": "str",
                                    "choices": ["disable",
                                                "enable"]},
                "netflow_sampler": {"required": False, "type": "str",
                                    "choices": ["disable",
                                                "tx",
                                                "rx",
                                                "both"]},
                "outbandwidth": {"required": False, "type": "int"},
                "padt_retry_timeout": {"required": False, "type": "int"},
                "password": {"required": False, "type": "str"},
                "ping_serv_status": {"required": False, "type": "int"},
                "polling_interval": {"required": False, "type": "int"},
                "pppoe_unnumbered_negotiate": {"required": False, "type": "str",
                                               "choices": ["enable",
                                                           "disable"]},
                "pptp_auth_type": {"required": False, "type": "str",
                                   "choices": ["auto",
                                               "pap",
                                               "chap",
                                               "mschapv1",
                                               "mschapv2"]},
                "pptp_client": {"required": False, "type": "str",
                                "choices": ["enable",
                                            "disable"]},
                "pptp_password": {"required": False, "type": "str"},
                "pptp_server_ip": {"required": False, "type": "str"},
                "pptp_timeout": {"required": False, "type": "int"},
                "pptp_user": {"required": False, "type": "str"},
                "preserve_session_route": {"required": False, "type": "str",
                                           "choices": ["enable",
                                                       "disable"]},
                "priority": {"required": False, "type": "int"},
                "priority_override": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable"]},
                "proxy_captive_portal": {"required": False, "type": "str",
                                         "choices": ["enable",
                                                     "disable"]},
                "redundant_interface": {"required": False, "type": "str"},
                "remote_ip": {"required": False, "type": "str"},
                "replacemsg_override_group": {"required": False, "type": "str"},
                "ring_rx": {"required": False, "type": "int"},
                "ring_tx": {"required": False, "type": "int"},
                "role": {"required": False, "type": "str",
                         "choices": ["lan",
                                     "wan",
                                     "dmz",
                                     "undefined"]},
                "sample_direction": {"required": False, "type": "str",
                                     "choices": ["tx",
                                                 "rx",
                                                 "both"]},
                "sample_rate": {"required": False, "type": "int"},
                "secondary_IP": {"required": False, "type": "str",
                                 "choices": ["enable",
                                             "disable"]},
                "secondaryip": {"required": False, "type": "list",
                                "options": {
                                    "allowaccess": {"required": False, "type": "str",
                                                    "choices": ["ping",
                                                                "https",
                                                                "ssh",
                                                                "snmp",
                                                                "http",
                                                                "telnet",
                                                                "fgfm",
                                                                "radius-acct",
                                                                "probe-response",
                                                                "fabric",
                                                                "ftm"]},
                                    "detectprotocol": {"required": False, "type": "str",
                                                       "choices": ["ping",
                                                                   "tcp-echo",
                                                                   "udp-echo"]},
                                    "detectserver": {"required": False, "type": "str"},
                                    "gwdetect": {"required": False, "type": "str",
                                                 "choices": ["enable",
                                                             "disable"]},
                                    "ha_priority": {"required": False, "type": "int"},
                                    "id": {"required": True, "type": "int"},
                                    "ip": {"required": False, "type": "str"},
                                    "ping_serv_status": {"required": False, "type": "int"}
                                }},
                "security_exempt_list": {"required": False, "type": "str"},
                "security_external_logout": {"required": False, "type": "str"},
                "security_external_web": {"required": False, "type": "str"},
                "security_groups": {"required": False, "type": "list",
                                    "options": {
                                        "name": {"required": True, "type": "str"}
                                    }},
                "security_mac_auth_bypass": {"required": False, "type": "str",
                                             "choices": ["mac-auth-only",
                                                         "enable",
                                                         "disable"]},
                "security_mode": {"required": False, "type": "str",
                                  "choices": ["none",
                                              "captive-portal",
                                              "802.1X"]},
                "security_redirect_url": {"required": False, "type": "str"},
                "service_name": {"required": False, "type": "str"},
                "sflow_sampler": {"required": False, "type": "str",
                                  "choices": ["enable",
                                              "disable"]},
                "snmp_index": {"required": False, "type": "int"},
                "speed": {"required": False, "type": "str",
                          "choices": ["auto",
                                      "10full",
                                      "10half",
                                      "100full",
                                      "100half",
                                      "1000full",
                                      "1000half",
                                      "1000auto"]},
                "spillover_threshold": {"required": False, "type": "int"},
                "src_check": {"required": False, "type": "str",
                              "choices": ["enable",
                                          "disable"]},
                "status": {"required": False, "type": "str",
                           "choices": ["up",
                                       "down"]},
                "stpforward": {"required": False, "type": "str",
                               "choices": ["enable",
                                           "disable"]},
                "stpforward_mode": {"required": False, "type": "str",
                                    "choices": ["rpl-all-ext-id",
                                                "rpl-bridge-ext-id",
                                                "rpl-nothing"]},
                "subst": {"required": False, "type": "str",
                          "choices": ["enable",
                                      "disable"]},
                "substitute_dst_mac": {"required": False, "type": "str"},
                "swc_vlan": {"required": False, "type": "int"},
                "switch": {"required": False, "type": "str"},
                "switch_controller_access_vlan": {"required": False, "type": "str",
                                                  "choices": ["enable",
                                                              "disable"]},
                "switch_controller_arp_inspection": {"required": False, "type": "str",
                                                     "choices": ["enable",
                                                                 "disable"]},
                "switch_controller_dhcp_snooping": {"required": False, "type": "str",
                                                    "choices": ["enable",
                                                                "disable"]},
                "switch_controller_dhcp_snooping_option82": {"required": False, "type": "str",
                                                             "choices": ["enable",
                                                                         "disable"]},
                "switch_controller_dhcp_snooping_verify_mac": {"required": False, "type": "str",
                                                               "choices": ["enable",
                                                                           "disable"]},
                "switch_controller_feature": {"required": False, "type": "str",
                                              "choices": ["none",
                                                          "default-vlan",
                                                          "quarantine",
                                                          "rspan",
                                                          "voice",
                                                          "video",
                                                          "nac"]},
                "switch_controller_igmp_snooping": {"required": False, "type": "str",
                                                    "choices": ["enable",
                                                                "disable"]},
                "switch_controller_igmp_snooping_fast_leave": {"required": False, "type": "str",
                                                               "choices": ["enable",
                                                                           "disable"]},
                "switch_controller_igmp_snooping_proxy": {"required": False, "type": "str",
                                                          "choices": ["enable",
                                                                      "disable"]},
                "switch_controller_learning_limit": {"required": False, "type": "int"},
                "switch_controller_mgmt_vlan": {"required": False, "type": "int"},
                "switch_controller_nac": {"required": False, "type": "str"},
                "switch_controller_rspan_mode": {"required": False, "type": "str",
                                                 "choices": ["disable",
                                                             "enable"]},
                "switch_controller_traffic_policy": {"required": False, "type": "str"},
                "tagging": {"required": False, "type": "list",
                            "options": {
                                "category": {"required": False, "type": "str"},
                                "name": {"required": True, "type": "str"},
                                "tags": {"required": False, "type": "list",
                                         "options": {
                                             "name": {"required": True, "type": "str"}
                                         }}
                            }},
                "tcp_mss": {"required": False, "type": "int"},
                "trust_ip_1": {"required": False, "type": "str"},
                "trust_ip_2": {"required": False, "type": "str"},
                "trust_ip_3": {"required": False, "type": "str"},
                "trust_ip6_1": {"required": False, "type": "str"},
                "trust_ip6_2": {"required": False, "type": "str"},
                "trust_ip6_3": {"required": False, "type": "str"},
                "type": {"required": False, "type": "str",
                         "choices": ["physical",
                                     "vlan",
                                     "aggregate",
                                     "redundant",
                                     "tunnel",
                                     "vdom-link",
                                     "loopback",
                                     "switch",
                                     "vap-switch",
                                     "wl-mesh",
                                     "fext-wan",
                                     "vxlan",
                                     "geneve",
                                     "hdlc",
                                     "switch-vlan",
                                     "emac-vlan"]},
                "username": {"required": False, "type": "str"},
                "vdom": {"required": False, "type": "str"},
                "vindex": {"required": False, "type": "int"},
                "vlan_protocol": {"required": False, "type": "str",
                                  "choices": ["8021q",
                                              "8021ad"]},
                "vlanforward": {"required": False, "type": "str",
                                "choices": ["enable",
                                            "disable"]},
                "vlanid": {"required": False, "type": "int"},
                "vrf": {"required": False, "type": "int"},
                "vrrp": {"required": False, "type": "list",
                         "options": {
                             "accept_mode": {"required": False, "type": "str",
                                             "choices": ["enable",
                                                         "disable"]},
                             "adv_interval": {"required": False, "type": "int"},
                             "ignore_default_route": {"required": False, "type": "str",
                                                      "choices": ["enable",
                                                                  "disable"]},
                             "preempt": {"required": False, "type": "str",
                                         "choices": ["enable",
                                                     "disable"]},
                             "priority": {"required": False, "type": "int"},
                             "proxy_arp": {"required": False, "type": "list",
                                           "options": {
                                               "id": {"required": True, "type": "int"},
                                               "ip": {"required": False, "type": "str"}
                                           }},
                             "start_time": {"required": False, "type": "int"},
                             "status": {"required": False, "type": "str",
                                        "choices": ["enable",
                                                    "disable"]},
                             "version": {"required": False, "type": "str",
                                         "choices": ["2",
                                                     "3"]},
                             "vrdst": {"required": False, "type": "str"},
                             "vrdst_priority": {"required": False, "type": "int"},
                             "vrgrp": {"required": False, "type": "int"},
                             "vrid": {"required": True, "type": "int"},
                             "vrip": {"required": False, "type": "str"}
                         }},
                "vrrp_virtual_mac": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "wccp": {"required": False, "type": "str",
                         "choices": ["enable",
                                     "disable"]},
                "weight": {"required": False, "type": "int"},
                "wins_ip": {"required": False, "type": "str"}

            }
        }
    }

    check_legacy_fortiosapi()
    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=True)

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if 'access_token' in module.params:
            connection.set_option('access_token', module.params['access_token'])

        fos = FortiOSHandler(connection, module, mkeyname)

        is_error, has_changed, result = fortios_system(module.params, fos, module.check_mode)
        versions_check_result = connection.get_system_version()
    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    if versions_check_result and versions_check_result['matched'] is False:
        module.warn("Ansible has detected version mismatch between FortOS system and galaxy, see more details by specifying option -vvv")

    if not is_error:
        if versions_check_result and versions_check_result['matched'] is False:
            module.exit_json(changed=has_changed, version_check_warning=versions_check_result, meta=result)
        else:
            module.exit_json(changed=has_changed, meta=result)
    else:
        if versions_check_result and versions_check_result['matched'] is False:
            module.fail_json(msg="Error in repo", version_check_warning=versions_check_result, meta=result)
        else:
            module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
