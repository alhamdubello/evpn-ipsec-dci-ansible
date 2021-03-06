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
module: fortios_switch_controller_global
short_description: Configure FortiSwitch global settings in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify switch_controller feature and global category.
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

    switch_controller_global:
        description:
            - Configure FortiSwitch global settings.
        default: null
        type: dict
        suboptions:
            allow_multiple_interfaces:
                description:
                    - Enable/disable multiple FortiLink interfaces for redundant connections between a managed FortiSwitch and FortiGate.
                type: str
                choices:
                    - enable
                    - disable
            bounce_quarantined_link:
                description:
                    - Enable/disable bouncing (administratively bring the link down, up) of a switch port where a quarantined device was seen last. Helps to
                       re-initiate the DHCP process for a device.
                type: str
                choices:
                    - disable
                    - enable
            custom_command:
                description:
                    - List of custom commands to be pushed to all FortiSwitches in the VDOM.
                type: list
                suboptions:
                    command_entry:
                        description:
                            - List of FortiSwitch commands.
                        type: str
                    command_name:
                        description:
                            - Name of custom command to push to all FortiSwitches in VDOM. Source switch-controller.custom-command.command-name.
                        type: str
            default_virtual_switch_vlan:
                description:
                    - Default VLAN for ports when added to the virtual-switch. Source system.interface.name.
                type: str
            disable_discovery:
                description:
                    - Prevent this FortiSwitch from discovering.
                type: list
                suboptions:
                    name:
                        description:
                            - Managed device ID.
                        required: true
                        type: str
            https_image_push:
                description:
                    - Enable/disable image push to FortiSwitch using HTTPS.
                type: str
                choices:
                    - enable
                    - disable
            log_mac_limit_violations:
                description:
                    - Enable/disable logs for Learning Limit Violations.
                type: str
                choices:
                    - enable
                    - disable
            mac_aging_interval:
                description:
                    - Time after which an inactive MAC is aged out (10 - 1000000 sec).
                type: int
            mac_event_logging:
                description:
                    - Enable/disable MAC address event logging.
                type: str
                choices:
                    - enable
                    - disable
            mac_retention_period:
                description:
                    - Time in hours after which an inactive MAC is removed from client DB (0 = aged out based on mac-aging-interval).
                type: int
            mac_violation_timer:
                description:
                    - Set timeout for Learning Limit Violations (0 = disabled).
                type: int
            quarantine_mode:
                description:
                    - Quarantine mode.
                type: str
                choices:
                    - by-vlan
                    - by-redirect
            sn_dns_resolution:
                description:
                    - Enable/disable DNS resolution of the FortiSwitch unit"s IP address by use of its serial number.
                type: str
                choices:
                    - enable
                    - disable
            vlan_all_mode:
                description:
                    - VLAN configuration mode, user-defined-vlans or all-possible-vlans.
                type: str
                choices:
                    - all
                    - defined
            vlan_optimization:
                description:
                    - FortiLink VLAN optimization.
                type: str
                choices:
                    - enable
                    - disable
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
  - name: Configure FortiSwitch global settings.
    fortios_switch_controller_global:
      vdom:  "{{ vdom }}"
      switch_controller_global:
        allow_multiple_interfaces: "enable"
        bounce_quarantined_link: "disable"
        custom_command:
         -
            command_entry: "<your_own_value>"
            command_name: "<your_own_value> (source switch-controller.custom-command.command-name)"
        default_virtual_switch_vlan: "<your_own_value> (source system.interface.name)"
        disable_discovery:
         -
            name: "default_name_10"
        https_image_push: "enable"
        log_mac_limit_violations: "enable"
        mac_aging_interval: "13"
        mac_event_logging: "enable"
        mac_retention_period: "15"
        mac_violation_timer: "16"
        quarantine_mode: "by-vlan"
        sn_dns_resolution: "enable"
        vlan_all_mode: "all"
        vlan_optimization: "enable"

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


def filter_switch_controller_global_data(json):
    option_list = ['allow_multiple_interfaces', 'bounce_quarantined_link', 'custom_command',
                   'default_virtual_switch_vlan', 'disable_discovery', 'https_image_push',
                   'log_mac_limit_violations', 'mac_aging_interval', 'mac_event_logging',
                   'mac_retention_period', 'mac_violation_timer', 'quarantine_mode',
                   'sn_dns_resolution', 'vlan_all_mode', 'vlan_optimization']
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


def switch_controller_global(data, fos):
    vdom = data['vdom']
    switch_controller_global_data = data['switch_controller_global']
    filtered_data = underscore_to_hyphen(filter_switch_controller_global_data(switch_controller_global_data))

    return fos.set('switch-controller',
                   'global',
                   data=filtered_data,
                   vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_switch_controller(data, fos):

    if data['switch_controller_global']:
        resp = switch_controller_global(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('switch_controller_global'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = None
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "switch_controller_global": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "allow_multiple_interfaces": {"required": False, "type": "str",
                                              "choices": ["enable",
                                                          "disable"]},
                "bounce_quarantined_link": {"required": False, "type": "str",
                                            "choices": ["disable",
                                                        "enable"]},
                "custom_command": {"required": False, "type": "list",
                                   "options": {
                                       "command_entry": {"required": False, "type": "str"},
                                       "command_name": {"required": False, "type": "str"}
                                   }},
                "default_virtual_switch_vlan": {"required": False, "type": "str"},
                "disable_discovery": {"required": False, "type": "list",
                                      "options": {
                                          "name": {"required": True, "type": "str"}
                                      }},
                "https_image_push": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "log_mac_limit_violations": {"required": False, "type": "str",
                                             "choices": ["enable",
                                                         "disable"]},
                "mac_aging_interval": {"required": False, "type": "int"},
                "mac_event_logging": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable"]},
                "mac_retention_period": {"required": False, "type": "int"},
                "mac_violation_timer": {"required": False, "type": "int"},
                "quarantine_mode": {"required": False, "type": "str",
                                    "choices": ["by-vlan",
                                                "by-redirect"]},
                "sn_dns_resolution": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable"]},
                "vlan_all_mode": {"required": False, "type": "str",
                                  "choices": ["all",
                                              "defined"]},
                "vlan_optimization": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable"]}

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

        is_error, has_changed, result = fortios_switch_controller(module.params, fos)
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
