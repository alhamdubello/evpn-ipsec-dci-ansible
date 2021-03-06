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
module: fortios_firewall_policy
short_description: Configure IPv4/IPv6 policies in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify firewall feature and policy category.
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
    - Adjust object order by moving self after(before) another.
    - Only one of [after, before] must be specified when action is moving an object.

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
    action:
        description:
            - the action indiactor to move an object in the list
        type: str
        choices:
            - move
    self:
        description:
            - mkey of self identifier
        type: str
    after:
        description:
            - mkey of target identifier
        type: str
    before:
        description:
            - mkey of target identifier
        type: str

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
    firewall_policy:
        description:
            - Configure IPv4/IPv6 policies.
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
            action:
                description:
                    - Policy action (allow/deny/ipsec).
                type: str
                choices:
                    - accept
                    - deny
                    - ipsec
            anti_replay:
                description:
                    - Enable/disable anti-replay check.
                type: str
                choices:
                    - enable
                    - disable
            app_category:
                description:
                    - Application category ID list.
                type: list
                suboptions:
                    id:
                        description:
                            - Category IDs.
                        required: true
                        type: int
            app_group:
                description:
                    - Application group names.
                type: list
                suboptions:
                    name:
                        description:
                            - Application group names.
                        required: true
                        type: str
            application:
                description:
                    - Application ID list.
                type: list
                suboptions:
                    id:
                        description:
                            - Application IDs.
                        required: true
                        type: int
            application_list:
                description:
                    - Name of an existing Application list. Source application.list.name.
                type: str
            auth_cert:
                description:
                    - HTTPS server certificate for policy authentication. Source vpn.certificate.local.name.
                type: str
            auth_path:
                description:
                    - Enable/disable authentication-based routing.
                type: str
                choices:
                    - enable
                    - disable
            auth_redirect_addr:
                description:
                    - HTTP-to-HTTPS redirect address for firewall authentication.
                type: str
            auto_asic_offload:
                description:
                    - Enable/disable policy traffic ASIC offloading.
                type: str
                choices:
                    - enable
                    - disable
            av_profile:
                description:
                    - Name of an existing Antivirus profile. Source antivirus.profile.name.
                type: str
            block_notification:
                description:
                    - Enable/disable block notification.
                type: str
                choices:
                    - enable
                    - disable
            captive_portal_exempt:
                description:
                    - Enable to exempt some users from the captive portal.
                type: str
                choices:
                    - enable
                    - disable
            capture_packet:
                description:
                    - Enable/disable capture packets.
                type: str
                choices:
                    - enable
                    - disable
            cifs_profile:
                description:
                    - Name of an existing CIFS profile. Source cifs.profile.name.
                type: str
            comments:
                description:
                    - Comment.
                type: str
            custom_log_fields:
                description:
                    - Custom fields to append to log messages for this policy.
                type: list
                suboptions:
                    field_id:
                        description:
                            - Custom log field. Source log.custom-field.id.
                        type: str
            decrypted_traffic_mirror:
                description:
                    - Decrypted traffic mirror. Source firewall.decrypted-traffic-mirror.name.
                type: str
            delay_tcp_npu_session:
                description:
                    - Enable TCP NPU session delay to guarantee packet order of 3-way handshake.
                type: str
                choices:
                    - enable
                    - disable
            diffserv_forward:
                description:
                    - Enable to change packet"s DiffServ values to the specified diffservcode-forward value.
                type: str
                choices:
                    - enable
                    - disable
            diffserv_reverse:
                description:
                    - Enable to change packet"s reverse (reply) DiffServ values to the specified diffservcode-rev value.
                type: str
                choices:
                    - enable
                    - disable
            diffservcode_forward:
                description:
                    - Change packet"s DiffServ to this value.
                type: str
            diffservcode_rev:
                description:
                    - Change packet"s reverse (reply) DiffServ to this value.
                type: str
            disclaimer:
                description:
                    - Enable/disable user authentication disclaimer.
                type: str
                choices:
                    - enable
                    - disable
            dlp_sensor:
                description:
                    - Name of an existing DLP sensor. Source dlp.sensor.name.
                type: str
            dnsfilter_profile:
                description:
                    - Name of an existing DNS filter profile. Source dnsfilter.profile.name.
                type: str
            dsri:
                description:
                    - Enable DSRI to ignore HTTP server responses.
                type: str
                choices:
                    - enable
                    - disable
            dstaddr:
                description:
                    - Destination IPv4 address and address group names.
                type: list
                suboptions:
                    name:
                        description:
                            - Address name. Source firewall.address.name firewall.addrgrp.name firewall.vip.name firewall.vipgrp.name system.external-resource
                              .name.
                        required: true
                        type: str
            dstaddr_negate:
                description:
                    - When enabled dstaddr/dstaddr6 specifies what the destination address must NOT be.
                type: str
                choices:
                    - enable
                    - disable
            dstaddr6:
                description:
                    - Destination IPv6 address name and address group names.
                type: list
                suboptions:
                    name:
                        description:
                            - Address name. Source firewall.address6.name firewall.addrgrp6.name firewall.vipgrp6.name firewall.vip6.name system
                              .external-resource.name.
                        required: true
                        type: str
            dstintf:
                description:
                    - Outgoing (egress) interface.
                type: list
                suboptions:
                    name:
                        description:
                            - Interface name. Source system.interface.name system.zone.name.
                        required: true
                        type: str
            email_collect:
                description:
                    - Enable/disable email collection.
                type: str
                choices:
                    - enable
                    - disable
            emailfilter_profile:
                description:
                    - Name of an existing email filter profile. Source emailfilter.profile.name.
                type: str
            firewall_session_dirty:
                description:
                    - How to handle sessions if the configuration of this firewall policy changes.
                type: str
                choices:
                    - check-all
                    - check-new
            fixedport:
                description:
                    - Enable to prevent source NAT from changing a session"s source port.
                type: str
                choices:
                    - enable
                    - disable
            fsso_agent_for_ntlm:
                description:
                    - FSSO agent to use for NTLM authentication. Source user.fsso.name.
                type: str
            fsso_groups:
                description:
                    - Names of FSSO groups.
                type: list
                suboptions:
                    name:
                        description:
                            - Names of FSSO groups. Source user.adgrp.name.
                        required: true
                        type: str
            geoip_anycast:
                description:
                    - Enable/disable recognition of anycast IP addresses using the geography IP database.
                type: str
                choices:
                    - enable
                    - disable
            geoip_match:
                description:
                    - Match geography address based either on its physical location or registered location.
                type: str
                choices:
                    - physical-location
                    - registered-location
            groups:
                description:
                    - Names of user groups that can authenticate with this policy.
                type: list
                suboptions:
                    name:
                        description:
                            - Group name. Source user.group.name.
                        required: true
                        type: str
            http_policy_redirect:
                description:
                    - Redirect HTTP(S) traffic to matching transparent web proxy policy.
                type: str
                choices:
                    - enable
                    - disable
            icap_profile:
                description:
                    - Name of an existing ICAP profile. Source icap.profile.name.
                type: str
            identity_based_route:
                description:
                    - Name of identity-based routing rule. Source firewall.identity-based-route.name.
                type: str
            inbound:
                description:
                    - 'Policy-based IPsec VPN: only traffic from the remote network can initiate a VPN.'
                type: str
                choices:
                    - enable
                    - disable
            inspection_mode:
                description:
                    - Policy inspection mode (Flow/proxy). Default is Flow mode.
                type: str
                choices:
                    - proxy
                    - flow
            internet_service:
                description:
                    - Enable/disable use of Internet Services for this policy. If enabled, destination address and service are not used.
                type: str
                choices:
                    - enable
                    - disable
            internet_service_custom:
                description:
                    - Custom Internet Service name.
                type: list
                suboptions:
                    name:
                        description:
                            - Custom Internet Service name. Source firewall.internet-service-custom.name.
                        required: true
                        type: str
            internet_service_custom_group:
                description:
                    - Custom Internet Service group name.
                type: list
                suboptions:
                    name:
                        description:
                            - Custom Internet Service group name. Source firewall.internet-service-custom-group.name.
                        required: true
                        type: str
            internet_service_group:
                description:
                    - Internet Service group name.
                type: list
                suboptions:
                    name:
                        description:
                            - Internet Service group name. Source firewall.internet-service-group.name.
                        required: true
                        type: str
            internet_service_name:
                description:
                    - Internet Service name.
                type: list
                suboptions:
                    name:
                        description:
                            - Internet Service name. Source firewall.internet-service-name.name.
                        required: true
                        type: str
            internet_service_negate:
                description:
                    - When enabled internet-service specifies what the service must NOT be.
                type: str
                choices:
                    - enable
                    - disable
            internet_service_src:
                description:
                    - Enable/disable use of Internet Services in source for this policy. If enabled, source address is not used.
                type: str
                choices:
                    - enable
                    - disable
            internet_service_src_custom:
                description:
                    - Custom Internet Service source name.
                type: list
                suboptions:
                    name:
                        description:
                            - Custom Internet Service name. Source firewall.internet-service-custom.name.
                        required: true
                        type: str
            internet_service_src_custom_group:
                description:
                    - Custom Internet Service source group name.
                type: list
                suboptions:
                    name:
                        description:
                            - Custom Internet Service group name. Source firewall.internet-service-custom-group.name.
                        required: true
                        type: str
            internet_service_src_group:
                description:
                    - Internet Service source group name.
                type: list
                suboptions:
                    name:
                        description:
                            - Internet Service group name. Source firewall.internet-service-group.name.
                        required: true
                        type: str
            internet_service_src_name:
                description:
                    - Internet Service source name.
                type: list
                suboptions:
                    name:
                        description:
                            - Internet Service name. Source firewall.internet-service-name.name.
                        required: true
                        type: str
            internet_service_src_negate:
                description:
                    - When enabled internet-service-src specifies what the service must NOT be.
                type: str
                choices:
                    - enable
                    - disable
            ippool:
                description:
                    - Enable to use IP Pools for source NAT.
                type: str
                choices:
                    - enable
                    - disable
            ips_sensor:
                description:
                    - Name of an existing IPS sensor. Source ips.sensor.name.
                type: str
            logtraffic:
                description:
                    - Enable or disable logging. Log all sessions or security profile sessions.
                type: str
                choices:
                    - all
                    - utm
                    - disable
            logtraffic_start:
                description:
                    - Record logs when a session starts.
                type: str
                choices:
                    - enable
                    - disable
            match_vip:
                description:
                    - Enable to match packets that have had their destination addresses changed by a VIP.
                type: str
                choices:
                    - enable
                    - disable
            match_vip_only:
                description:
                    - Enable/disable matching of only those packets that have had their destination addresses changed by a VIP.
                type: str
                choices:
                    - enable
                    - disable
            name:
                description:
                    - Policy name.
                type: str
            nat:
                description:
                    - Enable/disable source NAT.
                type: str
                choices:
                    - enable
                    - disable
            natinbound:
                description:
                    - 'Policy-based IPsec VPN: apply destination NAT to inbound traffic.'
                type: str
                choices:
                    - enable
                    - disable
            natip:
                description:
                    - 'Policy-based IPsec VPN: source NAT IP address for outgoing traffic.'
                type: str
            natoutbound:
                description:
                    - 'Policy-based IPsec VPN: apply source NAT to outbound traffic.'
                type: str
                choices:
                    - enable
                    - disable
            ntlm:
                description:
                    - Enable/disable NTLM authentication.
                type: str
                choices:
                    - enable
                    - disable
            ntlm_enabled_browsers:
                description:
                    - HTTP-User-Agent value of supported browsers.
                type: list
                suboptions:
                    user_agent_string:
                        description:
                            - User agent string.
                        type: str
            ntlm_guest:
                description:
                    - Enable/disable NTLM guest user access.
                type: str
                choices:
                    - enable
                    - disable
            outbound:
                description:
                    - 'Policy-based IPsec VPN: only traffic from the internal network can initiate a VPN.'
                type: str
                choices:
                    - enable
                    - disable
            per_ip_shaper:
                description:
                    - Per-IP traffic shaper. Source firewall.shaper.per-ip-shaper.name.
                type: str
            permit_any_host:
                description:
                    - Accept UDP packets from any host.
                type: str
                choices:
                    - enable
                    - disable
            permit_stun_host:
                description:
                    - Accept UDP packets from any Session Traversal Utilities for NAT (STUN) host.
                type: str
                choices:
                    - enable
                    - disable
            policyid:
                description:
                    - Policy ID (0 - 4294967294).
                required: true
                type: int
            poolname:
                description:
                    - IP Pool names.
                type: list
                suboptions:
                    name:
                        description:
                            - IP pool name. Source firewall.ippool.name.
                        required: true
                        type: str
            poolname6:
                description:
                    - IPv6 pool names.
                type: list
                suboptions:
                    name:
                        description:
                            - IPv6 pool name. Source firewall.ippool6.name.
                        required: true
                        type: str
            profile_group:
                description:
                    - Name of profile group. Source firewall.profile-group.name.
                type: str
            profile_protocol_options:
                description:
                    - Name of an existing Protocol options profile. Source firewall.profile-protocol-options.name.
                type: str
            profile_type:
                description:
                    - Determine whether the firewall policy allows security profile groups or single profiles only.
                type: str
                choices:
                    - single
                    - group
            radius_mac_auth_bypass:
                description:
                    - Enable MAC authentication bypass. The bypassed MAC address must be received from RADIUS server.
                type: str
                choices:
                    - enable
                    - disable
            redirect_url:
                description:
                    - URL users are directed to after seeing and accepting the disclaimer or authenticating.
                type: str
            replacemsg_override_group:
                description:
                    - Override the default replacement message group for this policy. Source system.replacemsg-group.name.
                type: str
            reputation_direction:
                description:
                    - Direction of the initial traffic for reputation to take effect.
                type: str
                choices:
                    - source
                    - destination
            reputation_minimum:
                description:
                    - Minimum Reputation to take action. Source firewall.internet-service-reputation.id.
                type: int
            rtp_addr:
                description:
                    - Address names if this is an RTP NAT policy.
                type: list
                suboptions:
                    name:
                        description:
                            - Address name. Source firewall.internet-service-custom-group.name firewall.addrgrp.name.
                        required: true
                        type: str
            rtp_nat:
                description:
                    - Enable Real Time Protocol (RTP) NAT.
                type: str
                choices:
                    - disable
                    - enable
            schedule:
                description:
                    - Schedule name. Source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name.
                type: str
            schedule_timeout:
                description:
                    - Enable to force current sessions to end when the schedule object times out. Disable allows them to end from inactivity.
                type: str
                choices:
                    - enable
                    - disable
            send_deny_packet:
                description:
                    - Enable to send a reply when a session is denied or blocked by a firewall policy.
                type: str
                choices:
                    - disable
                    - enable
            service:
                description:
                    - Service and service group names.
                type: list
                suboptions:
                    name:
                        description:
                            - Service and service group names. Source firewall.service.custom.name firewall.service.group.name.
                        required: true
                        type: str
            service_negate:
                description:
                    - When enabled service specifies what the service must NOT be.
                type: str
                choices:
                    - enable
                    - disable
            session_ttl:
                description:
                    - TTL in seconds for sessions accepted by this policy (0 means use the system ).
                type: str
            src_vendor_mac:
                description:
                    - Vendor MAC source ID.
                type: list
                suboptions:
                    id:
                        description:
                            - Vendor MAC ID. Source firewall.vendor-mac.id.
                        required: true
                        type: int
            srcaddr:
                description:
                    - Source IPv4 address and address group names.
                type: list
                suboptions:
                    name:
                        description:
                            - Address name. Source firewall.address.name firewall.addrgrp.name system.external-resource.name.
                        required: true
                        type: str
            srcaddr_negate:
                description:
                    - When enabled srcaddr/srcaddr6 specifies what the source address must NOT be.
                type: str
                choices:
                    - enable
                    - disable
            srcaddr6:
                description:
                    - Source IPv6 address name and address group names.
                type: list
                suboptions:
                    name:
                        description:
                            - Address name. Source firewall.address6.name firewall.addrgrp6.name system.external-resource.name.
                        required: true
                        type: str
            srcintf:
                description:
                    - Incoming (ingress) interface.
                type: list
                suboptions:
                    name:
                        description:
                            - Interface name. Source system.interface.name system.zone.name.
                        required: true
                        type: str
            ssh_filter_profile:
                description:
                    - Name of an existing SSH filter profile. Source ssh-filter.profile.name.
                type: str
            ssh_policy_redirect:
                description:
                    - Redirect SSH traffic to matching transparent proxy policy.
                type: str
                choices:
                    - enable
                    - disable
            ssl_ssh_profile:
                description:
                    - Name of an existing SSL SSH profile. Source firewall.ssl-ssh-profile.name.
                type: str
            status:
                description:
                    - Enable or disable this policy.
                type: str
                choices:
                    - enable
                    - disable
            tcp_mss_receiver:
                description:
                    - Receiver TCP maximum segment size (MSS).
                type: int
            tcp_mss_sender:
                description:
                    - Sender TCP maximum segment size (MSS).
                type: int
            tcp_session_without_syn:
                description:
                    - Enable/disable creation of TCP session without SYN flag.
                type: str
                choices:
                    - all
                    - data-only
                    - disable
            timeout_send_rst:
                description:
                    - Enable/disable sending RST packets when TCP sessions expire.
                type: str
                choices:
                    - enable
                    - disable
            tos:
                description:
                    - ToS (Type of Service) value used for comparison.
                type: str
            tos_mask:
                description:
                    - Non-zero bit positions are used for comparison while zero bit positions are ignored.
                type: str
            tos_negate:
                description:
                    - Enable negated TOS match.
                type: str
                choices:
                    - enable
                    - disable
            traffic_shaper:
                description:
                    - Traffic shaper. Source firewall.shaper.traffic-shaper.name.
                type: str
            traffic_shaper_reverse:
                description:
                    - Reverse traffic shaper. Source firewall.shaper.traffic-shaper.name.
                type: str
            url_category:
                description:
                    - URL category ID list.
                type: list
                suboptions:
                    id:
                        description:
                            - URL category ID.
                        required: true
                        type: int
            users:
                description:
                    - Names of individual users that can authenticate with this policy.
                type: list
                suboptions:
                    name:
                        description:
                            - Names of individual users that can authenticate with this policy. Source user.local.name.
                        required: true
                        type: str
            utm_status:
                description:
                    - Enable to add one or more security profiles (AV, IPS, etc.) to the firewall policy.
                type: str
                choices:
                    - enable
                    - disable
            uuid:
                description:
                    - Universally Unique Identifier (UUID; automatically assigned but can be manually reset).
                type: str
            vlan_cos_fwd:
                description:
                    - 'VLAN forward direction user priority: 255 passthrough, 0 lowest, 7 highest.'
                type: int
            vlan_cos_rev:
                description:
                    - 'VLAN reverse direction user priority: 255 passthrough, 0 lowest, 7 highest.'
                type: int
            vlan_filter:
                description:
                    - Set VLAN filters.
                type: str
            voip_profile:
                description:
                    - Name of an existing VoIP profile. Source voip.profile.name.
                type: str
            vpntunnel:
                description:
                    - 'Policy-based IPsec VPN: name of the IPsec VPN Phase 1. Source vpn.ipsec.phase1.name vpn.ipsec.manualkey.name.'
                type: str
            waf_profile:
                description:
                    - Name of an existing Web application firewall profile. Source waf.profile.name.
                type: str
            wanopt:
                description:
                    - Enable/disable WAN optimization.
                type: str
                choices:
                    - enable
                    - disable
            wanopt_detection:
                description:
                    - WAN optimization auto-detection mode.
                type: str
                choices:
                    - active
                    - passive
                    - off
            wanopt_passive_opt:
                description:
                    - WAN optimization passive mode options. This option decides what IP address will be used to connect server.
                type: str
                choices:
                    - default
                    - transparent
                    - non-transparent
            wanopt_peer:
                description:
                    - WAN optimization peer. Source wanopt.peer.peer-host-id.
                type: str
            wanopt_profile:
                description:
                    - WAN optimization profile. Source wanopt.profile.name.
                type: str
            wccp:
                description:
                    - Enable/disable forwarding traffic matching this policy to a configured WCCP server.
                type: str
                choices:
                    - enable
                    - disable
            webcache:
                description:
                    - Enable/disable web cache.
                type: str
                choices:
                    - enable
                    - disable
            webcache_https:
                description:
                    - Enable/disable web cache for HTTPS.
                type: str
                choices:
                    - disable
                    - enable
            webfilter_profile:
                description:
                    - Name of an existing Web filter profile. Source webfilter.profile.name.
                type: str
            webproxy_forward_server:
                description:
                    - Webproxy forward server name. Source web-proxy.forward-server.name web-proxy.forward-server-group.name.
                type: str
            webproxy_profile:
                description:
                    - Webproxy profile name. Source web-proxy.profile.name.
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
  - name: Configure IPv4/IPv6 policies.
    fortios_firewall_policy:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_policy:
        action: "accept"
        anti_replay: "enable"
        app_category:
         -
            id:  "6"
        app_group:
         -
            name: "default_name_8"
        application:
         -
            id:  "10"
        application_list: "<your_own_value> (source application.list.name)"
        auth_cert: "<your_own_value> (source vpn.certificate.local.name)"
        auth_path: "enable"
        auth_redirect_addr: "<your_own_value>"
        auto_asic_offload: "enable"
        av_profile: "<your_own_value> (source antivirus.profile.name)"
        block_notification: "enable"
        captive_portal_exempt: "enable"
        capture_packet: "enable"
        cifs_profile: "<your_own_value> (source cifs.profile.name)"
        comments: "<your_own_value>"
        custom_log_fields:
         -
            field_id: "<your_own_value> (source log.custom-field.id)"
        decrypted_traffic_mirror: "<your_own_value> (source firewall.decrypted-traffic-mirror.name)"
        delay_tcp_npu_session: "enable"
        diffserv_forward: "enable"
        diffserv_reverse: "enable"
        diffservcode_forward: "<your_own_value>"
        diffservcode_rev: "<your_own_value>"
        disclaimer: "enable"
        dlp_sensor: "<your_own_value> (source dlp.sensor.name)"
        dnsfilter_profile: "<your_own_value> (source dnsfilter.profile.name)"
        dsri: "enable"
        dstaddr:
         -
            name: "default_name_35 (source firewall.address.name firewall.addrgrp.name firewall.vip.name firewall.vipgrp.name system.external-resource.name)"
        dstaddr_negate: "enable"
        dstaddr6:
         -
            name: "default_name_38 (source firewall.address6.name firewall.addrgrp6.name firewall.vipgrp6.name firewall.vip6.name system.external-resource
              .name)"
        dstintf:
         -
            name: "default_name_40 (source system.interface.name system.zone.name)"
        email_collect: "enable"
        emailfilter_profile: "<your_own_value> (source emailfilter.profile.name)"
        firewall_session_dirty: "check-all"
        fixedport: "enable"
        fsso_agent_for_ntlm: "<your_own_value> (source user.fsso.name)"
        fsso_groups:
         -
            name: "default_name_47 (source user.adgrp.name)"
        geoip_anycast: "enable"
        geoip_match: "physical-location"
        groups:
         -
            name: "default_name_51 (source user.group.name)"
        http_policy_redirect: "enable"
        icap_profile: "<your_own_value> (source icap.profile.name)"
        identity_based_route: "<your_own_value> (source firewall.identity-based-route.name)"
        inbound: "enable"
        inspection_mode: "proxy"
        internet_service: "enable"
        internet_service_custom:
         -
            name: "default_name_59 (source firewall.internet-service-custom.name)"
        internet_service_custom_group:
         -
            name: "default_name_61 (source firewall.internet-service-custom-group.name)"
        internet_service_group:
         -
            name: "default_name_63 (source firewall.internet-service-group.name)"
        internet_service_name:
         -
            name: "default_name_65 (source firewall.internet-service-name.name)"
        internet_service_negate: "enable"
        internet_service_src: "enable"
        internet_service_src_custom:
         -
            name: "default_name_69 (source firewall.internet-service-custom.name)"
        internet_service_src_custom_group:
         -
            name: "default_name_71 (source firewall.internet-service-custom-group.name)"
        internet_service_src_group:
         -
            name: "default_name_73 (source firewall.internet-service-group.name)"
        internet_service_src_name:
         -
            name: "default_name_75 (source firewall.internet-service-name.name)"
        internet_service_src_negate: "enable"
        ippool: "enable"
        ips_sensor: "<your_own_value> (source ips.sensor.name)"
        logtraffic: "all"
        logtraffic_start: "enable"
        match_vip: "enable"
        match_vip_only: "enable"
        name: "default_name_83"
        nat: "enable"
        natinbound: "enable"
        natip: "<your_own_value>"
        natoutbound: "enable"
        ntlm: "enable"
        ntlm_enabled_browsers:
         -
            user_agent_string: "<your_own_value>"
        ntlm_guest: "enable"
        outbound: "enable"
        per_ip_shaper: "<your_own_value> (source firewall.shaper.per-ip-shaper.name)"
        permit_any_host: "enable"
        permit_stun_host: "enable"
        policyid: "96"
        poolname:
         -
            name: "default_name_98 (source firewall.ippool.name)"
        poolname6:
         -
            name: "default_name_100 (source firewall.ippool6.name)"
        profile_group: "<your_own_value> (source firewall.profile-group.name)"
        profile_protocol_options: "<your_own_value> (source firewall.profile-protocol-options.name)"
        profile_type: "single"
        radius_mac_auth_bypass: "enable"
        redirect_url: "<your_own_value>"
        replacemsg_override_group: "<your_own_value> (source system.replacemsg-group.name)"
        reputation_direction: "source"
        reputation_minimum: "108 (source firewall.internet-service-reputation.id)"
        rtp_addr:
         -
            name: "default_name_110 (source firewall.internet-service-custom-group.name firewall.addrgrp.name)"
        rtp_nat: "disable"
        schedule: "<your_own_value> (source firewall.schedule.onetime.name firewall.schedule.recurring.name firewall.schedule.group.name)"
        schedule_timeout: "enable"
        send_deny_packet: "disable"
        service:
         -
            name: "default_name_116 (source firewall.service.custom.name firewall.service.group.name)"
        service_negate: "enable"
        session_ttl: "<your_own_value>"
        src_vendor_mac:
         -
            id:  "120 (source firewall.vendor-mac.id)"
        srcaddr:
         -
            name: "default_name_122 (source firewall.address.name firewall.addrgrp.name system.external-resource.name)"
        srcaddr_negate: "enable"
        srcaddr6:
         -
            name: "default_name_125 (source firewall.address6.name firewall.addrgrp6.name system.external-resource.name)"
        srcintf:
         -
            name: "default_name_127 (source system.interface.name system.zone.name)"
        ssh_filter_profile: "<your_own_value> (source ssh-filter.profile.name)"
        ssh_policy_redirect: "enable"
        ssl_ssh_profile: "<your_own_value> (source firewall.ssl-ssh-profile.name)"
        status: "enable"
        tcp_mss_receiver: "132"
        tcp_mss_sender: "133"
        tcp_session_without_syn: "all"
        timeout_send_rst: "enable"
        tos: "<your_own_value>"
        tos_mask: "<your_own_value>"
        tos_negate: "enable"
        traffic_shaper: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
        traffic_shaper_reverse: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
        url_category:
         -
            id:  "142"
        users:
         -
            name: "default_name_144 (source user.local.name)"
        utm_status: "enable"
        uuid: "<your_own_value>"
        vlan_cos_fwd: "147"
        vlan_cos_rev: "148"
        vlan_filter: "<your_own_value>"
        voip_profile: "<your_own_value> (source voip.profile.name)"
        vpntunnel: "<your_own_value> (source vpn.ipsec.phase1.name vpn.ipsec.manualkey.name)"
        waf_profile: "<your_own_value> (source waf.profile.name)"
        wanopt: "enable"
        wanopt_detection: "active"
        wanopt_passive_opt: "default"
        wanopt_peer: "<your_own_value> (source wanopt.peer.peer-host-id)"
        wanopt_profile: "<your_own_value> (source wanopt.profile.name)"
        wccp: "enable"
        webcache: "enable"
        webcache_https: "disable"
        webfilter_profile: "<your_own_value> (source webfilter.profile.name)"
        webproxy_forward_server: "<your_own_value> (source web-proxy.forward-server.name web-proxy.forward-server-group.name)"
        webproxy_profile: "<your_own_value> (source web-proxy.profile.name)"

  - name: move firewall.policy
    fortios_firewall_policy:
      vdom:  "root"
      action: "move"
      self: "<mkey of self identifier>"
      after: "<mkey of target identifier>"
     #before: "<mkey of target identifier>"

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


def filter_firewall_policy_data(json):
    option_list = ['action', 'anti_replay', 'app_category',
                   'app_group', 'application', 'application_list',
                   'auth_cert', 'auth_path', 'auth_redirect_addr',
                   'auto_asic_offload', 'av_profile', 'block_notification',
                   'captive_portal_exempt', 'capture_packet', 'cifs_profile',
                   'comments', 'custom_log_fields', 'decrypted_traffic_mirror',
                   'delay_tcp_npu_session', 'diffserv_forward', 'diffserv_reverse',
                   'diffservcode_forward', 'diffservcode_rev', 'disclaimer',
                   'dlp_sensor', 'dnsfilter_profile', 'dsri',
                   'dstaddr', 'dstaddr_negate', 'dstaddr6',
                   'dstintf', 'email_collect', 'emailfilter_profile',
                   'firewall_session_dirty', 'fixedport', 'fsso_agent_for_ntlm',
                   'fsso_groups', 'geoip_anycast', 'geoip_match',
                   'groups', 'http_policy_redirect', 'icap_profile',
                   'identity_based_route', 'inbound', 'inspection_mode',
                   'internet_service', 'internet_service_custom', 'internet_service_custom_group',
                   'internet_service_group', 'internet_service_name', 'internet_service_negate',
                   'internet_service_src', 'internet_service_src_custom', 'internet_service_src_custom_group',
                   'internet_service_src_group', 'internet_service_src_name', 'internet_service_src_negate',
                   'ippool', 'ips_sensor', 'logtraffic',
                   'logtraffic_start', 'match_vip', 'match_vip_only',
                   'name', 'nat', 'natinbound',
                   'natip', 'natoutbound', 'ntlm',
                   'ntlm_enabled_browsers', 'ntlm_guest', 'outbound',
                   'per_ip_shaper', 'permit_any_host', 'permit_stun_host',
                   'policyid', 'poolname', 'poolname6',
                   'profile_group', 'profile_protocol_options', 'profile_type',
                   'radius_mac_auth_bypass', 'redirect_url', 'replacemsg_override_group',
                   'reputation_direction', 'reputation_minimum', 'rtp_addr',
                   'rtp_nat', 'schedule', 'schedule_timeout',
                   'send_deny_packet', 'service', 'service_negate',
                   'session_ttl', 'src_vendor_mac', 'srcaddr',
                   'srcaddr_negate', 'srcaddr6', 'srcintf',
                   'ssh_filter_profile', 'ssh_policy_redirect', 'ssl_ssh_profile',
                   'status', 'tcp_mss_receiver', 'tcp_mss_sender',
                   'tcp_session_without_syn', 'timeout_send_rst', 'tos',
                   'tos_mask', 'tos_negate', 'traffic_shaper',
                   'traffic_shaper_reverse', 'url_category', 'users',
                   'utm_status', 'uuid', 'vlan_cos_fwd',
                   'vlan_cos_rev', 'vlan_filter', 'voip_profile',
                   'vpntunnel', 'waf_profile', 'wanopt',
                   'wanopt_detection', 'wanopt_passive_opt', 'wanopt_peer',
                   'wanopt_profile', 'wccp', 'webcache',
                   'webcache_https', 'webfilter_profile', 'webproxy_forward_server',
                   'webproxy_profile']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


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


def firewall_policy(data, fos):
    vdom = data['vdom']
    if 'state' in data and data['state']:
        state = data['state']
    elif 'state' in data['firewall_policy'] and data['firewall_policy']['state']:
        state = data['firewall_policy']['state']
    else:
        state = True
    firewall_policy_data = data['firewall_policy']
    filtered_data = underscore_to_hyphen(filter_firewall_policy_data(firewall_policy_data))

    if state == "present":
        return fos.set('firewall',
                       'policy',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('firewall',
                          'policy',
                          mkey=filtered_data['policyid'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def move_fortios_firewall(data, fos):
    if not data['self'] or (not data['after'] and not data['before']):
        fos._module.fail_json(msg='self, after(or before) must not be empty')
    vdom = data['vdom']
    params_set = dict()
    params_set['action'] = 'move'
    if data['after']:
        params_set['after'] = data['after']
    if data['before']:
        params_set['before'] = data['before']
    return fos.set('firewall',
                   'policy',
                   data=None,
                   mkey=data['self'],
                   vdom=vdom,
                   parameters=params_set)


def fortios_firewall(data, fos):

    if data['action'] == 'move':
        resp = move_fortios_firewall(data, fos)
    elif data['firewall_policy']:
        resp = firewall_policy(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('firewall_policy'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = 'policyid'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "action": {"type": "str", "required": False, "choices": ["move"]},
        "self": {"type": "str", "required": False},
        "before": {"type": "str", "required": False},
        "after": {"type": "str", "required": False},
        "state": {"required": False, "type": "str",
                  "choices": ["present", "absent"]},
        "firewall_policy": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "state": {"required": False, "type": "str",
                          "choices": ["present", "absent"]},
                "action": {"required": False, "type": "str",
                           "choices": ["accept",
                                       "deny",
                                       "ipsec"]},
                "anti_replay": {"required": False, "type": "str",
                                "choices": ["enable",
                                            "disable"]},
                "app_category": {"required": False, "type": "list",
                                 "options": {
                                     "id": {"required": True, "type": "int"}
                                 }},
                "app_group": {"required": False, "type": "list",
                              "options": {
                                  "name": {"required": True, "type": "str"}
                              }},
                "application": {"required": False, "type": "list",
                                "options": {
                                    "id": {"required": True, "type": "int"}
                                }},
                "application_list": {"required": False, "type": "str"},
                "auth_cert": {"required": False, "type": "str"},
                "auth_path": {"required": False, "type": "str",
                              "choices": ["enable",
                                          "disable"]},
                "auth_redirect_addr": {"required": False, "type": "str"},
                "auto_asic_offload": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable"]},
                "av_profile": {"required": False, "type": "str"},
                "block_notification": {"required": False, "type": "str",
                                       "choices": ["enable",
                                                   "disable"]},
                "captive_portal_exempt": {"required": False, "type": "str",
                                          "choices": ["enable",
                                                      "disable"]},
                "capture_packet": {"required": False, "type": "str",
                                   "choices": ["enable",
                                               "disable"]},
                "cifs_profile": {"required": False, "type": "str"},
                "comments": {"required": False, "type": "str"},
                "custom_log_fields": {"required": False, "type": "list",
                                      "options": {
                                          "field_id": {"required": False, "type": "str"}
                                      }},
                "decrypted_traffic_mirror": {"required": False, "type": "str"},
                "delay_tcp_npu_session": {"required": False, "type": "str",
                                          "choices": ["enable",
                                                      "disable"]},
                "diffserv_forward": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "diffserv_reverse": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "diffservcode_forward": {"required": False, "type": "str"},
                "diffservcode_rev": {"required": False, "type": "str"},
                "disclaimer": {"required": False, "type": "str",
                               "choices": ["enable",
                                           "disable"]},
                "dlp_sensor": {"required": False, "type": "str"},
                "dnsfilter_profile": {"required": False, "type": "str"},
                "dsri": {"required": False, "type": "str",
                         "choices": ["enable",
                                     "disable"]},
                "dstaddr": {"required": False, "type": "list",
                            "options": {
                                "name": {"required": True, "type": "str"}
                            }},
                "dstaddr_negate": {"required": False, "type": "str",
                                   "choices": ["enable",
                                               "disable"]},
                "dstaddr6": {"required": False, "type": "list",
                             "options": {
                                 "name": {"required": True, "type": "str"}
                             }},
                "dstintf": {"required": False, "type": "list",
                            "options": {
                                "name": {"required": True, "type": "str"}
                            }},
                "email_collect": {"required": False, "type": "str",
                                  "choices": ["enable",
                                              "disable"]},
                "emailfilter_profile": {"required": False, "type": "str"},
                "firewall_session_dirty": {"required": False, "type": "str",
                                           "choices": ["check-all",
                                                       "check-new"]},
                "fixedport": {"required": False, "type": "str",
                              "choices": ["enable",
                                          "disable"]},
                "fsso_agent_for_ntlm": {"required": False, "type": "str"},
                "fsso_groups": {"required": False, "type": "list",
                                "options": {
                                    "name": {"required": True, "type": "str"}
                                }},
                "geoip_anycast": {"required": False, "type": "str",
                                  "choices": ["enable",
                                              "disable"]},
                "geoip_match": {"required": False, "type": "str",
                                "choices": ["physical-location",
                                            "registered-location"]},
                "groups": {"required": False, "type": "list",
                           "options": {
                               "name": {"required": True, "type": "str"}
                           }},
                "http_policy_redirect": {"required": False, "type": "str",
                                         "choices": ["enable",
                                                     "disable"]},
                "icap_profile": {"required": False, "type": "str"},
                "identity_based_route": {"required": False, "type": "str"},
                "inbound": {"required": False, "type": "str",
                            "choices": ["enable",
                                        "disable"]},
                "inspection_mode": {"required": False, "type": "str",
                                    "choices": ["proxy",
                                                "flow"]},
                "internet_service": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "internet_service_custom": {"required": False, "type": "list",
                                            "options": {
                                                "name": {"required": True, "type": "str"}
                                            }},
                "internet_service_custom_group": {"required": False, "type": "list",
                                                  "options": {
                                                      "name": {"required": True, "type": "str"}
                                                  }},
                "internet_service_group": {"required": False, "type": "list",
                                           "options": {
                                               "name": {"required": True, "type": "str"}
                                           }},
                "internet_service_name": {"required": False, "type": "list",
                                          "options": {
                                              "name": {"required": True, "type": "str"}
                                          }},
                "internet_service_negate": {"required": False, "type": "str",
                                            "choices": ["enable",
                                                        "disable"]},
                "internet_service_src": {"required": False, "type": "str",
                                         "choices": ["enable",
                                                     "disable"]},
                "internet_service_src_custom": {"required": False, "type": "list",
                                                "options": {
                                                    "name": {"required": True, "type": "str"}
                                                }},
                "internet_service_src_custom_group": {"required": False, "type": "list",
                                                      "options": {
                                                          "name": {"required": True, "type": "str"}
                                                      }},
                "internet_service_src_group": {"required": False, "type": "list",
                                               "options": {
                                                   "name": {"required": True, "type": "str"}
                                               }},
                "internet_service_src_name": {"required": False, "type": "list",
                                              "options": {
                                                  "name": {"required": True, "type": "str"}
                                              }},
                "internet_service_src_negate": {"required": False, "type": "str",
                                                "choices": ["enable",
                                                            "disable"]},
                "ippool": {"required": False, "type": "str",
                           "choices": ["enable",
                                       "disable"]},
                "ips_sensor": {"required": False, "type": "str"},
                "logtraffic": {"required": False, "type": "str",
                               "choices": ["all",
                                           "utm",
                                           "disable"]},
                "logtraffic_start": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "match_vip": {"required": False, "type": "str",
                              "choices": ["enable",
                                          "disable"]},
                "match_vip_only": {"required": False, "type": "str",
                                   "choices": ["enable",
                                               "disable"]},
                "name": {"required": False, "type": "str"},
                "nat": {"required": False, "type": "str",
                        "choices": ["enable",
                                    "disable"]},
                "natinbound": {"required": False, "type": "str",
                               "choices": ["enable",
                                           "disable"]},
                "natip": {"required": False, "type": "str"},
                "natoutbound": {"required": False, "type": "str",
                                "choices": ["enable",
                                            "disable"]},
                "ntlm": {"required": False, "type": "str",
                         "choices": ["enable",
                                     "disable"]},
                "ntlm_enabled_browsers": {"required": False, "type": "list",
                                          "options": {
                                              "user_agent_string": {"required": False, "type": "str"}
                                          }},
                "ntlm_guest": {"required": False, "type": "str",
                               "choices": ["enable",
                                           "disable"]},
                "outbound": {"required": False, "type": "str",
                             "choices": ["enable",
                                         "disable"]},
                "per_ip_shaper": {"required": False, "type": "str"},
                "permit_any_host": {"required": False, "type": "str",
                                    "choices": ["enable",
                                                "disable"]},
                "permit_stun_host": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "policyid": {"required": True, "type": "int"},
                "poolname": {"required": False, "type": "list",
                             "options": {
                                 "name": {"required": True, "type": "str"}
                             }},
                "poolname6": {"required": False, "type": "list",
                              "options": {
                                  "name": {"required": True, "type": "str"}
                              }},
                "profile_group": {"required": False, "type": "str"},
                "profile_protocol_options": {"required": False, "type": "str"},
                "profile_type": {"required": False, "type": "str",
                                 "choices": ["single",
                                             "group"]},
                "radius_mac_auth_bypass": {"required": False, "type": "str",
                                           "choices": ["enable",
                                                       "disable"]},
                "redirect_url": {"required": False, "type": "str"},
                "replacemsg_override_group": {"required": False, "type": "str"},
                "reputation_direction": {"required": False, "type": "str",
                                         "choices": ["source",
                                                     "destination"]},
                "reputation_minimum": {"required": False, "type": "int"},
                "rtp_addr": {"required": False, "type": "list",
                             "options": {
                                 "name": {"required": True, "type": "str"}
                             }},
                "rtp_nat": {"required": False, "type": "str",
                            "choices": ["disable",
                                        "enable"]},
                "schedule": {"required": False, "type": "str"},
                "schedule_timeout": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "send_deny_packet": {"required": False, "type": "str",
                                     "choices": ["disable",
                                                 "enable"]},
                "service": {"required": False, "type": "list",
                            "options": {
                                "name": {"required": True, "type": "str"}
                            }},
                "service_negate": {"required": False, "type": "str",
                                   "choices": ["enable",
                                               "disable"]},
                "session_ttl": {"required": False, "type": "str"},
                "src_vendor_mac": {"required": False, "type": "list",
                                   "options": {
                                       "id": {"required": True, "type": "int"}
                                   }},
                "srcaddr": {"required": False, "type": "list",
                            "options": {
                                "name": {"required": True, "type": "str"}
                            }},
                "srcaddr_negate": {"required": False, "type": "str",
                                   "choices": ["enable",
                                               "disable"]},
                "srcaddr6": {"required": False, "type": "list",
                             "options": {
                                 "name": {"required": True, "type": "str"}
                             }},
                "srcintf": {"required": False, "type": "list",
                            "options": {
                                "name": {"required": True, "type": "str"}
                            }},
                "ssh_filter_profile": {"required": False, "type": "str"},
                "ssh_policy_redirect": {"required": False, "type": "str",
                                        "choices": ["enable",
                                                    "disable"]},
                "ssl_ssh_profile": {"required": False, "type": "str"},
                "status": {"required": False, "type": "str",
                           "choices": ["enable",
                                       "disable"]},
                "tcp_mss_receiver": {"required": False, "type": "int"},
                "tcp_mss_sender": {"required": False, "type": "int"},
                "tcp_session_without_syn": {"required": False, "type": "str",
                                            "choices": ["all",
                                                        "data-only",
                                                        "disable"]},
                "timeout_send_rst": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "tos": {"required": False, "type": "str"},
                "tos_mask": {"required": False, "type": "str"},
                "tos_negate": {"required": False, "type": "str",
                               "choices": ["enable",
                                           "disable"]},
                "traffic_shaper": {"required": False, "type": "str"},
                "traffic_shaper_reverse": {"required": False, "type": "str"},
                "url_category": {"required": False, "type": "list",
                                 "options": {
                                     "id": {"required": True, "type": "int"}
                                 }},
                "users": {"required": False, "type": "list",
                          "options": {
                              "name": {"required": True, "type": "str"}
                          }},
                "utm_status": {"required": False, "type": "str",
                               "choices": ["enable",
                                           "disable"]},
                "uuid": {"required": False, "type": "str"},
                "vlan_cos_fwd": {"required": False, "type": "int"},
                "vlan_cos_rev": {"required": False, "type": "int"},
                "vlan_filter": {"required": False, "type": "str"},
                "voip_profile": {"required": False, "type": "str"},
                "vpntunnel": {"required": False, "type": "str"},
                "waf_profile": {"required": False, "type": "str"},
                "wanopt": {"required": False, "type": "str",
                           "choices": ["enable",
                                       "disable"]},
                "wanopt_detection": {"required": False, "type": "str",
                                     "choices": ["active",
                                                 "passive",
                                                 "off"]},
                "wanopt_passive_opt": {"required": False, "type": "str",
                                       "choices": ["default",
                                                   "transparent",
                                                   "non-transparent"]},
                "wanopt_peer": {"required": False, "type": "str"},
                "wanopt_profile": {"required": False, "type": "str"},
                "wccp": {"required": False, "type": "str",
                         "choices": ["enable",
                                     "disable"]},
                "webcache": {"required": False, "type": "str",
                             "choices": ["enable",
                                         "disable"]},
                "webcache_https": {"required": False, "type": "str",
                                   "choices": ["disable",
                                               "enable"]},
                "webfilter_profile": {"required": False, "type": "str"},
                "webproxy_forward_server": {"required": False, "type": "str"},
                "webproxy_profile": {"required": False, "type": "str"}

            }
        }
    }

    check_legacy_fortiosapi()
    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if 'access_token' in module.params:
            connection.set_option('access_token', module.params['access_token'])

        fos = FortiOSHandler(connection, module, mkeyname)

        is_error, has_changed, result = fortios_firewall(module.params, fos)
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
