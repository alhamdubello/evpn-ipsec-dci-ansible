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
module: fortios_cifs_profile
short_description: Configure CIFS profile in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify cifs feature and profile category.
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
    cifs_profile:
        description:
            - Configure CIFS profile.
        default: null
        type: dict
        suboptions:
            domain_controller:
                description:
                    - Domain for which to decrypt CIFS traffic. Source credential-store.domain-controller.server-name.
                type: str
            file_filter:
                description:
                    - File filter.
                type: dict
                suboptions:
                    entries:
                        description:
                            - File filter entries.
                        type: list
                        suboptions:
                            action:
                                description:
                                    - Action taken for matched file.
                                type: str
                                choices:
                                    - log
                                    - block
                            comment:
                                description:
                                    - Comment.
                                type: str
                            direction:
                                description:
                                    - Match files transmitted in the session"s originating or reply direction.
                                type: str
                                choices:
                                    - incoming
                                    - outgoing
                                    - any
                            file_type:
                                description:
                                    - Select file type.
                                type: list
                                suboptions:
                                    name:
                                        description:
                                            - File type name. Source antivirus.filetype.name.
                                        required: true
                                        type: str
                            filter:
                                description:
                                    - Add a file filter.
                                required: true
                                type: str
                    log:
                        description:
                            - Enable/disable file filter logging.
                        type: str
                        choices:
                            - enable
                            - disable
                    status:
                        description:
                            - Enable/disable file filter.
                        type: str
                        choices:
                            - enable
                            - disable
            name:
                description:
                    - Profile name.
                required: true
                type: str
            server_credential_type:
                description:
                    - CIFS server credential type.
                type: str
                choices:
                    - none
                    - credential-replication
                    - credential-keytab
            server_keytab:
                description:
                    - Server keytab.
                type: str
                suboptions:
                    keytab:
                        description:
                            - Base64 encoded keytab file containing credential of the server.
                        type: str
                    principal:
                        description:
                            - Service principal.  For example, "host/cifsserver.example.com@example.com".
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
  - name: Configure CIFS profile.
    fortios_cifs_profile:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      cifs_profile:
        domain_controller: "<your_own_value> (source credential-store.domain-controller.server-name)"
        file_filter:
            entries:
             -
                action: "log"
                comment: "Comment."
                direction: "incoming"
                file_type:
                 -
                    name: "default_name_10 (source antivirus.filetype.name)"
                filter: "<your_own_value>"
            log: "enable"
            status: "enable"
        name: "default_name_14"
        server_credential_type: "none"
        server_keytab:
         -
            keytab: "<your_own_value>"
            principal: "<your_own_value>"

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


def filter_cifs_profile_data(json):
    option_list = ['domain_controller', 'file_filter', 'name',
                   'server_credential_type', 'server_keytab']
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


def cifs_profile(data, fos):
    vdom = data['vdom']
    state = data['state']
    cifs_profile_data = data['cifs_profile']
    filtered_data = underscore_to_hyphen(filter_cifs_profile_data(cifs_profile_data))

    if state == "present":
        return fos.set('cifs',
                       'profile',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('cifs',
                          'profile',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_cifs(data, fos):

    if data['cifs_profile']:
        resp = cifs_profile(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('cifs_profile'))

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
        "cifs_profile": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "domain_controller": {"required": False, "type": "str"},
                "file_filter": {"required": False, "type": "dict",
                                "options": {
                                    "entries": {"required": False, "type": "list",
                                                "options": {
                                                    "action": {"required": False, "type": "str",
                                                               "choices": ["log",
                                                                           "block"]},
                                                    "comment": {"required": False, "type": "str"},
                                                    "direction": {"required": False, "type": "str",
                                                                  "choices": ["incoming",
                                                                              "outgoing",
                                                                              "any"]},
                                                    "file_type": {"required": False, "type": "list",
                                                                  "options": {
                                                                      "name": {"required": True, "type": "str"}
                                                                  }},
                                                    "filter": {"required": True, "type": "str"}
                                                }},
                                    "log": {"required": False, "type": "str",
                                            "choices": ["enable",
                                                        "disable"]},
                                    "status": {"required": False, "type": "str",
                                               "choices": ["enable",
                                                           "disable"]}
                                }},
                "name": {"required": True, "type": "str"},
                "server_credential_type": {"required": False, "type": "str",
                                           "choices": ["none",
                                                       "credential-replication",
                                                       "credential-keytab"]},
                "server_keytab": {"required": False, "type": "str",
                                  "options": {
                                      "keytab": {"required": False, "type": "str"},
                                      "principal": {"required": True, "type": "str"}
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

        is_error, has_changed, result = fortios_cifs(module.params, fos)
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
