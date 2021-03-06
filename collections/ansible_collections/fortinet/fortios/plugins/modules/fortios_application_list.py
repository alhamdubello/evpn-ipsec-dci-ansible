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
module: fortios_application_list
short_description: Configure application control lists in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify application feature and list category.
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
    application_list:
        description:
            - Configure application control lists.
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
            app_replacemsg:
                description:
                    - Enable/disable replacement messages for blocked applications.
                type: str
                choices:
                    - disable
                    - enable
            comment:
                description:
                    - comments
                type: str
            control_default_network_services:
                description:
                    - Enable/disable enforcement of protocols over selected ports.
                type: str
                choices:
                    - disable
                    - enable
            deep_app_inspection:
                description:
                    - Enable/disable deep application inspection.
                type: str
                choices:
                    - disable
                    - enable
            default_network_services:
                description:
                    - Default network service entries.
                type: list
                suboptions:
                    id:
                        description:
                            - Entry ID.
                        required: true
                        type: int
                    port:
                        description:
                            - Port number.
                        type: int
                    services:
                        description:
                            - Network protocols.
                        type: str
                        choices:
                            - http
                            - ssh
                            - telnet
                            - ftp
                            - dns
                            - smtp
                            - pop3
                            - imap
                            - snmp
                            - nntp
                            - https
                    violation_action:
                        description:
                            - Action for protocols not white listed under selected port.
                        type: str
                        choices:
                            - pass
                            - monitor
                            - block
            enforce_default_app_port:
                description:
                    - Enable/disable default application port enforcement for allowed applications.
                type: str
                choices:
                    - disable
                    - enable
            entries:
                description:
                    - Application list entries.
                type: list
                suboptions:
                    action:
                        description:
                            - Pass or block traffic, or reset connection for traffic from this application.
                        type: str
                        choices:
                            - pass
                            - block
                            - reset
                    application:
                        description:
                            - ID of allowed applications.
                        type: list
                        suboptions:
                            id:
                                description:
                                    - Application IDs.
                                required: true
                                type: int
                    behavior:
                        description:
                            - Application behavior filter.
                        type: str
                    category:
                        description:
                            - Category ID list.
                        type: list
                        suboptions:
                            id:
                                description:
                                    - Application category ID.
                                required: true
                                type: int
                    id:
                        description:
                            - Entry ID.
                        required: true
                        type: int
                    log:
                        description:
                            - Enable/disable logging for this application list.
                        type: str
                        choices:
                            - disable
                            - enable
                    log_packet:
                        description:
                            - Enable/disable packet logging.
                        type: str
                        choices:
                            - disable
                            - enable
                    parameters:
                        description:
                            - Application parameters.
                        type: list
                        suboptions:
                            id:
                                description:
                                    - Parameter tuple ID.
                                required: true
                                type: int
                            members:
                                description:
                                    - Parameter tuple members.
                                type: list
                                suboptions:
                                    id:
                                        description:
                                            - Parameter.
                                        required: true
                                        type: int
                                    name:
                                        description:
                                            - Parameter name.
                                        type: str
                                    value:
                                        description:
                                            - Parameter value.
                                        type: str
                    per_ip_shaper:
                        description:
                            - Per-IP traffic shaper. Source firewall.shaper.per-ip-shaper.name.
                        type: str
                    popularity:
                        description:
                            - Application popularity filter (1 - 5, from least to most popular).
                        type: str
                        choices:
                            - 1
                            - 2
                            - 3
                            - 4
                            - 5
                    protocols:
                        description:
                            - Application protocol filter.
                        type: str
                    quarantine:
                        description:
                            - Quarantine method.
                        type: str
                        choices:
                            - none
                            - attacker
                    quarantine_expiry:
                        description:
                            - Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m). Requires quarantine set to attacker.
                        type: str
                    quarantine_log:
                        description:
                            - Enable/disable quarantine logging.
                        type: str
                        choices:
                            - disable
                            - enable
                    rate_count:
                        description:
                            - Count of the rate.
                        type: int
                    rate_duration:
                        description:
                            - Duration (sec) of the rate.
                        type: int
                    rate_mode:
                        description:
                            - Rate limit mode.
                        type: str
                        choices:
                            - periodical
                            - continuous
                    rate_track:
                        description:
                            - Track the packet protocol field.
                        type: str
                        choices:
                            - none
                            - src-ip
                            - dest-ip
                            - dhcp-client-mac
                            - dns-domain
                    risk:
                        description:
                            - Risk, or impact, of allowing traffic from this application to occur (1 - 5; Low, Elevated, Medium, High, and Critical).
                        type: list
                        suboptions:
                            level:
                                description:
                                    - Risk, or impact, of allowing traffic from this application to occur (1 - 5; Low, Elevated, Medium, High, and Critical).
                                required: true
                                type: int
                    session_ttl:
                        description:
                            - Session TTL (0 = default).
                        type: int
                    shaper:
                        description:
                            - Traffic shaper. Source firewall.shaper.traffic-shaper.name.
                        type: str
                    shaper_reverse:
                        description:
                            - Reverse traffic shaper. Source firewall.shaper.traffic-shaper.name.
                        type: str
                    sub_category:
                        description:
                            - Application Sub-category ID list.
                        type: list
                        suboptions:
                            id:
                                description:
                                    - Application sub-category ID.
                                required: true
                                type: int
                    technology:
                        description:
                            - Application technology filter.
                        type: str
                    vendor:
                        description:
                            - Application vendor filter.
                        type: str
            extended_log:
                description:
                    - Enable/disable extended logging.
                type: str
                choices:
                    - enable
                    - disable
            force_inclusion_ssl_di_sigs:
                description:
                    - Enable/disable forced inclusion of SSL deep inspection signatures.
                type: str
                choices:
                    - disable
                    - enable
            name:
                description:
                    - List name.
                required: true
                type: str
            options:
                description:
                    - Basic application protocol signatures allowed by default.
                type: str
                choices:
                    - allow-dns
                    - allow-icmp
                    - allow-http
                    - allow-ssl
                    - allow-quic
            other_application_action:
                description:
                    - Action for other applications.
                type: str
                choices:
                    - pass
                    - block
            other_application_log:
                description:
                    - Enable/disable logging for other applications.
                type: str
                choices:
                    - disable
                    - enable
            p2p_black_list:
                description:
                    - P2P applications to be black listed.
                type: str
                choices:
                    - skype
                    - edonkey
                    - bittorrent
            replacemsg_group:
                description:
                    - Replacement message group. Source system.replacemsg-group.name.
                type: str
            unknown_application_action:
                description:
                    - Pass or block traffic from unknown applications.
                type: str
                choices:
                    - pass
                    - block
            unknown_application_log:
                description:
                    - Enable/disable logging for unknown applications.
                type: str
                choices:
                    - disable
                    - enable
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
  - name: Configure application control lists.
    fortios_application_list:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      application_list:
        app_replacemsg: "disable"
        comment: "comments"
        control_default_network_services: "disable"
        deep_app_inspection: "disable"
        default_network_services:
         -
            id:  "8"
            port: "9"
            services: "http"
            violation_action: "pass"
        enforce_default_app_port: "disable"
        entries:
         -
            action: "pass"
            application:
             -
                id:  "16"
            behavior: "<your_own_value>"
            category:
             -
                id:  "19"
            id:  "20"
            log: "disable"
            log_packet: "disable"
            parameters:
             -
                id:  "24"
                members:
                 -
                    id:  "26"
                    name: "default_name_27"
                    value: "<your_own_value>"
            per_ip_shaper: "<your_own_value> (source firewall.shaper.per-ip-shaper.name)"
            popularity: "1"
            protocols: "<your_own_value>"
            quarantine: "none"
            quarantine_expiry: "<your_own_value>"
            quarantine_log: "disable"
            rate_count: "35"
            rate_duration: "36"
            rate_mode: "periodical"
            rate_track: "none"
            risk:
             -
                level: "40"
            session_ttl: "41"
            shaper: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
            shaper_reverse: "<your_own_value> (source firewall.shaper.traffic-shaper.name)"
            sub_category:
             -
                id:  "45"
            technology: "<your_own_value>"
            vendor: "<your_own_value>"
        extended_log: "enable"
        force_inclusion_ssl_di_sigs: "disable"
        name: "default_name_50"
        options: "allow-dns"
        other_application_action: "pass"
        other_application_log: "disable"
        p2p_black_list: "skype"
        replacemsg_group: "<your_own_value> (source system.replacemsg-group.name)"
        unknown_application_action: "pass"
        unknown_application_log: "disable"

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


def filter_application_list_data(json):
    option_list = ['app_replacemsg', 'comment', 'control_default_network_services',
                   'deep_app_inspection', 'default_network_services', 'enforce_default_app_port',
                   'entries', 'extended_log', 'force_inclusion_ssl_di_sigs',
                   'name', 'options', 'other_application_action',
                   'other_application_log', 'p2p_black_list', 'replacemsg_group',
                   'unknown_application_action', 'unknown_application_log']
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


def application_list(data, fos):
    vdom = data['vdom']
    if 'state' in data and data['state']:
        state = data['state']
    elif 'state' in data['application_list'] and data['application_list']['state']:
        state = data['application_list']['state']
    else:
        state = True
    application_list_data = data['application_list']
    filtered_data = underscore_to_hyphen(filter_application_list_data(application_list_data))

    if state == "present":
        return fos.set('application',
                       'list',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('application',
                          'list',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_application(data, fos):

    if data['application_list']:
        resp = application_list(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('application_list'))

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
        "application_list": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "state": {"required": False, "type": "str",
                          "choices": ["present", "absent"]},
                "app_replacemsg": {"required": False, "type": "str",
                                   "choices": ["disable",
                                               "enable"]},
                "comment": {"required": False, "type": "str"},
                "control_default_network_services": {"required": False, "type": "str",
                                                     "choices": ["disable",
                                                                 "enable"]},
                "deep_app_inspection": {"required": False, "type": "str",
                                        "choices": ["disable",
                                                    "enable"]},
                "default_network_services": {"required": False, "type": "list",
                                             "options": {
                                                 "id": {"required": True, "type": "int"},
                                                 "port": {"required": False, "type": "int"},
                                                 "services": {"required": False, "type": "str",
                                                              "choices": ["http",
                                                                          "ssh",
                                                                          "telnet",
                                                                          "ftp",
                                                                          "dns",
                                                                          "smtp",
                                                                          "pop3",
                                                                          "imap",
                                                                          "snmp",
                                                                          "nntp",
                                                                          "https"]},
                                                 "violation_action": {"required": False, "type": "str",
                                                                      "choices": ["pass",
                                                                                  "monitor",
                                                                                  "block"]}
                                             }},
                "enforce_default_app_port": {"required": False, "type": "str",
                                             "choices": ["disable",
                                                         "enable"]},
                "entries": {"required": False, "type": "list",
                            "options": {
                                "action": {"required": False, "type": "str",
                                           "choices": ["pass",
                                                       "block",
                                                       "reset"]},
                                "application": {"required": False, "type": "list",
                                                "options": {
                                                    "id": {"required": True, "type": "int"}
                                                }},
                                "behavior": {"required": False, "type": "str"},
                                "category": {"required": False, "type": "list",
                                             "options": {
                                                 "id": {"required": True, "type": "int"}
                                             }},
                                "id": {"required": True, "type": "int"},
                                "log": {"required": False, "type": "str",
                                        "choices": ["disable",
                                                    "enable"]},
                                "log_packet": {"required": False, "type": "str",
                                               "choices": ["disable",
                                                           "enable"]},
                                "parameters": {"required": False, "type": "list",
                                               "options": {
                                                   "id": {"required": True, "type": "int"},
                                                   "members": {"required": False, "type": "list",
                                                               "options": {
                                                                   "id": {"required": True, "type": "int"},
                                                                   "name": {"required": False, "type": "str"},
                                                                   "value": {"required": False, "type": "str"}
                                                               }}
                                               }},
                                "per_ip_shaper": {"required": False, "type": "str"},
                                "popularity": {"required": False, "type": "str",
                                               "choices": ["1",
                                                           "2",
                                                           "3",
                                                           "4",
                                                           "5"]},
                                "protocols": {"required": False, "type": "str"},
                                "quarantine": {"required": False, "type": "str",
                                               "choices": ["none",
                                                           "attacker"]},
                                "quarantine_expiry": {"required": False, "type": "str"},
                                "quarantine_log": {"required": False, "type": "str",
                                                   "choices": ["disable",
                                                               "enable"]},
                                "rate_count": {"required": False, "type": "int"},
                                "rate_duration": {"required": False, "type": "int"},
                                "rate_mode": {"required": False, "type": "str",
                                              "choices": ["periodical",
                                                          "continuous"]},
                                "rate_track": {"required": False, "type": "str",
                                               "choices": ["none",
                                                           "src-ip",
                                                           "dest-ip",
                                                           "dhcp-client-mac",
                                                           "dns-domain"]},
                                "risk": {"required": False, "type": "list",
                                         "options": {
                                             "level": {"required": True, "type": "int"}
                                         }},
                                "session_ttl": {"required": False, "type": "int"},
                                "shaper": {"required": False, "type": "str"},
                                "shaper_reverse": {"required": False, "type": "str"},
                                "sub_category": {"required": False, "type": "list",
                                                 "options": {
                                                     "id": {"required": True, "type": "int"}
                                                 }},
                                "technology": {"required": False, "type": "str"},
                                "vendor": {"required": False, "type": "str"}
                            }},
                "extended_log": {"required": False, "type": "str",
                                 "choices": ["enable",
                                             "disable"]},
                "force_inclusion_ssl_di_sigs": {"required": False, "type": "str",
                                                "choices": ["disable",
                                                            "enable"]},
                "name": {"required": True, "type": "str"},
                "options": {"required": False, "type": "str",
                            "choices": ["allow-dns",
                                        "allow-icmp",
                                        "allow-http",
                                        "allow-ssl",
                                        "allow-quic"]},
                "other_application_action": {"required": False, "type": "str",
                                             "choices": ["pass",
                                                         "block"]},
                "other_application_log": {"required": False, "type": "str",
                                          "choices": ["disable",
                                                      "enable"]},
                "p2p_black_list": {"required": False, "type": "str",
                                   "choices": ["skype",
                                               "edonkey",
                                               "bittorrent"]},
                "replacemsg_group": {"required": False, "type": "str"},
                "unknown_application_action": {"required": False, "type": "str",
                                               "choices": ["pass",
                                                           "block"]},
                "unknown_application_log": {"required": False, "type": "str",
                                            "choices": ["disable",
                                                        "enable"]}

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

        is_error, has_changed, result = fortios_application(module.params, fos)
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
