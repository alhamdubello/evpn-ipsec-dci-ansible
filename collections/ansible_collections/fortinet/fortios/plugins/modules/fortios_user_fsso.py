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
module: fortios_user_fsso
short_description: Configure Fortinet Single Sign On (FSSO) agents in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify user feature and fsso category.
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
    user_fsso:
        description:
            - Configure Fortinet Single Sign On (FSSO) agents.
        default: null
        type: dict
        suboptions:
            group_poll_interval:
                description:
                    - Interval in minutes within to fetch groups from FSSO server, or unset to disable.
                type: int
            ldap_poll:
                description:
                    - Enable/disable automatic fetching of groups from LDAP server.
                type: str
                choices:
                    - enable
                    - disable
            ldap_poll_filter:
                description:
                    - Filter used to fetch groups.
                type: str
            ldap_poll_interval:
                description:
                    - Interval in minutes within to fetch groups from LDAP server.
                type: int
            ldap_server:
                description:
                    - LDAP server to get group information. Source user.ldap.name.
                type: str
            name:
                description:
                    - Name.
                required: true
                type: str
            password:
                description:
                    - Password of the first FSSO collector agent.
                type: str
            password2:
                description:
                    - Password of the second FSSO collector agent.
                type: str
            password3:
                description:
                    - Password of the third FSSO collector agent.
                type: str
            password4:
                description:
                    - Password of the fourth FSSO collector agent.
                type: str
            password5:
                description:
                    - Password of the fifth FSSO collector agent.
                type: str
            port:
                description:
                    - Port of the first FSSO collector agent.
                type: int
            port2:
                description:
                    - Port of the second FSSO collector agent.
                type: int
            port3:
                description:
                    - Port of the third FSSO collector agent.
                type: int
            port4:
                description:
                    - Port of the fourth FSSO collector agent.
                type: int
            port5:
                description:
                    - Port of the fifth FSSO collector agent.
                type: int
            server:
                description:
                    - Domain name or IP address of the first FSSO collector agent.
                type: str
            server2:
                description:
                    - Domain name or IP address of the second FSSO collector agent.
                type: str
            server3:
                description:
                    - Domain name or IP address of the third FSSO collector agent.
                type: str
            server4:
                description:
                    - Domain name or IP address of the fourth FSSO collector agent.
                type: str
            server5:
                description:
                    - Domain name or IP address of the fifth FSSO collector agent.
                type: str
            source_ip:
                description:
                    - Source IP for communications to FSSO agent.
                type: str
            source_ip6:
                description:
                    - IPv6 source for communications to FSSO agent.
                type: str
            ssl:
                description:
                    - Enable/disable use of SSL.
                type: str
                choices:
                    - enable
                    - disable
            ssl_trusted_cert:
                description:
                    - Trusted server certificate or CA certificate. Source vpn.certificate.remote.name vpn.certificate.ca.name.
                type: str
            type:
                description:
                    - Server type.
                type: str
                choices:
                    - default
                    - fortinac
            user_info_server:
                description:
                    - LDAP server to get user information. Source user.ldap.name.
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
  - name: Configure Fortinet Single Sign On (FSSO) agents.
    fortios_user_fsso:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      user_fsso:
        group_poll_interval: "3"
        ldap_poll: "enable"
        ldap_poll_filter: "<your_own_value>"
        ldap_poll_interval: "6"
        ldap_server: "<your_own_value> (source user.ldap.name)"
        name: "default_name_8"
        password: "<your_own_value>"
        password2: "<your_own_value>"
        password3: "<your_own_value>"
        password4: "<your_own_value>"
        password5: "<your_own_value>"
        port: "14"
        port2: "15"
        port3: "16"
        port4: "17"
        port5: "18"
        server: "192.168.100.40"
        server2: "<your_own_value>"
        server3: "<your_own_value>"
        server4: "<your_own_value>"
        server5: "<your_own_value>"
        source_ip: "84.230.14.43"
        source_ip6: "<your_own_value>"
        ssl: "enable"
        ssl_trusted_cert: "<your_own_value> (source vpn.certificate.remote.name vpn.certificate.ca.name)"
        type: "default"
        user_info_server: "<your_own_value> (source user.ldap.name)"

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


def filter_user_fsso_data(json):
    option_list = ['group_poll_interval', 'ldap_poll', 'ldap_poll_filter',
                   'ldap_poll_interval', 'ldap_server', 'name',
                   'password', 'password2', 'password3',
                   'password4', 'password5', 'port',
                   'port2', 'port3', 'port4',
                   'port5', 'server', 'server2',
                   'server3', 'server4', 'server5',
                   'source_ip', 'source_ip6', 'ssl',
                   'ssl_trusted_cert', 'type', 'user_info_server']
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


def user_fsso(data, fos):
    vdom = data['vdom']
    state = data['state']
    user_fsso_data = data['user_fsso']
    filtered_data = underscore_to_hyphen(filter_user_fsso_data(user_fsso_data))

    if state == "present":
        return fos.set('user',
                       'fsso',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('user',
                          'fsso',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_user(data, fos):

    if data['user_fsso']:
        resp = user_fsso(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('user_fsso'))

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
        "user_fsso": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "group_poll_interval": {"required": False, "type": "int"},
                "ldap_poll": {"required": False, "type": "str",
                              "choices": ["enable",
                                          "disable"]},
                "ldap_poll_filter": {"required": False, "type": "str"},
                "ldap_poll_interval": {"required": False, "type": "int"},
                "ldap_server": {"required": False, "type": "str"},
                "name": {"required": True, "type": "str"},
                "password": {"required": False, "type": "str"},
                "password2": {"required": False, "type": "str"},
                "password3": {"required": False, "type": "str"},
                "password4": {"required": False, "type": "str"},
                "password5": {"required": False, "type": "str"},
                "port": {"required": False, "type": "int"},
                "port2": {"required": False, "type": "int"},
                "port3": {"required": False, "type": "int"},
                "port4": {"required": False, "type": "int"},
                "port5": {"required": False, "type": "int"},
                "server": {"required": False, "type": "str"},
                "server2": {"required": False, "type": "str"},
                "server3": {"required": False, "type": "str"},
                "server4": {"required": False, "type": "str"},
                "server5": {"required": False, "type": "str"},
                "source_ip": {"required": False, "type": "str"},
                "source_ip6": {"required": False, "type": "str"},
                "ssl": {"required": False, "type": "str",
                        "choices": ["enable",
                                    "disable"]},
                "ssl_trusted_cert": {"required": False, "type": "str"},
                "type": {"required": False, "type": "str",
                         "choices": ["default",
                                     "fortinac"]},
                "user_info_server": {"required": False, "type": "str"}

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
