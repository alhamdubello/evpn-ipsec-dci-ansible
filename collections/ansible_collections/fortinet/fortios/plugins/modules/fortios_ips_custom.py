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
module: fortios_ips_custom
short_description: Configure IPS custom signature in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify ips feature and custom category.
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
    ips_custom:
        description:
            - Configure IPS custom signature.
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
                    - Default action (pass or block) for this signature.
                type: str
                choices:
                    - pass
                    - block
            application:
                description:
                    - Applications to be protected. Blank for all applications.
                type: str
            comment:
                description:
                    - Comment.
                type: str
            location:
                description:
                    - Protect client or server traffic.
                type: str
            log:
                description:
                    - Enable/disable logging.
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
            os:
                description:
                    - Operating system(s) that the signature protects. Blank for all operating systems.
                type: str
            protocol:
                description:
                    - Protocol(s) that the signature scans. Blank for all protocols.
                type: str
            rule_id:
                description:
                    - Signature ID.
                type: int
            severity:
                description:
                    - Relative severity of the signature, from info to critical. Log messages generated by the signature include the severity.
                type: str
            signature:
                description:
                    - Custom signature enclosed in single quotes.
                type: str
            status:
                description:
                    - Enable/disable this signature.
                type: str
                choices:
                    - disable
                    - enable
            tag:
                description:
                    - Signature tag.
                required: true
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
  - name: Configure IPS custom signature.
    fortios_ips_custom:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      ips_custom:
        action: "pass"
        application: "<your_own_value>"
        comment: "Comment."
        location: "<your_own_value>"
        log: "disable"
        log_packet: "disable"
        os: "<your_own_value>"
        protocol: "<your_own_value>"
        rule_id: "11"
        severity: "<your_own_value>"
        signature: "<your_own_value>"
        status: "disable"
        tag: "<your_own_value>"

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


def filter_ips_custom_data(json):
    option_list = ['action', 'application', 'comment',
                   'location', 'log', 'log_packet',
                   'os', 'protocol', 'rule_id',
                   'severity', 'signature', 'status',
                   'tag']
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


def ips_custom(data, fos):
    vdom = data['vdom']
    if 'state' in data and data['state']:
        state = data['state']
    elif 'state' in data['ips_custom'] and data['ips_custom']['state']:
        state = data['ips_custom']['state']
    else:
        state = True
    ips_custom_data = data['ips_custom']
    filtered_data = underscore_to_hyphen(filter_ips_custom_data(ips_custom_data))

    if state == "present":
        return fos.set('ips',
                       'custom',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('ips',
                          'custom',
                          mkey=filtered_data['tag'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_ips(data, fos):

    if data['ips_custom']:
        resp = ips_custom(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('ips_custom'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = 'tag'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": False, "type": "str",
                  "choices": ["present", "absent"]},
        "ips_custom": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "state": {"required": False, "type": "str",
                          "choices": ["present", "absent"]},
                "action": {"required": False, "type": "str",
                           "choices": ["pass",
                                       "block"]},
                "application": {"required": False, "type": "str"},
                "comment": {"required": False, "type": "str"},
                "location": {"required": False, "type": "str"},
                "log": {"required": False, "type": "str",
                        "choices": ["disable",
                                    "enable"]},
                "log_packet": {"required": False, "type": "str",
                               "choices": ["disable",
                                           "enable"]},
                "os": {"required": False, "type": "str"},
                "protocol": {"required": False, "type": "str"},
                "rule_id": {"required": False, "type": "int"},
                "severity": {"required": False, "type": "str"},
                "signature": {"required": False, "type": "str"},
                "status": {"required": False, "type": "str",
                           "choices": ["disable",
                                       "enable"]},
                "tag": {"required": True, "type": "str"}

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

        is_error, has_changed, result = fortios_ips(module.params, fos)
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
