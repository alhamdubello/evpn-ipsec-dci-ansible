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
module: fortios_firewall_dos_policy
short_description: Configure IPv4 DoS policies in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify firewall feature and dos_policy category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.4.0
version_added: "2.10"
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
        type: str
        required: true
        choices:
            - present
            - absent
    firewall_dos_policy:
        description:
            - Configure IPv4 DoS policies.
        default: null
        type: dict
        suboptions:
            anomaly:
                description:
                    - Anomaly name.
                type: list
                suboptions:
                    action:
                        description:
                            - Action taken when the threshold is reached.
                        type: str
                        choices:
                            - pass
                            - block
                    log:
                        description:
                            - Enable/disable anomaly logging.
                        type: str
                        choices:
                            - enable
                            - disable
                    name:
                        description:
                            - Anomaly name.
                        required: true
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
                    status:
                        description:
                            - Enable/disable this anomaly.
                        type: str
                        choices:
                            - disable
                            - enable
                    threshold:
                        description:
                            - Anomaly threshold. Number of detected instances per minute that triggers the anomaly action.
                        type: int
                    threshold(default):
                        description:
                            - Number of detected instances per minute which triggers action (1 - 2147483647). Note that each anomaly has a different threshold
                               value assigned to it.
                        type: int
            comments:
                description:
                    - Comment.
                type: str
            dstaddr:
                description:
                    - Destination address name from available addresses.
                type: list
                suboptions:
                    name:
                        description:
                            - Address name. Source firewall.address.name firewall.addrgrp.name.
                        required: true
                        type: str
            interface:
                description:
                    - Incoming interface name from available interfaces. Source system.zone.name system.interface.name.
                type: str
            policyid:
                description:
                    - Policy ID.
                required: true
                type: int
            service:
                description:
                    - Service object from available options.
                type: list
                suboptions:
                    name:
                        description:
                            - Service name. Source firewall.service.custom.name firewall.service.group.name.
                        required: true
                        type: str
            srcaddr:
                description:
                    - Source address name from available addresses.
                type: list
                suboptions:
                    name:
                        description:
                            - Service name. Source firewall.address.name firewall.addrgrp.name.
                        required: true
                        type: str
            status:
                description:
                    - Enable/disable this policy.
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
  - name: Configure IPv4 DoS policies.
    fortios_firewall_dos_policy:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_dos_policy:
        anomaly:
         -
            action: "pass"
            log: "enable"
            name: "default_name_6"
            quarantine: "none"
            quarantine_expiry: "<your_own_value>"
            quarantine_log: "disable"
            status: "disable"
            threshold: "11"
            threshold(default): "12"
        comments: "<your_own_value>"
        dstaddr:
         -
            name: "default_name_15 (source firewall.address.name firewall.addrgrp.name)"
        interface: "<your_own_value> (source system.zone.name system.interface.name)"
        policyid: "17"
        service:
         -
            name: "default_name_19 (source firewall.service.custom.name firewall.service.group.name)"
        srcaddr:
         -
            name: "default_name_21 (source firewall.address.name firewall.addrgrp.name)"
        status: "enable"

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


def filter_firewall_dos_policy_data(json):
    option_list = ['anomaly', 'comments', 'dstaddr',
                   'interface', 'policyid', 'service',
                   'srcaddr', 'status']
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


def firewall_dos_policy(data, fos):
    vdom = data['vdom']
    state = data['state']
    firewall_dos_policy_data = data['firewall_dos_policy']
    filtered_data = underscore_to_hyphen(filter_firewall_dos_policy_data(firewall_dos_policy_data))

    if state == "present":
        return fos.set('firewall',
                       'DoS-policy',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('firewall',
                          'DoS-policy',
                          mkey=filtered_data['policyid'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_firewall(data, fos):

    if data['firewall_dos_policy']:
        resp = firewall_dos_policy(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('firewall_dos_policy'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = 'policyid'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": True, "type": "str",
                  "choices": ["present", "absent"]},
        "firewall_dos_policy": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "anomaly": {"required": False, "type": "list",
                            "options": {
                                "action": {"required": False, "type": "str",
                                           "choices": ["pass",
                                                       "block"]},
                                "log": {"required": False, "type": "str",
                                        "choices": ["enable",
                                                    "disable"]},
                                "name": {"required": True, "type": "str"},
                                "quarantine": {"required": False, "type": "str",
                                               "choices": ["none",
                                                           "attacker"]},
                                "quarantine_expiry": {"required": False, "type": "str"},
                                "quarantine_log": {"required": False, "type": "str",
                                                   "choices": ["disable",
                                                               "enable"]},
                                "status": {"required": False, "type": "str",
                                           "choices": ["disable",
                                                       "enable"]},
                                "threshold": {"required": False, "type": "int"},
                                "threshold(default)": {"required": False, "type": "int"}
                            }},
                "comments": {"required": False, "type": "str"},
                "dstaddr": {"required": False, "type": "list",
                            "options": {
                                "name": {"required": True, "type": "str"}
                            }},
                "interface": {"required": False, "type": "str"},
                "policyid": {"required": True, "type": "int"},
                "service": {"required": False, "type": "list",
                            "options": {
                                "name": {"required": True, "type": "str"}
                            }},
                "srcaddr": {"required": False, "type": "list",
                            "options": {
                                "name": {"required": True, "type": "str"}
                            }},
                "status": {"required": False, "type": "str",
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
