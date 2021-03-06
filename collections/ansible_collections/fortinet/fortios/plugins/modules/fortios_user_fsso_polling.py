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
module: fortios_user_fsso_polling
short_description: Configure FSSO active directory servers for polling mode in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify user feature and fsso_polling category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.4.0
version_added: "2.9"
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
    user_fsso_polling:
        description:
            - Configure FSSO active directory servers for polling mode.
        default: null
        type: dict
        suboptions:
            adgrp:
                description:
                    - LDAP Group Info.
                type: list
                suboptions:
                    name:
                        description:
                            - Name.
                        required: true
                        type: str
            default_domain:
                description:
                    - Default domain managed by this Active Directory server.
                type: str
            id:
                description:
                    - Active Directory server ID.
                required: true
                type: int
            ldap_server:
                description:
                    - LDAP server name used in LDAP connection strings. Source user.ldap.name.
                type: str
            logon_history:
                description:
                    - Number of hours of logon history to keep, 0 means keep all history.
                type: int
            password:
                description:
                    - Password required to log into this Active Directory server
                type: str
            polling_frequency:
                description:
                    - Polling frequency (every 1 to 30 seconds).
                type: int
            port:
                description:
                    - Port to communicate with this Active Directory server.
                type: int
            server:
                description:
                    - Host name or IP address of the Active Directory server.
                type: str
            smb_ntlmv1_auth:
                description:
                    - Enable/disable support of NTLMv1 for Samba authentication.
                type: str
                choices:
                    - enable
                    - disable
            smbv1:
                description:
                    - Enable/disable support of SMBv1 for Samba.
                type: str
                choices:
                    - enable
                    - disable
            status:
                description:
                    - Enable/disable polling for the status of this Active Directory server.
                type: str
                choices:
                    - enable
                    - disable
            user:
                description:
                    - User name required to log into this Active Directory server.
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
  - name: Configure FSSO active directory servers for polling mode.
    fortios_user_fsso_polling:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      user_fsso_polling:
        adgrp:
         -
            name: "default_name_4"
        default_domain: "<your_own_value>"
        id:  "6"
        ldap_server: "<your_own_value> (source user.ldap.name)"
        logon_history: "8"
        password: "<your_own_value>"
        polling_frequency: "10"
        port: "11"
        server: "192.168.100.40"
        smb_ntlmv1_auth: "enable"
        smbv1: "enable"
        status: "enable"
        user: "<your_own_value>"

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


def filter_user_fsso_polling_data(json):
    option_list = ['adgrp', 'default_domain', 'id',
                   'ldap_server', 'logon_history', 'password',
                   'polling_frequency', 'port', 'server',
                   'smb_ntlmv1_auth', 'smbv1', 'status',
                   'user']
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


def user_fsso_polling(data, fos):
    vdom = data['vdom']
    state = data['state']
    user_fsso_polling_data = data['user_fsso_polling']
    filtered_data = underscore_to_hyphen(filter_user_fsso_polling_data(user_fsso_polling_data))

    if state == "present":
        return fos.set('user',
                       'fsso-polling',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('user',
                          'fsso-polling',
                          mkey=filtered_data['id'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_user(data, fos):

    if data['user_fsso_polling']:
        resp = user_fsso_polling(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('user_fsso_polling'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = 'id'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": True, "type": "str",
                  "choices": ["present", "absent"]},
        "user_fsso_polling": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "adgrp": {"required": False, "type": "list",
                          "options": {
                              "name": {"required": True, "type": "str"}
                          }},
                "default_domain": {"required": False, "type": "str"},
                "id": {"required": True, "type": "int"},
                "ldap_server": {"required": False, "type": "str"},
                "logon_history": {"required": False, "type": "int"},
                "password": {"required": False, "type": "str"},
                "polling_frequency": {"required": False, "type": "int"},
                "port": {"required": False, "type": "int"},
                "server": {"required": False, "type": "str"},
                "smb_ntlmv1_auth": {"required": False, "type": "str",
                                    "choices": ["enable",
                                                "disable"]},
                "smbv1": {"required": False, "type": "str",
                          "choices": ["enable",
                                      "disable"]},
                "status": {"required": False, "type": "str",
                           "choices": ["enable",
                                       "disable"]},
                "user": {"required": False, "type": "str"}

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

        is_error, has_changed, result = fortios_user(module.params, fos)
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
