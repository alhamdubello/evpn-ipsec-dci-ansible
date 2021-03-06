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
module: fortios_system_global
short_description: Configure global attributes in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify system feature and global category.
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

    system_global:
        description:
            - Configure global attributes.
        default: null
        type: dict
        suboptions:
            admin_concurrent:
                description:
                    - Enable/disable concurrent administrator logins. (Use policy-auth-concurrent for firewall authenticated users.)
                type: str
                choices:
                    - enable
                    - disable
            admin_console_timeout:
                description:
                    - Console login timeout that overrides the admintimeout value. (15 - 300 seconds) (15 seconds to 5 minutes). 0 the default, disables this
                       timeout.
                type: int
            admin_hsts_max_age:
                description:
                    - HTTPS Strict-Transport-Security header max-age in seconds. A value of 0 will reset any HSTS records in the browser.When
                       admin-https-redirect is disabled the header max-age will be 0.
                type: int
            admin_https_pki_required:
                description:
                    - Enable/disable admin login method. Enable to force administrators to provide a valid certificate to log in if PKI is enabled. Disable to
                       allow administrators to log in with a certificate or password.
                type: str
                choices:
                    - enable
                    - disable
            admin_https_redirect:
                description:
                    - Enable/disable redirection of HTTP administration access to HTTPS.
                type: str
                choices:
                    - enable
                    - disable
            admin_https_ssl_versions:
                description:
                    - Allowed TLS versions for web administration.
                type: list
                choices:
                    - tlsv1-1
                    - tlsv1-2
                    - tlsv1-3
            admin_lockout_duration:
                description:
                    - Amount of time in seconds that an administrator account is locked out after reaching the admin-lockout-threshold for repeated failed
                       login attempts.
                type: int
            admin_lockout_threshold:
                description:
                    - Number of failed login attempts before an administrator account is locked out for the admin-lockout-duration.
                type: int
            admin_login_max:
                description:
                    - Maximum number of administrators who can be logged in at the same time (1 - 100)
                type: int
            admin_maintainer:
                description:
                    - Enable/disable maintainer administrator login. When enabled, the maintainer account can be used to log in from the console after a hard
                       reboot. The password is "bcpb" followed by the FortiGate unit serial number. You have limited time to complete this login.
                type: str
                choices:
                    - enable
                    - disable
            admin_port:
                description:
                    - Administrative access port for HTTP. (1 - 65535).
                type: int
            admin_restrict_local:
                description:
                    - Enable/disable local admin authentication restriction when remote authenticator is up and running.
                type: str
                choices:
                    - enable
                    - disable
            admin_scp:
                description:
                    - Enable/disable using SCP to download the system configuration. You can use SCP as an alternative method for backing up the configuration.
                type: str
                choices:
                    - enable
                    - disable
            admin_server_cert:
                description:
                    - Server certificate that the FortiGate uses for HTTPS administrative connections. Source certificate.local.name.
                type: str
            admin_sport:
                description:
                    - Administrative access port for HTTPS. (1 - 65535).
                type: int
            admin_ssh_grace_time:
                description:
                    - Maximum time in seconds permitted between making an SSH connection to the FortiGate unit and authenticating (10 - 3600 sec (1 hour)).
                type: int
            admin_ssh_password:
                description:
                    - Enable/disable password authentication for SSH admin access.
                type: str
                choices:
                    - enable
                    - disable
            admin_ssh_port:
                description:
                    - Administrative access port for SSH. (1 - 65535).
                type: int
            admin_ssh_v1:
                description:
                    - Enable/disable SSH v1 compatibility.
                type: str
                choices:
                    - enable
                    - disable
            admin_telnet:
                description:
                    - Enable/disable TELNET service.
                type: str
                choices:
                    - enable
                    - disable
            admin_telnet_port:
                description:
                    - Administrative access port for TELNET. (1 - 65535).
                type: int
            admintimeout:
                description:
                    - Number of minutes before an idle administrator session times out (1 - 480 minutes (8 hours)). A shorter idle timeout is more secure.
                type: int
            alias:
                description:
                    - Alias for your FortiGate unit.
                type: str
            allow_traffic_redirect:
                description:
                    - Disable to allow traffic to be routed back on a different interface.
                type: str
                choices:
                    - enable
                    - disable
            anti_replay:
                description:
                    - Level of checking for packet replay and TCP sequence checking.
                type: str
                choices:
                    - disable
                    - loose
                    - strict
            arp_max_entry:
                description:
                    - Maximum number of dynamically learned MAC addresses that can be added to the ARP table (131072 - 2147483647).
                type: int
            auth_cert:
                description:
                    - Server certificate that the FortiGate uses for HTTPS firewall authentication connections. Source certificate.local.name.
                type: str
            auth_http_port:
                description:
                    - User authentication HTTP port. (1 - 65535).
                type: int
            auth_https_port:
                description:
                    - User authentication HTTPS port. (1 - 65535).
                type: int
            auth_keepalive:
                description:
                    - Enable to prevent user authentication sessions from timing out when idle.
                type: str
                choices:
                    - enable
                    - disable
            auth_session_limit:
                description:
                    - Action to take when the number of allowed user authenticated sessions is reached.
                type: str
                choices:
                    - block-new
                    - logout-inactive
            auto_auth_extension_device:
                description:
                    - Enable/disable automatic authorization of dedicated Fortinet extension devices.
                type: str
                choices:
                    - enable
                    - disable
            autorun_log_fsck:
                description:
                    - Enable/disable automatic log partition check after ungraceful shutdown.
                type: str
                choices:
                    - enable
                    - disable
            av_affinity:
                description:
                    - Affinity setting for AV scanning (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).
                type: str
            av_failopen:
                description:
                    - Set the action to take if the FortiGate is running low on memory or the proxy connection limit has been reached.
                type: str
                choices:
                    - pass
                    - off
                    - one-shot
            av_failopen_session:
                description:
                    - When enabled and a proxy for a protocol runs out of room in its session table, that protocol goes into failopen mode and enacts the
                       action specified by av-failopen.
                type: str
                choices:
                    - enable
                    - disable
            batch_cmdb:
                description:
                    - Enable/disable batch mode, allowing you to enter a series of CLI commands that will execute as a group once they are loaded.
                type: str
                choices:
                    - enable
                    - disable
            block_session_timer:
                description:
                    - Duration in seconds for blocked sessions (1 - 300 sec  (5 minutes)).
                type: int
            br_fdb_max_entry:
                description:
                    - Maximum number of bridge forwarding database (FDB) entries.
                type: int
            cert_chain_max:
                description:
                    - Maximum number of certificates that can be traversed in a certificate chain.
                type: int
            cfg_revert_timeout:
                description:
                    - Time-out for reverting to the last saved configuration. (10 - 4294967295 seconds).
                type: int
            cfg_save:
                description:
                    - Configuration file save mode for CLI changes.
                type: str
                choices:
                    - automatic
                    - manual
                    - revert
            check_protocol_header:
                description:
                    - Level of checking performed on protocol headers. Strict checking is more thorough but may affect performance. Loose checking is ok in
                       most cases.
                type: str
                choices:
                    - loose
                    - strict
            check_reset_range:
                description:
                    - Configure ICMP error message verification. You can either apply strict RST range checking or disable it.
                type: str
                choices:
                    - strict
                    - disable
            cli_audit_log:
                description:
                    - Enable/disable CLI audit log.
                type: str
                choices:
                    - enable
                    - disable
            cloud_communication:
                description:
                    - Enable/disable all cloud communication.
                type: str
                choices:
                    - enable
                    - disable
            clt_cert_req:
                description:
                    - Enable/disable requiring administrators to have a client certificate to log into the GUI using HTTPS.
                type: str
                choices:
                    - enable
                    - disable
            cpu_use_threshold:
                description:
                    - Threshold at which CPU usage is reported. (% of total CPU).
                type: int
            csr_ca_attribute:
                description:
                    - Enable/disable the CA attribute in certificates. Some CA servers reject CSRs that have the CA attribute.
                type: str
                choices:
                    - enable
                    - disable
            daily_restart:
                description:
                    - Enable/disable daily restart of FortiGate unit. Use the restart-time option to set the time of day for the restart.
                type: str
                choices:
                    - enable
                    - disable
            default_service_source_port:
                description:
                    - Default service source port range.
                type: str
            device_identification_active_scan_delay:
                description:
                    - Number of seconds to passively scan a device before performing an active scan. (20 - 3600 sec, (20 sec to 1 hour)).
                type: int
            device_idle_timeout:
                description:
                    - Time in seconds that a device must be idle to automatically log the device user out. (30 - 31536000 sec (30 sec to 1 year)).
                type: int
            dh_params:
                description:
                    - Number of bits to use in the Diffie-Hellman exchange for HTTPS/SSH protocols.
                type: str
                choices:
                    - 1024
                    - 1536
                    - 2048
                    - 3072
                    - 4096
                    - 6144
                    - 8192
            dnsproxy_worker_count:
                description:
                    - DNS proxy worker count.
                type: int
            dst:
                description:
                    - Enable/disable daylight saving time.
                type: str
                choices:
                    - enable
                    - disable
            failtime:
                description:
                    - Fail-time for server lost.
                type: int
            faz_disk_buffer_size:
                description:
                    - Maximum disk buffer size to temporarily store logs destined for FortiAnalyzer. To be used in the event that FortiAnalyzer is
                       unavailalble.
                type: int
            fds_statistics:
                description:
                    - Enable/disable sending IPS, Application Control, and AntiVirus data to FortiGuard. This data is used to improve FortiGuard services and
                       is not shared with external parties and is protected by Fortinet"s privacy policy.
                type: str
                choices:
                    - enable
                    - disable
            fds_statistics_period:
                description:
                    - FortiGuard statistics collection period in minutes. (1 - 1440 min (1 min to 24 hours)).
                type: int
            fec_port:
                description:
                    - Local UDP port for Forward Error Correction (49152 - 65535).
                type: int
            fgd_alert_subscription:
                description:
                    - Type of alert to retrieve from FortiGuard.
                type: list
                choices:
                    - advisory
                    - latest-threat
                    - latest-virus
                    - latest-attack
                    - new-antivirus-db
                    - new-attack-db
            fortiextender:
                description:
                    - Enable/disable FortiExtender.
                type: str
                choices:
                    - disable
                    - enable
            fortiextender_data_port:
                description:
                    - FortiExtender data port (1024 - 49150).
                type: int
            fortiextender_vlan_mode:
                description:
                    - Enable/disable FortiExtender VLAN mode.
                type: str
                choices:
                    - enable
                    - disable
            fortiservice_port:
                description:
                    - FortiService port (1 - 65535). Used by FortiClient endpoint compliance. Older versions of FortiClient used a different port.
                type: int
            fortitoken_cloud:
                description:
                    - Enable/disable FortiToken Cloud service.
                type: str
                choices:
                    - enable
                    - disable
            gui_allow_default_hostname:
                description:
                    - Enable/disable the factory default hostname warning on the GUI setup wizard.
                type: str
                choices:
                    - enable
                    - disable
            gui_certificates:
                description:
                    - Enable/disable the System > Certificate GUI page, allowing you to add and configure certificates from the GUI.
                type: str
                choices:
                    - enable
                    - disable
            gui_custom_language:
                description:
                    - Enable/disable custom languages in GUI.
                type: str
                choices:
                    - enable
                    - disable
            gui_date_format:
                description:
                    - Default date format used throughout GUI.
                type: str
                choices:
                    - yyyy/MM/dd
                    - dd/MM/yyyy
                    - MM/dd/yyyy
                    - yyyy-MM-dd
                    - dd-MM-yyyy
                    - MM-dd-yyyy
            gui_date_time_source:
                description:
                    - Source from which the FortiGate GUI uses to display date and time entries.
                type: str
                choices:
                    - system
                    - browser
            gui_device_latitude:
                description:
                    - Add the latitude of the location of this FortiGate to position it on the Threat Map.
                type: str
            gui_device_longitude:
                description:
                    - Add the longitude of the location of this FortiGate to position it on the Threat Map.
                type: str
            gui_display_hostname:
                description:
                    - Enable/disable displaying the FortiGate"s hostname on the GUI login page.
                type: str
                choices:
                    - enable
                    - disable
            gui_firmware_upgrade_setup_warning:
                description:
                    - Enable/disable the firmware upgrade warning on GUI setup wizard.
                type: str
                choices:
                    - enable
                    - disable
            gui_fortisandbox_cloud:
                description:
                    - Enable/disable displaying FortiSandbox Cloud on the GUI.
                type: str
                choices:
                    - enable
                    - disable
            gui_ipv6:
                description:
                    - Enable/disable IPv6 settings on the GUI.
                type: str
                choices:
                    - enable
                    - disable
            gui_lines_per_page:
                description:
                    - Number of lines to display per page for web administration.
                type: int
            gui_theme:
                description:
                    - Color scheme for the administration GUI.
                type: str
                choices:
                    - green
                    - neutrino
                    - blue
                    - melongene
                    - mariner
            gui_wireless_opensecurity:
                description:
                    - Enable/disable wireless open security option on the GUI.
                type: str
                choices:
                    - enable
                    - disable
            honor_df:
                description:
                    - Enable/disable honoring of Don"t-Fragment (DF) flag.
                type: str
                choices:
                    - enable
                    - disable
            hostname:
                description:
                    - FortiGate unit"s hostname. Most models will truncate names longer than 24 characters. Some models support hostnames up to 35 characters.
                type: str
            igmp_state_limit:
                description:
                    - Maximum number of IGMP memberships (96 - 64000).
                type: int
            interval:
                description:
                    - Dead gateway detection interval.
                type: int
            ip_src_port_range:
                description:
                    - IP source port range used for traffic originating from the FortiGate unit.
                type: str
            ips_affinity:
                description:
                    - Affinity setting for IPS (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx; allowed CPUs must be less than total
                       number of IPS engine daemons).
                type: str
            ipsec_asic_offload:
                description:
                    - Enable/disable ASIC offloading (hardware acceleration) for IPsec VPN traffic. Hardware acceleration can offload IPsec VPN sessions and
                       accelerate encryption and decryption.
                type: str
                choices:
                    - enable
                    - disable
            ipsec_hmac_offload:
                description:
                    - Enable/disable offloading (hardware acceleration) of HMAC processing for IPsec VPN.
                type: str
                choices:
                    - enable
                    - disable
            ipsec_soft_dec_async:
                description:
                    - Enable/disable software decryption asynchronization (using multiple CPUs to do decryption) for IPsec VPN traffic.
                type: str
                choices:
                    - enable
                    - disable
            ipv6_accept_dad:
                description:
                    - Enable/disable acceptance of IPv6 Duplicate Address Detection (DAD).
                type: int
            ipv6_allow_anycast_probe:
                description:
                    - Enable/disable IPv6 address probe through Anycast.
                type: str
                choices:
                    - enable
                    - disable
            language:
                description:
                    - GUI display language.
                type: str
                choices:
                    - english
                    - french
                    - spanish
                    - portuguese
                    - japanese
                    - trach
                    - simch
                    - korean
            ldapconntimeout:
                description:
                    - Global timeout for connections with remote LDAP servers in milliseconds (1 - 300000).
                type: int
            lldp_reception:
                description:
                    - Enable/disable Link Layer Discovery Protocol (LLDP) reception.
                type: str
                choices:
                    - enable
                    - disable
            lldp_transmission:
                description:
                    - Enable/disable Link Layer Discovery Protocol (LLDP) transmission.
                type: str
                choices:
                    - enable
                    - disable
            log_ssl_connection:
                description:
                    - Enable/disable logging of SSL connection events.
                type: str
                choices:
                    - enable
                    - disable
            log_uuid_address:
                description:
                    - Enable/disable insertion of address UUIDs to traffic logs.
                type: str
                choices:
                    - enable
                    - disable
            log_uuid_policy:
                description:
                    - Enable/disable insertion of policy UUIDs to traffic logs.
                type: str
                choices:
                    - enable
                    - disable
            login_timestamp:
                description:
                    - Enable/disable login time recording.
                type: str
                choices:
                    - enable
                    - disable
            management_vdom:
                description:
                    - Management virtual domain name. Source system.vdom.name.
                type: str
            max_dlpstat_memory:
                description:
                    - Maximum DLP stat memory (0 - 4294967295).
                type: int
            max_route_cache_size:
                description:
                    - Maximum number of IP route cache entries (0 - 2147483647).
                type: int
            memory_use_threshold_extreme:
                description:
                    - Threshold at which memory usage is considered extreme (new sessions are dropped) (% of total RAM).
                type: int
            memory_use_threshold_green:
                description:
                    - Threshold at which memory usage forces the FortiGate to exit conserve mode (% of total RAM).
                type: int
            memory_use_threshold_red:
                description:
                    - Threshold at which memory usage forces the FortiGate to enter conserve mode (% of total RAM).
                type: int
            miglog_affinity:
                description:
                    - Affinity setting for logging (64-bit hexadecimal value in the format of xxxxxxxxxxxxxxxx).
                type: str
            miglogd_children:
                description:
                    - Number of logging (miglogd) processes to be allowed to run. Higher number can reduce performance; lower number can slow log processing
                       time. No logs will be dropped or lost if the number is changed.
                type: int
            multi_factor_authentication:
                description:
                    - Enforce all login methods to require an additional authentication factor .
                type: str
                choices:
                    - optional
                    - mandatory
            ndp_max_entry:
                description:
                    - Maximum number of NDP table entries (set to 65,536 or higher; if set to 0, kernel holds 65,536 entries).
                type: int
            per_user_bwl:
                description:
                    - Enable/disable per-user black/white list filter.
                type: str
                choices:
                    - enable
                    - disable
            policy_auth_concurrent:
                description:
                    - Number of concurrent firewall use logins from the same user (1 - 100).
                type: int
            post_login_banner:
                description:
                    - Enable/disable displaying the administrator access disclaimer message after an administrator successfully logs in.
                type: str
                choices:
                    - disable
                    - enable
            pre_login_banner:
                description:
                    - Enable/disable displaying the administrator access disclaimer message on the login page before an administrator logs in.
                type: str
                choices:
                    - enable
                    - disable
            private_data_encryption:
                description:
                    - Enable/disable private data encryption using an AES 128-bit key.
                type: str
                choices:
                    - disable
                    - enable
            proxy_auth_lifetime:
                description:
                    - Enable/disable authenticated users lifetime control.  This is a cap on the total time a proxy user can be authenticated for after which
                       re-authentication will take place.
                type: str
                choices:
                    - enable
                    - disable
            proxy_auth_lifetime_timeout:
                description:
                    - Lifetime timeout in minutes for authenticated users (5  - 65535 min).
                type: int
            proxy_auth_timeout:
                description:
                    - Authentication timeout in minutes for authenticated users (1 - 300 min).
                type: int
            proxy_re_authentication_mode:
                description:
                    - Control if users must re-authenticate after a session is closed, traffic has been idle, or from the point at which the user was first
                       created.
                type: str
                choices:
                    - session
                    - traffic
                    - absolute
            proxy_worker_count:
                description:
                    - Proxy worker count.
                type: int
            radius_port:
                description:
                    - RADIUS service port number.
                type: int
            reboot_upon_config_restore:
                description:
                    - Enable/disable reboot of system upon restoring configuration.
                type: str
                choices:
                    - enable
                    - disable
            refresh:
                description:
                    - Statistics refresh interval second(s) in GUI.
                type: int
            remoteauthtimeout:
                description:
                    - Number of seconds that the FortiGate waits for responses from remote RADIUS, LDAP, or TACACS+ authentication servers. (1-300 sec).
                type: int
            reset_sessionless_tcp:
                description:
                    - Action to perform if the FortiGate receives a TCP packet but cannot find a corresponding session in its session table. NAT/Route mode
                       only.
                type: str
                choices:
                    - enable
                    - disable
            restart_time:
                description:
                    - 'Daily restart time (hh:mm).'
                type: str
            revision_backup_on_logout:
                description:
                    - Enable/disable back-up of the latest configuration revision when an administrator logs out of the CLI or GUI.
                type: str
                choices:
                    - enable
                    - disable
            revision_image_auto_backup:
                description:
                    - Enable/disable back-up of the latest configuration revision after the firmware is upgraded.
                type: str
                choices:
                    - enable
                    - disable
            scanunit_count:
                description:
                    - Number of scanunits. The range and the default depend on the number of CPUs. Only available on FortiGate units with multiple CPUs.
                type: int
            security_rating_result_submission:
                description:
                    - Enable/disable the submission of Security Rating results to FortiGuard.
                type: str
                choices:
                    - enable
                    - disable
            security_rating_run_on_schedule:
                description:
                    - Enable/disable scheduled runs of Security Rating.
                type: str
                choices:
                    - enable
                    - disable
            send_pmtu_icmp:
                description:
                    - Enable/disable sending of path maximum transmission unit (PMTU) - ICMP destination unreachable packet and to support PMTUD protocol on
                       your network to reduce fragmentation of packets.
                type: str
                choices:
                    - enable
                    - disable
            snat_route_change:
                description:
                    - Enable/disable the ability to change the static NAT route.
                type: str
                choices:
                    - enable
                    - disable
            special_file_23_support:
                description:
                    - Enable/disable IPS detection of HIBUN format files when using Data Leak Protection.
                type: str
                choices:
                    - disable
                    - enable
            ssd_trim_date:
                description:
                    - Date within a month to run ssd trim.
                type: int
            ssd_trim_freq:
                description:
                    - How often to run SSD Trim . SSD Trim prevents SSD drive data loss by finding and isolating errors.
                type: str
                choices:
                    - never
                    - hourly
                    - daily
                    - weekly
                    - monthly
            ssd_trim_hour:
                description:
                    - Hour of the day on which to run SSD Trim (0 - 23).
                type: int
            ssd_trim_min:
                description:
                    - Minute of the hour on which to run SSD Trim (0 - 59, 60 for random).
                type: int
            ssd_trim_weekday:
                description:
                    - Day of week to run SSD Trim.
                type: str
                choices:
                    - sunday
                    - monday
                    - tuesday
                    - wednesday
                    - thursday
                    - friday
                    - saturday
            ssh_cbc_cipher:
                description:
                    - Enable/disable CBC cipher for SSH access.
                type: str
                choices:
                    - enable
                    - disable
            ssh_hmac_md5:
                description:
                    - Enable/disable HMAC-MD5 for SSH access.
                type: str
                choices:
                    - enable
                    - disable
            ssh_kex_sha1:
                description:
                    - Enable/disable SHA1 key exchange for SSH access.
                type: str
                choices:
                    - enable
                    - disable
            ssh_mac_weak:
                description:
                    - Enable/disable HMAC-SHA1 and UMAC-64-ETM for SSH access.
                type: str
                choices:
                    - enable
                    - disable
            ssl_min_proto_version:
                description:
                    - Minimum supported protocol version for SSL/TLS connections .
                type: str
                choices:
                    - SSLv3
                    - TLSv1
                    - TLSv1-1
                    - TLSv1-2
                    - TLSv1-3
            ssl_static_key_ciphers:
                description:
                    - Enable/disable static key ciphers in SSL/TLS connections (e.g. AES128-SHA, AES256-SHA, AES128-SHA256, AES256-SHA256).
                type: str
                choices:
                    - enable
                    - disable
            sslvpn_max_worker_count:
                description:
                    - Maximum number of SSL VPN processes. Upper limit for this value is the number of CPUs and depends on the model. Default value of zero
                       means the SSLVPN daemon decides the number of worker processes.
                type: int
            sslvpn_plugin_version_check:
                description:
                    - Enable/disable checking browser"s plugin version by SSL VPN.
                type: str
                choices:
                    - enable
                    - disable
            strict_dirty_session_check:
                description:
                    - Enable to check the session against the original policy when revalidating. This can prevent dropping of redirected sessions when
                       web-filtering and authentication are enabled together. If this option is enabled, the FortiGate unit deletes a session if a routing or
                          policy change causes the session to no longer match the policy that originally allowed the session.
                type: str
                choices:
                    - enable
                    - disable
            strong_crypto:
                description:
                    - Enable to use strong encryption and only allow strong ciphers (AES, 3DES) and digest (SHA1) for HTTPS/SSH/TLS/SSL functions.
                type: str
                choices:
                    - enable
                    - disable
            switch_controller:
                description:
                    - Enable/disable switch controller feature. Switch controller allows you to manage FortiSwitch from the FortiGate itself.
                type: str
                choices:
                    - disable
                    - enable
            switch_controller_reserved_network:
                description:
                    - Enable reserved network subnet for controlled switches. This is available when the switch controller is enabled.
                type: str
            sys_perf_log_interval:
                description:
                    - Time in minutes between updates of performance statistics logging. (1 - 15 min).
                type: int
            tcp_halfclose_timer:
                description:
                    - Number of seconds the FortiGate unit should wait to close a session after one peer has sent a FIN packet but the other has not responded
                       (1 - 86400 sec (1 day)).
                type: int
            tcp_halfopen_timer:
                description:
                    - Number of seconds the FortiGate unit should wait to close a session after one peer has sent an open session packet but the other has not
                       responded (1 - 86400 sec (1 day)).
                type: int
            tcp_option:
                description:
                    - Enable SACK, timestamp and MSS TCP options.
                type: str
                choices:
                    - enable
                    - disable
            tcp_timewait_timer:
                description:
                    - Length of the TCP TIME-WAIT state in seconds.
                type: int
            tftp:
                description:
                    - Enable/disable TFTP.
                type: str
                choices:
                    - enable
                    - disable
            timezone:
                description:
                    - Number corresponding to your time zone from 00 to 86. Enter set timezone ? to view the list of time zones and the numbers that represent
                       them.
                type: str
                choices:
                    - 01
                    - 02
                    - 03
                    - 04
                    - 05
                    - 81
                    - 06
                    - 07
                    - 08
                    - 09
                    - 10
                    - 11
                    - 12
                    - 13
                    - 74
                    - 14
                    - 77
                    - 15
                    - 87
                    - 16
                    - 17
                    - 18
                    - 19
                    - 20
                    - 75
                    - 21
                    - 22
                    - 23
                    - 24
                    - 80
                    - 79
                    - 25
                    - 26
                    - 27
                    - 28
                    - 78
                    - 29
                    - 30
                    - 31
                    - 32
                    - 33
                    - 34
                    - 35
                    - 36
                    - 37
                    - 38
                    - 83
                    - 84
                    - 40
                    - 85
                    - 41
                    - 42
                    - 43
                    - 39
                    - 44
                    - 46
                    - 47
                    - 51
                    - 48
                    - 45
                    - 49
                    - 50
                    - 52
                    - 53
                    - 54
                    - 55
                    - 56
                    - 57
                    - 58
                    - 59
                    - 60
                    - 62
                    - 63
                    - 61
                    - 64
                    - 65
                    - 66
                    - 67
                    - 68
                    - 69
                    - 70
                    - 71
                    - 72
                    - 00
                    - 82
                    - 73
                    - 86
                    - 76
            traffic_priority:
                description:
                    - Choose Type of Service (ToS) or Differentiated Services Code Point (DSCP) for traffic prioritization in traffic shaping.
                type: str
                choices:
                    - tos
                    - dscp
            traffic_priority_level:
                description:
                    - Default system-wide level of priority for traffic prioritization.
                type: str
                choices:
                    - low
                    - medium
                    - high
            two_factor_email_expiry:
                description:
                    - Email-based two-factor authentication session timeout (30 - 300 seconds (5 minutes)).
                type: int
            two_factor_fac_expiry:
                description:
                    - FortiAuthenticator token authentication session timeout (10 - 3600 seconds (1 hour)).
                type: int
            two_factor_ftk_expiry:
                description:
                    - FortiToken authentication session timeout (60 - 600 sec (10 minutes)).
                type: int
            two_factor_ftm_expiry:
                description:
                    - FortiToken Mobile session timeout (1 - 168 hours (7 days)).
                type: int
            two_factor_sms_expiry:
                description:
                    - SMS-based two-factor authentication session timeout (30 - 300 sec).
                type: int
            udp_idle_timer:
                description:
                    - UDP connection session timeout. This command can be useful in managing CPU and memory resources (1 - 86400 seconds (1 day)).
                type: int
            url_filter_affinity:
                description:
                    - URL filter CPU affinity.
                type: str
            url_filter_count:
                description:
                    - URL filter daemon count.
                type: int
            user_server_cert:
                description:
                    - Certificate to use for https user authentication. Source certificate.local.name.
                type: str
            vip_arp_range:
                description:
                    - Controls the number of ARPs that the FortiGate sends for a Virtual IP (VIP) address range.
                type: str
                choices:
                    - unlimited
                    - restricted
            wad_affinity:
                description:
                    - Affinity setting for wad (hexadecimal value up to 256 bits in the format of xxxxxxxxxxxxxxxx).
                type: str
            wad_csvc_cs_count:
                description:
                    - Number of concurrent WAD-cache-service object-cache processes.
                type: int
            wad_csvc_db_count:
                description:
                    - Number of concurrent WAD-cache-service byte-cache processes.
                type: int
            wad_memory_change_granularity:
                description:
                    - Minimum percentage change in system memory usage detected by the wad daemon prior to adjusting TCP window size for any active connection.
                type: int
            wad_source_affinity:
                description:
                    - Enable/disable dispatching traffic to WAD workers based on source affinity.
                type: str
                choices:
                    - disable
                    - enable
            wad_worker_count:
                description:
                    - Number of explicit proxy WAN optimization daemon (WAD) processes. By default WAN optimization, explicit proxy, and web caching is
                       handled by all of the CPU cores in a FortiGate unit.
                type: int
            wifi_ca_certificate:
                description:
                    - CA certificate that verifies the WiFi certificate. Source certificate.ca.name.
                type: str
            wifi_certificate:
                description:
                    - Certificate to use for WiFi authentication. Source certificate.local.name.
                type: str
            wimax_4g_usb:
                description:
                    - Enable/disable comparability with WiMAX 4G USB devices.
                type: str
                choices:
                    - enable
                    - disable
            wireless_controller:
                description:
                    - Enable/disable the wireless controller feature to use the FortiGate unit to manage FortiAPs.
                type: str
                choices:
                    - enable
                    - disable
            wireless_controller_port:
                description:
                    - Port used for the control channel in wireless controller mode (wireless-mode is ac). The data channel port is the control channel port
                       number plus one (1024 - 49150).
                type: int
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
  - name: Configure global attributes.
    fortios_system_global:
      vdom:  "{{ vdom }}"
      system_global:
        admin_concurrent: "enable"
        admin_console_timeout: "4"
        admin_hsts_max_age: "5"
        admin_https_pki_required: "enable"
        admin_https_redirect: "enable"
        admin_https_ssl_versions: "tlsv1-1"
        admin_lockout_duration: "9"
        admin_lockout_threshold: "10"
        admin_login_max: "11"
        admin_maintainer: "enable"
        admin_port: "13"
        admin_restrict_local: "enable"
        admin_scp: "enable"
        admin_server_cert: "<your_own_value> (source certificate.local.name)"
        admin_sport: "17"
        admin_ssh_grace_time: "18"
        admin_ssh_password: "enable"
        admin_ssh_port: "20"
        admin_ssh_v1: "enable"
        admin_telnet: "enable"
        admin_telnet_port: "23"
        admintimeout: "24"
        alias: "<your_own_value>"
        allow_traffic_redirect: "enable"
        anti_replay: "disable"
        arp_max_entry: "28"
        auth_cert: "<your_own_value> (source certificate.local.name)"
        auth_http_port: "30"
        auth_https_port: "31"
        auth_keepalive: "enable"
        auth_session_limit: "block-new"
        auto_auth_extension_device: "enable"
        autorun_log_fsck: "enable"
        av_affinity: "<your_own_value>"
        av_failopen: "pass"
        av_failopen_session: "enable"
        batch_cmdb: "enable"
        block_session_timer: "40"
        br_fdb_max_entry: "41"
        cert_chain_max: "42"
        cfg_revert_timeout: "43"
        cfg_save: "automatic"
        check_protocol_header: "loose"
        check_reset_range: "strict"
        cli_audit_log: "enable"
        cloud_communication: "enable"
        clt_cert_req: "enable"
        cpu_use_threshold: "50"
        csr_ca_attribute: "enable"
        daily_restart: "enable"
        default_service_source_port: "<your_own_value>"
        device_identification_active_scan_delay: "54"
        device_idle_timeout: "55"
        dh_params: "1024"
        dnsproxy_worker_count: "57"
        dst: "enable"
        failtime: "59"
        faz_disk_buffer_size: "60"
        fds_statistics: "enable"
        fds_statistics_period: "62"
        fec_port: "63"
        fgd_alert_subscription: "advisory"
        fortiextender: "disable"
        fortiextender_data_port: "66"
        fortiextender_vlan_mode: "enable"
        fortiservice_port: "68"
        fortitoken_cloud: "enable"
        gui_allow_default_hostname: "enable"
        gui_certificates: "enable"
        gui_custom_language: "enable"
        gui_date_format: "yyyy/MM/dd"
        gui_date_time_source: "system"
        gui_device_latitude: "<your_own_value>"
        gui_device_longitude: "<your_own_value>"
        gui_display_hostname: "enable"
        gui_firmware_upgrade_setup_warning: "enable"
        gui_fortisandbox_cloud: "enable"
        gui_ipv6: "enable"
        gui_lines_per_page: "81"
        gui_theme: "green"
        gui_wireless_opensecurity: "enable"
        honor_df: "enable"
        hostname: "myhostname"
        igmp_state_limit: "86"
        interval: "87"
        ip_src_port_range: "<your_own_value>"
        ips_affinity: "<your_own_value>"
        ipsec_asic_offload: "enable"
        ipsec_hmac_offload: "enable"
        ipsec_soft_dec_async: "enable"
        ipv6_accept_dad: "93"
        ipv6_allow_anycast_probe: "enable"
        language: "english"
        ldapconntimeout: "96"
        lldp_reception: "enable"
        lldp_transmission: "enable"
        log_ssl_connection: "enable"
        log_uuid_address: "enable"
        log_uuid_policy: "enable"
        login_timestamp: "enable"
        management_vdom: "<your_own_value> (source system.vdom.name)"
        max_dlpstat_memory: "104"
        max_route_cache_size: "105"
        memory_use_threshold_extreme: "106"
        memory_use_threshold_green: "107"
        memory_use_threshold_red: "108"
        miglog_affinity: "<your_own_value>"
        miglogd_children: "110"
        multi_factor_authentication: "optional"
        ndp_max_entry: "112"
        per_user_bwl: "enable"
        policy_auth_concurrent: "114"
        post_login_banner: "disable"
        pre_login_banner: "enable"
        private_data_encryption: "disable"
        proxy_auth_lifetime: "enable"
        proxy_auth_lifetime_timeout: "119"
        proxy_auth_timeout: "120"
        proxy_re_authentication_mode: "session"
        proxy_worker_count: "122"
        radius_port: "123"
        reboot_upon_config_restore: "enable"
        refresh: "125"
        remoteauthtimeout: "126"
        reset_sessionless_tcp: "enable"
        restart_time: "<your_own_value>"
        revision_backup_on_logout: "enable"
        revision_image_auto_backup: "enable"
        scanunit_count: "131"
        security_rating_result_submission: "enable"
        security_rating_run_on_schedule: "enable"
        send_pmtu_icmp: "enable"
        snat_route_change: "enable"
        special_file_23_support: "disable"
        ssd_trim_date: "137"
        ssd_trim_freq: "never"
        ssd_trim_hour: "139"
        ssd_trim_min: "140"
        ssd_trim_weekday: "sunday"
        ssh_cbc_cipher: "enable"
        ssh_hmac_md5: "enable"
        ssh_kex_sha1: "enable"
        ssh_mac_weak: "enable"
        ssl_min_proto_version: "SSLv3"
        ssl_static_key_ciphers: "enable"
        sslvpn_max_worker_count: "148"
        sslvpn_plugin_version_check: "enable"
        strict_dirty_session_check: "enable"
        strong_crypto: "enable"
        switch_controller: "disable"
        switch_controller_reserved_network: "<your_own_value>"
        sys_perf_log_interval: "154"
        tcp_halfclose_timer: "155"
        tcp_halfopen_timer: "156"
        tcp_option: "enable"
        tcp_timewait_timer: "158"
        tftp: "enable"
        timezone: "01"
        traffic_priority: "tos"
        traffic_priority_level: "low"
        two_factor_email_expiry: "163"
        two_factor_fac_expiry: "164"
        two_factor_ftk_expiry: "165"
        two_factor_ftm_expiry: "166"
        two_factor_sms_expiry: "167"
        udp_idle_timer: "168"
        url_filter_affinity: "<your_own_value>"
        url_filter_count: "170"
        user_server_cert: "<your_own_value> (source certificate.local.name)"
        vip_arp_range: "unlimited"
        wad_affinity: "<your_own_value>"
        wad_csvc_cs_count: "174"
        wad_csvc_db_count: "175"
        wad_memory_change_granularity: "176"
        wad_source_affinity: "disable"
        wad_worker_count: "178"
        wifi_ca_certificate: "<your_own_value> (source certificate.ca.name)"
        wifi_certificate: "<your_own_value> (source certificate.local.name)"
        wimax_4g_usb: "enable"
        wireless_controller: "enable"
        wireless_controller_port: "183"

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


def filter_system_global_data(json):
    option_list = ['admin_concurrent', 'admin_console_timeout', 'admin_hsts_max_age',
                   'admin_https_pki_required', 'admin_https_redirect', 'admin_https_ssl_versions',
                   'admin_lockout_duration', 'admin_lockout_threshold', 'admin_login_max',
                   'admin_maintainer', 'admin_port', 'admin_restrict_local',
                   'admin_scp', 'admin_server_cert', 'admin_sport',
                   'admin_ssh_grace_time', 'admin_ssh_password', 'admin_ssh_port',
                   'admin_ssh_v1', 'admin_telnet', 'admin_telnet_port',
                   'admintimeout', 'alias', 'allow_traffic_redirect',
                   'anti_replay', 'arp_max_entry', 'auth_cert',
                   'auth_http_port', 'auth_https_port', 'auth_keepalive',
                   'auth_session_limit', 'auto_auth_extension_device', 'autorun_log_fsck',
                   'av_affinity', 'av_failopen', 'av_failopen_session',
                   'batch_cmdb', 'block_session_timer', 'br_fdb_max_entry',
                   'cert_chain_max', 'cfg_revert_timeout', 'cfg_save',
                   'check_protocol_header', 'check_reset_range', 'cli_audit_log',
                   'cloud_communication', 'clt_cert_req', 'cpu_use_threshold',
                   'csr_ca_attribute', 'daily_restart', 'default_service_source_port',
                   'device_identification_active_scan_delay', 'device_idle_timeout', 'dh_params',
                   'dnsproxy_worker_count', 'dst', 'failtime',
                   'faz_disk_buffer_size', 'fds_statistics', 'fds_statistics_period',
                   'fec_port', 'fgd_alert_subscription', 'fortiextender',
                   'fortiextender_data_port', 'fortiextender_vlan_mode', 'fortiservice_port',
                   'fortitoken_cloud', 'gui_allow_default_hostname', 'gui_certificates',
                   'gui_custom_language', 'gui_date_format', 'gui_date_time_source',
                   'gui_device_latitude', 'gui_device_longitude', 'gui_display_hostname',
                   'gui_firmware_upgrade_setup_warning', 'gui_fortisandbox_cloud', 'gui_ipv6',
                   'gui_lines_per_page', 'gui_theme', 'gui_wireless_opensecurity',
                   'honor_df', 'hostname', 'igmp_state_limit',
                   'interval', 'ip_src_port_range', 'ips_affinity',
                   'ipsec_asic_offload', 'ipsec_hmac_offload', 'ipsec_soft_dec_async',
                   'ipv6_accept_dad', 'ipv6_allow_anycast_probe', 'language',
                   'ldapconntimeout', 'lldp_reception', 'lldp_transmission',
                   'log_ssl_connection', 'log_uuid_address', 'log_uuid_policy',
                   'login_timestamp', 'management_vdom', 'max_dlpstat_memory',
                   'max_route_cache_size', 'memory_use_threshold_extreme', 'memory_use_threshold_green',
                   'memory_use_threshold_red', 'miglog_affinity', 'miglogd_children',
                   'multi_factor_authentication', 'ndp_max_entry', 'per_user_bwl',
                   'policy_auth_concurrent', 'post_login_banner', 'pre_login_banner',
                   'private_data_encryption', 'proxy_auth_lifetime', 'proxy_auth_lifetime_timeout',
                   'proxy_auth_timeout', 'proxy_re_authentication_mode', 'proxy_worker_count',
                   'radius_port', 'reboot_upon_config_restore', 'refresh',
                   'remoteauthtimeout', 'reset_sessionless_tcp', 'restart_time',
                   'revision_backup_on_logout', 'revision_image_auto_backup', 'scanunit_count',
                   'security_rating_result_submission', 'security_rating_run_on_schedule', 'send_pmtu_icmp',
                   'snat_route_change', 'special_file_23_support', 'ssd_trim_date',
                   'ssd_trim_freq', 'ssd_trim_hour', 'ssd_trim_min',
                   'ssd_trim_weekday', 'ssh_cbc_cipher', 'ssh_hmac_md5',
                   'ssh_kex_sha1', 'ssh_mac_weak', 'ssl_min_proto_version',
                   'ssl_static_key_ciphers', 'sslvpn_max_worker_count', 'sslvpn_plugin_version_check',
                   'strict_dirty_session_check', 'strong_crypto', 'switch_controller',
                   'switch_controller_reserved_network', 'sys_perf_log_interval', 'tcp_halfclose_timer',
                   'tcp_halfopen_timer', 'tcp_option', 'tcp_timewait_timer',
                   'tftp', 'timezone', 'traffic_priority',
                   'traffic_priority_level', 'two_factor_email_expiry', 'two_factor_fac_expiry',
                   'two_factor_ftk_expiry', 'two_factor_ftm_expiry', 'two_factor_sms_expiry',
                   'udp_idle_timer', 'url_filter_affinity', 'url_filter_count',
                   'user_server_cert', 'vip_arp_range', 'wad_affinity',
                   'wad_csvc_cs_count', 'wad_csvc_db_count', 'wad_memory_change_granularity',
                   'wad_source_affinity', 'wad_worker_count', 'wifi_ca_certificate',
                   'wifi_certificate', 'wimax_4g_usb', 'wireless_controller',
                   'wireless_controller_port']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def flatten_multilists_attributes(data):
    multilist_attrs = [[u'admin_https_ssl_versions'], [u'fgd_alert_subscription']]

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


def system_global(data, fos):
    vdom = data['vdom']
    system_global_data = data['system_global']
    system_global_data = flatten_multilists_attributes(system_global_data)
    filtered_data = underscore_to_hyphen(filter_system_global_data(system_global_data))

    return fos.set('system',
                   'global',
                   data=filtered_data,
                   vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_system(data, fos):

    if data['system_global']:
        resp = system_global(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('system_global'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = None
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "system_global": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "admin_concurrent": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "admin_console_timeout": {"required": False, "type": "int"},
                "admin_hsts_max_age": {"required": False, "type": "int"},
                "admin_https_pki_required": {"required": False, "type": "str",
                                             "choices": ["enable",
                                                         "disable"]},
                "admin_https_redirect": {"required": False, "type": "str",
                                         "choices": ["enable",
                                                     "disable"]},
                "admin_https_ssl_versions": {"required": False, "type": "list",
                                             "choices": ["tlsv1-1",
                                                         "tlsv1-2",
                                                         "tlsv1-3"]},
                "admin_lockout_duration": {"required": False, "type": "int"},
                "admin_lockout_threshold": {"required": False, "type": "int"},
                "admin_login_max": {"required": False, "type": "int"},
                "admin_maintainer": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "admin_port": {"required": False, "type": "int"},
                "admin_restrict_local": {"required": False, "type": "str",
                                         "choices": ["enable",
                                                     "disable"]},
                "admin_scp": {"required": False, "type": "str",
                              "choices": ["enable",
                                          "disable"]},
                "admin_server_cert": {"required": False, "type": "str"},
                "admin_sport": {"required": False, "type": "int"},
                "admin_ssh_grace_time": {"required": False, "type": "int"},
                "admin_ssh_password": {"required": False, "type": "str",
                                       "choices": ["enable",
                                                   "disable"]},
                "admin_ssh_port": {"required": False, "type": "int"},
                "admin_ssh_v1": {"required": False, "type": "str",
                                 "choices": ["enable",
                                             "disable"]},
                "admin_telnet": {"required": False, "type": "str",
                                 "choices": ["enable",
                                             "disable"]},
                "admin_telnet_port": {"required": False, "type": "int"},
                "admintimeout": {"required": False, "type": "int"},
                "alias": {"required": False, "type": "str"},
                "allow_traffic_redirect": {"required": False, "type": "str",
                                           "choices": ["enable",
                                                       "disable"]},
                "anti_replay": {"required": False, "type": "str",
                                "choices": ["disable",
                                            "loose",
                                            "strict"]},
                "arp_max_entry": {"required": False, "type": "int"},
                "auth_cert": {"required": False, "type": "str"},
                "auth_http_port": {"required": False, "type": "int"},
                "auth_https_port": {"required": False, "type": "int"},
                "auth_keepalive": {"required": False, "type": "str",
                                   "choices": ["enable",
                                               "disable"]},
                "auth_session_limit": {"required": False, "type": "str",
                                       "choices": ["block-new",
                                                   "logout-inactive"]},
                "auto_auth_extension_device": {"required": False, "type": "str",
                                               "choices": ["enable",
                                                           "disable"]},
                "autorun_log_fsck": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "av_affinity": {"required": False, "type": "str"},
                "av_failopen": {"required": False, "type": "str",
                                "choices": ["pass",
                                            "off",
                                            "one-shot"]},
                "av_failopen_session": {"required": False, "type": "str",
                                        "choices": ["enable",
                                                    "disable"]},
                "batch_cmdb": {"required": False, "type": "str",
                               "choices": ["enable",
                                           "disable"]},
                "block_session_timer": {"required": False, "type": "int"},
                "br_fdb_max_entry": {"required": False, "type": "int"},
                "cert_chain_max": {"required": False, "type": "int"},
                "cfg_revert_timeout": {"required": False, "type": "int"},
                "cfg_save": {"required": False, "type": "str",
                             "choices": ["automatic",
                                         "manual",
                                         "revert"]},
                "check_protocol_header": {"required": False, "type": "str",
                                          "choices": ["loose",
                                                      "strict"]},
                "check_reset_range": {"required": False, "type": "str",
                                      "choices": ["strict",
                                                  "disable"]},
                "cli_audit_log": {"required": False, "type": "str",
                                  "choices": ["enable",
                                              "disable"]},
                "cloud_communication": {"required": False, "type": "str",
                                        "choices": ["enable",
                                                    "disable"]},
                "clt_cert_req": {"required": False, "type": "str",
                                 "choices": ["enable",
                                             "disable"]},
                "cpu_use_threshold": {"required": False, "type": "int"},
                "csr_ca_attribute": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "daily_restart": {"required": False, "type": "str",
                                  "choices": ["enable",
                                              "disable"]},
                "default_service_source_port": {"required": False, "type": "str"},
                "device_identification_active_scan_delay": {"required": False, "type": "int"},
                "device_idle_timeout": {"required": False, "type": "int"},
                "dh_params": {"required": False, "type": "str",
                              "choices": ["1024",
                                          "1536",
                                          "2048",
                                          "3072",
                                          "4096",
                                          "6144",
                                          "8192"]},
                "dnsproxy_worker_count": {"required": False, "type": "int"},
                "dst": {"required": False, "type": "str",
                        "choices": ["enable",
                                    "disable"]},
                "failtime": {"required": False, "type": "int"},
                "faz_disk_buffer_size": {"required": False, "type": "int"},
                "fds_statistics": {"required": False, "type": "str",
                                   "choices": ["enable",
                                               "disable"]},
                "fds_statistics_period": {"required": False, "type": "int"},
                "fec_port": {"required": False, "type": "int"},
                "fgd_alert_subscription": {"required": False, "type": "list",
                                           "choices": ["advisory",
                                                       "latest-threat",
                                                       "latest-virus",
                                                       "latest-attack",
                                                       "new-antivirus-db",
                                                       "new-attack-db"]},
                "fortiextender": {"required": False, "type": "str",
                                  "choices": ["disable",
                                              "enable"]},
                "fortiextender_data_port": {"required": False, "type": "int"},
                "fortiextender_vlan_mode": {"required": False, "type": "str",
                                            "choices": ["enable",
                                                        "disable"]},
                "fortiservice_port": {"required": False, "type": "int"},
                "fortitoken_cloud": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "gui_allow_default_hostname": {"required": False, "type": "str",
                                               "choices": ["enable",
                                                           "disable"]},
                "gui_certificates": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "gui_custom_language": {"required": False, "type": "str",
                                        "choices": ["enable",
                                                    "disable"]},
                "gui_date_format": {"required": False, "type": "str",
                                    "choices": ["yyyy/MM/dd",
                                                "dd/MM/yyyy",
                                                "MM/dd/yyyy",
                                                "yyyy-MM-dd",
                                                "dd-MM-yyyy",
                                                "MM-dd-yyyy"]},
                "gui_date_time_source": {"required": False, "type": "str",
                                         "choices": ["system",
                                                     "browser"]},
                "gui_device_latitude": {"required": False, "type": "str"},
                "gui_device_longitude": {"required": False, "type": "str"},
                "gui_display_hostname": {"required": False, "type": "str",
                                         "choices": ["enable",
                                                     "disable"]},
                "gui_firmware_upgrade_setup_warning": {"required": False, "type": "str",
                                                       "choices": ["enable",
                                                                   "disable"]},
                "gui_fortisandbox_cloud": {"required": False, "type": "str",
                                           "choices": ["enable",
                                                       "disable"]},
                "gui_ipv6": {"required": False, "type": "str",
                             "choices": ["enable",
                                         "disable"]},
                "gui_lines_per_page": {"required": False, "type": "int"},
                "gui_theme": {"required": False, "type": "str",
                              "choices": ["green",
                                          "neutrino",
                                          "blue",
                                          "melongene",
                                          "mariner"]},
                "gui_wireless_opensecurity": {"required": False, "type": "str",
                                              "choices": ["enable",
                                                          "disable"]},
                "honor_df": {"required": False, "type": "str",
                             "choices": ["enable",
                                         "disable"]},
                "hostname": {"required": False, "type": "str"},
                "igmp_state_limit": {"required": False, "type": "int"},
                "interval": {"required": False, "type": "int"},
                "ip_src_port_range": {"required": False, "type": "str"},
                "ips_affinity": {"required": False, "type": "str"},
                "ipsec_asic_offload": {"required": False, "type": "str",
                                       "choices": ["enable",
                                                   "disable"]},
                "ipsec_hmac_offload": {"required": False, "type": "str",
                                       "choices": ["enable",
                                                   "disable"]},
                "ipsec_soft_dec_async": {"required": False, "type": "str",
                                         "choices": ["enable",
                                                     "disable"]},
                "ipv6_accept_dad": {"required": False, "type": "int"},
                "ipv6_allow_anycast_probe": {"required": False, "type": "str",
                                             "choices": ["enable",
                                                         "disable"]},
                "language": {"required": False, "type": "str",
                             "choices": ["english",
                                         "french",
                                         "spanish",
                                         "portuguese",
                                         "japanese",
                                         "trach",
                                         "simch",
                                         "korean"]},
                "ldapconntimeout": {"required": False, "type": "int"},
                "lldp_reception": {"required": False, "type": "str",
                                   "choices": ["enable",
                                               "disable"]},
                "lldp_transmission": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable"]},
                "log_ssl_connection": {"required": False, "type": "str",
                                       "choices": ["enable",
                                                   "disable"]},
                "log_uuid_address": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "log_uuid_policy": {"required": False, "type": "str",
                                    "choices": ["enable",
                                                "disable"]},
                "login_timestamp": {"required": False, "type": "str",
                                    "choices": ["enable",
                                                "disable"]},
                "management_vdom": {"required": False, "type": "str"},
                "max_dlpstat_memory": {"required": False, "type": "int"},
                "max_route_cache_size": {"required": False, "type": "int"},
                "memory_use_threshold_extreme": {"required": False, "type": "int"},
                "memory_use_threshold_green": {"required": False, "type": "int"},
                "memory_use_threshold_red": {"required": False, "type": "int"},
                "miglog_affinity": {"required": False, "type": "str"},
                "miglogd_children": {"required": False, "type": "int"},
                "multi_factor_authentication": {"required": False, "type": "str",
                                                "choices": ["optional",
                                                            "mandatory"]},
                "ndp_max_entry": {"required": False, "type": "int"},
                "per_user_bwl": {"required": False, "type": "str",
                                 "choices": ["enable",
                                             "disable"]},
                "policy_auth_concurrent": {"required": False, "type": "int"},
                "post_login_banner": {"required": False, "type": "str",
                                      "choices": ["disable",
                                                  "enable"]},
                "pre_login_banner": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "private_data_encryption": {"required": False, "type": "str",
                                            "choices": ["disable",
                                                        "enable"]},
                "proxy_auth_lifetime": {"required": False, "type": "str",
                                        "choices": ["enable",
                                                    "disable"]},
                "proxy_auth_lifetime_timeout": {"required": False, "type": "int"},
                "proxy_auth_timeout": {"required": False, "type": "int"},
                "proxy_re_authentication_mode": {"required": False, "type": "str",
                                                 "choices": ["session",
                                                             "traffic",
                                                             "absolute"]},
                "proxy_worker_count": {"required": False, "type": "int"},
                "radius_port": {"required": False, "type": "int"},
                "reboot_upon_config_restore": {"required": False, "type": "str",
                                               "choices": ["enable",
                                                           "disable"]},
                "refresh": {"required": False, "type": "int"},
                "remoteauthtimeout": {"required": False, "type": "int"},
                "reset_sessionless_tcp": {"required": False, "type": "str",
                                          "choices": ["enable",
                                                      "disable"]},
                "restart_time": {"required": False, "type": "str"},
                "revision_backup_on_logout": {"required": False, "type": "str",
                                              "choices": ["enable",
                                                          "disable"]},
                "revision_image_auto_backup": {"required": False, "type": "str",
                                               "choices": ["enable",
                                                           "disable"]},
                "scanunit_count": {"required": False, "type": "int"},
                "security_rating_result_submission": {"required": False, "type": "str",
                                                      "choices": ["enable",
                                                                  "disable"]},
                "security_rating_run_on_schedule": {"required": False, "type": "str",
                                                    "choices": ["enable",
                                                                "disable"]},
                "send_pmtu_icmp": {"required": False, "type": "str",
                                   "choices": ["enable",
                                               "disable"]},
                "snat_route_change": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable"]},
                "special_file_23_support": {"required": False, "type": "str",
                                            "choices": ["disable",
                                                        "enable"]},
                "ssd_trim_date": {"required": False, "type": "int"},
                "ssd_trim_freq": {"required": False, "type": "str",
                                  "choices": ["never",
                                              "hourly",
                                              "daily",
                                              "weekly",
                                              "monthly"]},
                "ssd_trim_hour": {"required": False, "type": "int"},
                "ssd_trim_min": {"required": False, "type": "int"},
                "ssd_trim_weekday": {"required": False, "type": "str",
                                     "choices": ["sunday",
                                                 "monday",
                                                 "tuesday",
                                                 "wednesday",
                                                 "thursday",
                                                 "friday",
                                                 "saturday"]},
                "ssh_cbc_cipher": {"required": False, "type": "str",
                                   "choices": ["enable",
                                               "disable"]},
                "ssh_hmac_md5": {"required": False, "type": "str",
                                 "choices": ["enable",
                                             "disable"]},
                "ssh_kex_sha1": {"required": False, "type": "str",
                                 "choices": ["enable",
                                             "disable"]},
                "ssh_mac_weak": {"required": False, "type": "str",
                                 "choices": ["enable",
                                             "disable"]},
                "ssl_min_proto_version": {"required": False, "type": "str",
                                          "choices": ["SSLv3",
                                                      "TLSv1",
                                                      "TLSv1-1",
                                                      "TLSv1-2",
                                                      "TLSv1-3"]},
                "ssl_static_key_ciphers": {"required": False, "type": "str",
                                           "choices": ["enable",
                                                       "disable"]},
                "sslvpn_max_worker_count": {"required": False, "type": "int"},
                "sslvpn_plugin_version_check": {"required": False, "type": "str",
                                                "choices": ["enable",
                                                            "disable"]},
                "strict_dirty_session_check": {"required": False, "type": "str",
                                               "choices": ["enable",
                                                           "disable"]},
                "strong_crypto": {"required": False, "type": "str",
                                  "choices": ["enable",
                                              "disable"]},
                "switch_controller": {"required": False, "type": "str",
                                      "choices": ["disable",
                                                  "enable"]},
                "switch_controller_reserved_network": {"required": False, "type": "str"},
                "sys_perf_log_interval": {"required": False, "type": "int"},
                "tcp_halfclose_timer": {"required": False, "type": "int"},
                "tcp_halfopen_timer": {"required": False, "type": "int"},
                "tcp_option": {"required": False, "type": "str",
                               "choices": ["enable",
                                           "disable"]},
                "tcp_timewait_timer": {"required": False, "type": "int"},
                "tftp": {"required": False, "type": "str",
                         "choices": ["enable",
                                     "disable"]},
                "timezone": {"required": False, "type": "str",
                             "choices": ["01",
                                         "02",
                                         "03",
                                         "04",
                                         "05",
                                         "81",
                                         "06",
                                         "07",
                                         "08",
                                         "09",
                                         "10",
                                         "11",
                                         "12",
                                         "13",
                                         "74",
                                         "14",
                                         "77",
                                         "15",
                                         "87",
                                         "16",
                                         "17",
                                         "18",
                                         "19",
                                         "20",
                                         "75",
                                         "21",
                                         "22",
                                         "23",
                                         "24",
                                         "80",
                                         "79",
                                         "25",
                                         "26",
                                         "27",
                                         "28",
                                         "78",
                                         "29",
                                         "30",
                                         "31",
                                         "32",
                                         "33",
                                         "34",
                                         "35",
                                         "36",
                                         "37",
                                         "38",
                                         "83",
                                         "84",
                                         "40",
                                         "85",
                                         "41",
                                         "42",
                                         "43",
                                         "39",
                                         "44",
                                         "46",
                                         "47",
                                         "51",
                                         "48",
                                         "45",
                                         "49",
                                         "50",
                                         "52",
                                         "53",
                                         "54",
                                         "55",
                                         "56",
                                         "57",
                                         "58",
                                         "59",
                                         "60",
                                         "62",
                                         "63",
                                         "61",
                                         "64",
                                         "65",
                                         "66",
                                         "67",
                                         "68",
                                         "69",
                                         "70",
                                         "71",
                                         "72",
                                         "00",
                                         "82",
                                         "73",
                                         "86",
                                         "76"]},
                "traffic_priority": {"required": False, "type": "str",
                                     "choices": ["tos",
                                                 "dscp"]},
                "traffic_priority_level": {"required": False, "type": "str",
                                           "choices": ["low",
                                                       "medium",
                                                       "high"]},
                "two_factor_email_expiry": {"required": False, "type": "int"},
                "two_factor_fac_expiry": {"required": False, "type": "int"},
                "two_factor_ftk_expiry": {"required": False, "type": "int"},
                "two_factor_ftm_expiry": {"required": False, "type": "int"},
                "two_factor_sms_expiry": {"required": False, "type": "int"},
                "udp_idle_timer": {"required": False, "type": "int"},
                "url_filter_affinity": {"required": False, "type": "str"},
                "url_filter_count": {"required": False, "type": "int"},
                "user_server_cert": {"required": False, "type": "str"},
                "vip_arp_range": {"required": False, "type": "str",
                                  "choices": ["unlimited",
                                              "restricted"]},
                "wad_affinity": {"required": False, "type": "str"},
                "wad_csvc_cs_count": {"required": False, "type": "int"},
                "wad_csvc_db_count": {"required": False, "type": "int"},
                "wad_memory_change_granularity": {"required": False, "type": "int"},
                "wad_source_affinity": {"required": False, "type": "str",
                                        "choices": ["disable",
                                                    "enable"]},
                "wad_worker_count": {"required": False, "type": "int"},
                "wifi_ca_certificate": {"required": False, "type": "str"},
                "wifi_certificate": {"required": False, "type": "str"},
                "wimax_4g_usb": {"required": False, "type": "str",
                                 "choices": ["enable",
                                             "disable"]},
                "wireless_controller": {"required": False, "type": "str",
                                        "choices": ["enable",
                                                    "disable"]},
                "wireless_controller_port": {"required": False, "type": "int"}

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

        is_error, has_changed, result = fortios_system(module.params, fos)
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
