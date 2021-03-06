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
module: fortios_system_lldp_network_policy
short_description: Configure LLDP network policy in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify system_lldp feature and network_policy category.
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
    system_lldp_network_policy:
        description:
            - Configure LLDP network policy.
        default: null
        type: dict
        suboptions:
            comment:
                description:
                    - Comment.
                type: str
            guest:
                description:
                    - Guest.
                type: dict
                suboptions:
                    dscp:
                        description:
                            - Differentiated Services Code Point (DSCP) value to advertise.
                        type: int
                    priority:
                        description:
                            - 802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).
                        type: int
                    status:
                        description:
                            - Enable/disable advertising this policy.
                        type: str
                        choices:
                            - disable
                            - enable
                    tag:
                        description:
                            - Advertise tagged or untagged traffic.
                        type: str
                        choices:
                            - none
                            - dot1q
                            - dot1p
                    vlan:
                        description:
                            - 802.1Q VLAN ID to advertise (1 - 4094).
                        type: int
            guest_voice_signaling:
                description:
                    - Guest Voice Signaling.
                type: dict
                suboptions:
                    dscp:
                        description:
                            - Differentiated Services Code Point (DSCP) value to advertise.
                        type: int
                    priority:
                        description:
                            - 802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).
                        type: int
                    status:
                        description:
                            - Enable/disable advertising this policy.
                        type: str
                        choices:
                            - disable
                            - enable
                    tag:
                        description:
                            - Advertise tagged or untagged traffic.
                        type: str
                        choices:
                            - none
                            - dot1q
                            - dot1p
                    vlan:
                        description:
                            - 802.1Q VLAN ID to advertise (1 - 4094).
                        type: int
            name:
                description:
                    - LLDP network policy name.
                required: true
                type: str
            softphone:
                description:
                    - Softphone.
                type: dict
                suboptions:
                    dscp:
                        description:
                            - Differentiated Services Code Point (DSCP) value to advertise.
                        type: int
                    priority:
                        description:
                            - 802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).
                        type: int
                    status:
                        description:
                            - Enable/disable advertising this policy.
                        type: str
                        choices:
                            - disable
                            - enable
                    tag:
                        description:
                            - Advertise tagged or untagged traffic.
                        type: str
                        choices:
                            - none
                            - dot1q
                            - dot1p
                    vlan:
                        description:
                            - 802.1Q VLAN ID to advertise (1 - 4094).
                        type: int
            streaming_video:
                description:
                    - Streaming Video.
                type: dict
                suboptions:
                    dscp:
                        description:
                            - Differentiated Services Code Point (DSCP) value to advertise.
                        type: int
                    priority:
                        description:
                            - 802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).
                        type: int
                    status:
                        description:
                            - Enable/disable advertising this policy.
                        type: str
                        choices:
                            - disable
                            - enable
                    tag:
                        description:
                            - Advertise tagged or untagged traffic.
                        type: str
                        choices:
                            - none
                            - dot1q
                            - dot1p
                    vlan:
                        description:
                            - 802.1Q VLAN ID to advertise (1 - 4094).
                        type: int
            video_conferencing:
                description:
                    - Video Conferencing.
                type: dict
                suboptions:
                    dscp:
                        description:
                            - Differentiated Services Code Point (DSCP) value to advertise.
                        type: int
                    priority:
                        description:
                            - 802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).
                        type: int
                    status:
                        description:
                            - Enable/disable advertising this policy.
                        type: str
                        choices:
                            - disable
                            - enable
                    tag:
                        description:
                            - Advertise tagged or untagged traffic.
                        type: str
                        choices:
                            - none
                            - dot1q
                            - dot1p
                    vlan:
                        description:
                            - 802.1Q VLAN ID to advertise (1 - 4094).
                        type: int
            video_signaling:
                description:
                    - Video Signaling.
                type: dict
                suboptions:
                    dscp:
                        description:
                            - Differentiated Services Code Point (DSCP) value to advertise.
                        type: int
                    priority:
                        description:
                            - 802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).
                        type: int
                    status:
                        description:
                            - Enable/disable advertising this policy.
                        type: str
                        choices:
                            - disable
                            - enable
                    tag:
                        description:
                            - Advertise tagged or untagged traffic.
                        type: str
                        choices:
                            - none
                            - dot1q
                            - dot1p
                    vlan:
                        description:
                            - 802.1Q VLAN ID to advertise (1 - 4094).
                        type: int
            voice:
                description:
                    - Voice.
                type: dict
                suboptions:
                    dscp:
                        description:
                            - Differentiated Services Code Point (DSCP) value to advertise.
                        type: int
                    priority:
                        description:
                            - 802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).
                        type: int
                    status:
                        description:
                            - Enable/disable advertising this policy.
                        type: str
                        choices:
                            - disable
                            - enable
                    tag:
                        description:
                            - Advertise tagged or untagged traffic.
                        type: str
                        choices:
                            - none
                            - dot1q
                            - dot1p
                    vlan:
                        description:
                            - 802.1Q VLAN ID to advertise (1 - 4094).
                        type: int
            voice_signaling:
                description:
                    - Voice signaling.
                type: dict
                suboptions:
                    dscp:
                        description:
                            - Differentiated Services Code Point (DSCP) value to advertise.
                        type: int
                    priority:
                        description:
                            - 802.1P CoS/PCP to advertise (0 - 7; from lowest to highest priority).
                        type: int
                    status:
                        description:
                            - Enable/disable advertising this policy.
                        type: str
                        choices:
                            - disable
                            - enable
                    tag:
                        description:
                            - Advertise tagged or untagged traffic.
                        type: str
                        choices:
                            - none
                            - dot1q
                            - dot1p
                    vlan:
                        description:
                            - 802.1Q VLAN ID to advertise (1 - 4094).
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
  - name: Configure LLDP network policy.
    fortios_system_lldp_network_policy:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_lldp_network_policy:
        comment: "Comment."
        guest:
            dscp: "5"
            priority: "6"
            status: "disable"
            tag: "none"
            vlan: "9"
        guest_voice_signaling:
            dscp: "11"
            priority: "12"
            status: "disable"
            tag: "none"
            vlan: "15"
        name: "default_name_16"
        softphone:
            dscp: "18"
            priority: "19"
            status: "disable"
            tag: "none"
            vlan: "22"
        streaming_video:
            dscp: "24"
            priority: "25"
            status: "disable"
            tag: "none"
            vlan: "28"
        video_conferencing:
            dscp: "30"
            priority: "31"
            status: "disable"
            tag: "none"
            vlan: "34"
        video_signaling:
            dscp: "36"
            priority: "37"
            status: "disable"
            tag: "none"
            vlan: "40"
        voice:
            dscp: "42"
            priority: "43"
            status: "disable"
            tag: "none"
            vlan: "46"
        voice_signaling:
            dscp: "48"
            priority: "49"
            status: "disable"
            tag: "none"
            vlan: "52"

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


def filter_system_lldp_network_policy_data(json):
    option_list = ['comment', 'guest', 'guest_voice_signaling',
                   'name', 'softphone', 'streaming_video',
                   'video_conferencing', 'video_signaling', 'voice',
                   'voice_signaling']
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


def system_lldp_network_policy(data, fos):
    vdom = data['vdom']
    state = data['state']
    system_lldp_network_policy_data = data['system_lldp_network_policy']
    filtered_data = underscore_to_hyphen(filter_system_lldp_network_policy_data(system_lldp_network_policy_data))

    if state == "present":
        return fos.set('system.lldp',
                       'network-policy',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('system.lldp',
                          'network-policy',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_system_lldp(data, fos):

    if data['system_lldp_network_policy']:
        resp = system_lldp_network_policy(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('system_lldp_network_policy'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = 'name'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": True, "type": "str",
                  "choices": ["present", "absent"]},
        "system_lldp_network_policy": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "comment": {"required": False, "type": "str"},
                "guest": {"required": False, "type": "dict",
                          "options": {
                              "dscp": {"required": False, "type": "int"},
                              "priority": {"required": False, "type": "int"},
                              "status": {"required": False, "type": "str",
                                         "choices": ["disable",
                                                     "enable"]},
                              "tag": {"required": False, "type": "str",
                                      "choices": ["none",
                                                  "dot1q",
                                                  "dot1p"]},
                              "vlan": {"required": False, "type": "int"}
                          }},
                "guest_voice_signaling": {"required": False, "type": "dict",
                                          "options": {
                                              "dscp": {"required": False, "type": "int"},
                                              "priority": {"required": False, "type": "int"},
                                              "status": {"required": False, "type": "str",
                                                         "choices": ["disable",
                                                                     "enable"]},
                                              "tag": {"required": False, "type": "str",
                                                      "choices": ["none",
                                                                  "dot1q",
                                                                  "dot1p"]},
                                              "vlan": {"required": False, "type": "int"}
                                          }},
                "name": {"required": True, "type": "str"},
                "softphone": {"required": False, "type": "dict",
                              "options": {
                                  "dscp": {"required": False, "type": "int"},
                                  "priority": {"required": False, "type": "int"},
                                  "status": {"required": False, "type": "str",
                                             "choices": ["disable",
                                                         "enable"]},
                                  "tag": {"required": False, "type": "str",
                                          "choices": ["none",
                                                      "dot1q",
                                                      "dot1p"]},
                                  "vlan": {"required": False, "type": "int"}
                              }},
                "streaming_video": {"required": False, "type": "dict",
                                    "options": {
                                        "dscp": {"required": False, "type": "int"},
                                        "priority": {"required": False, "type": "int"},
                                        "status": {"required": False, "type": "str",
                                                   "choices": ["disable",
                                                               "enable"]},
                                        "tag": {"required": False, "type": "str",
                                                "choices": ["none",
                                                            "dot1q",
                                                            "dot1p"]},
                                        "vlan": {"required": False, "type": "int"}
                                    }},
                "video_conferencing": {"required": False, "type": "dict",
                                       "options": {
                                           "dscp": {"required": False, "type": "int"},
                                           "priority": {"required": False, "type": "int"},
                                           "status": {"required": False, "type": "str",
                                                      "choices": ["disable",
                                                                  "enable"]},
                                           "tag": {"required": False, "type": "str",
                                                   "choices": ["none",
                                                               "dot1q",
                                                               "dot1p"]},
                                           "vlan": {"required": False, "type": "int"}
                                       }},
                "video_signaling": {"required": False, "type": "dict",
                                    "options": {
                                        "dscp": {"required": False, "type": "int"},
                                        "priority": {"required": False, "type": "int"},
                                        "status": {"required": False, "type": "str",
                                                   "choices": ["disable",
                                                               "enable"]},
                                        "tag": {"required": False, "type": "str",
                                                "choices": ["none",
                                                            "dot1q",
                                                            "dot1p"]},
                                        "vlan": {"required": False, "type": "int"}
                                    }},
                "voice": {"required": False, "type": "dict",
                          "options": {
                              "dscp": {"required": False, "type": "int"},
                              "priority": {"required": False, "type": "int"},
                              "status": {"required": False, "type": "str",
                                         "choices": ["disable",
                                                     "enable"]},
                              "tag": {"required": False, "type": "str",
                                      "choices": ["none",
                                                  "dot1q",
                                                  "dot1p"]},
                              "vlan": {"required": False, "type": "int"}
                          }},
                "voice_signaling": {"required": False, "type": "dict",
                                    "options": {
                                        "dscp": {"required": False, "type": "int"},
                                        "priority": {"required": False, "type": "int"},
                                        "status": {"required": False, "type": "str",
                                                   "choices": ["disable",
                                                               "enable"]},
                                        "tag": {"required": False, "type": "str",
                                                "choices": ["none",
                                                            "dot1q",
                                                            "dot1p"]},
                                        "vlan": {"required": False, "type": "int"}
                                    }}

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

        is_error, has_changed, result = fortios_system_lldp(module.params, fos)
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
