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
module: fortios_firewall_interface_policy
short_description: Configure IPv4 interface policies in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify firewall feature and interface_policy category.
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
    firewall_interface_policy:
        description:
            - Configure IPv4 interface policies.
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
            application_list:
                description:
                    - Application list name. Source application.list.name.
                type: str
            application_list_status:
                description:
                    - Enable/disable application control.
                type: str
                choices:
                    - enable
                    - disable
            av_profile:
                description:
                    - Antivirus profile. Source antivirus.profile.name.
                type: str
            av_profile_status:
                description:
                    - Enable/disable antivirus.
                type: str
                choices:
                    - enable
                    - disable
            comments:
                description:
                    - Comments.
                type: str
            dlp_sensor:
                description:
                    - DLP sensor name. Source dlp.sensor.name.
                type: str
            dlp_sensor_status:
                description:
                    - Enable/disable DLP.
                type: str
                choices:
                    - enable
                    - disable
            dsri:
                description:
                    - Enable/disable DSRI.
                type: str
                choices:
                    - enable
                    - disable
            dstaddr:
                description:
                    - Address object to limit traffic monitoring to network traffic sent to the specified address or range.
                type: list
                suboptions:
                    name:
                        description:
                            - Address name. Source firewall.address.name firewall.addrgrp.name.
                        required: true
                        type: str
            emailfilter_profile:
                description:
                    - Email filter profile. Source emailfilter.profile.name.
                type: str
            emailfilter_profile_status:
                description:
                    - Enable/disable email filter.
                type: str
                choices:
                    - enable
                    - disable
            interface:
                description:
                    - Monitored interface name from available interfaces. Source system.zone.name system.interface.name.
                type: str
            ips_sensor:
                description:
                    - IPS sensor name. Source ips.sensor.name.
                type: str
            ips_sensor_status:
                description:
                    - Enable/disable IPS.
                type: str
                choices:
                    - enable
                    - disable
            logtraffic:
                description:
                    - 'Logging type to be used in this policy (Options: all | utm | disable).'
                type: str
                choices:
                    - all
                    - utm
                    - disable
            policyid:
                description:
                    - Policy ID (0 - 4294967295).
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
                    - Address object to limit traffic monitoring to network traffic sent from the specified address or range.
                type: list
                suboptions:
                    name:
                        description:
                            - Address name. Source firewall.address.name firewall.addrgrp.name.
                        required: true
                        type: str
            status:
                description:
                    - Enable/disable this policy.
                type: str
                choices:
                    - enable
                    - disable
            webfilter_profile:
                description:
                    - Web filter profile. Source webfilter.profile.name.
                type: str
            webfilter_profile_status:
                description:
                    - Enable/disable web filtering.
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
  - name: Configure IPv4 interface policies.
    fortios_firewall_interface_policy:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_interface_policy:
        application_list: "<your_own_value> (source application.list.name)"
        application_list_status: "enable"
        av_profile: "<your_own_value> (source antivirus.profile.name)"
        av_profile_status: "enable"
        comments: "<your_own_value>"
        dlp_sensor: "<your_own_value> (source dlp.sensor.name)"
        dlp_sensor_status: "enable"
        dsri: "enable"
        dstaddr:
         -
            name: "default_name_12 (source firewall.address.name firewall.addrgrp.name)"
        emailfilter_profile: "<your_own_value> (source emailfilter.profile.name)"
        emailfilter_profile_status: "enable"
        interface: "<your_own_value> (source system.zone.name system.interface.name)"
        ips_sensor: "<your_own_value> (source ips.sensor.name)"
        ips_sensor_status: "enable"
        logtraffic: "all"
        policyid: "19"
        service:
         -
            name: "default_name_21 (source firewall.service.custom.name firewall.service.group.name)"
        srcaddr:
         -
            name: "default_name_23 (source firewall.address.name firewall.addrgrp.name)"
        status: "enable"
        webfilter_profile: "<your_own_value> (source webfilter.profile.name)"
        webfilter_profile_status: "enable"

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


def filter_firewall_interface_policy_data(json):
    option_list = ['application_list', 'application_list_status', 'av_profile',
                   'av_profile_status', 'comments', 'dlp_sensor',
                   'dlp_sensor_status', 'dsri', 'dstaddr',
                   'emailfilter_profile', 'emailfilter_profile_status', 'interface',
                   'ips_sensor', 'ips_sensor_status', 'logtraffic',
                   'policyid', 'service', 'srcaddr',
                   'status', 'webfilter_profile', 'webfilter_profile_status']
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


def firewall_interface_policy(data, fos):
    vdom = data['vdom']
    if 'state' in data and data['state']:
        state = data['state']
    elif 'state' in data['firewall_interface_policy'] and data['firewall_interface_policy']['state']:
        state = data['firewall_interface_policy']['state']
    else:
        state = True
    firewall_interface_policy_data = data['firewall_interface_policy']
    filtered_data = underscore_to_hyphen(filter_firewall_interface_policy_data(firewall_interface_policy_data))

    if state == "present":
        return fos.set('firewall',
                       'interface-policy',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('firewall',
                          'interface-policy',
                          mkey=filtered_data['policyid'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_firewall(data, fos):

    if data['firewall_interface_policy']:
        resp = firewall_interface_policy(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('firewall_interface_policy'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = 'policyid'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": False, "type": "str",
                  "choices": ["present", "absent"]},
        "firewall_interface_policy": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "state": {"required": False, "type": "str",
                          "choices": ["present", "absent"]},
                "application_list": {"required": False, "type": "str"},
                "application_list_status": {"required": False, "type": "str",
                                            "choices": ["enable",
                                                        "disable"]},
                "av_profile": {"required": False, "type": "str"},
                "av_profile_status": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable"]},
                "comments": {"required": False, "type": "str"},
                "dlp_sensor": {"required": False, "type": "str"},
                "dlp_sensor_status": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable"]},
                "dsri": {"required": False, "type": "str",
                         "choices": ["enable",
                                     "disable"]},
                "dstaddr": {"required": False, "type": "list",
                            "options": {
                                "name": {"required": True, "type": "str"}
                            }},
                "emailfilter_profile": {"required": False, "type": "str"},
                "emailfilter_profile_status": {"required": False, "type": "str",
                                               "choices": ["enable",
                                                           "disable"]},
                "interface": {"required": False, "type": "str"},
                "ips_sensor": {"required": False, "type": "str"},
                "ips_sensor_status": {"required": False, "type": "str",
                                      "choices": ["enable",
                                                  "disable"]},
                "logtraffic": {"required": False, "type": "str",
                               "choices": ["all",
                                           "utm",
                                           "disable"]},
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
                                       "disable"]},
                "webfilter_profile": {"required": False, "type": "str"},
                "webfilter_profile_status": {"required": False, "type": "str",
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
