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
module: fortios_log_syslogd_setting
short_description: Global settings for remote syslog server in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify log_syslogd feature and setting category.
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

    log_syslogd_setting:
        description:
            - Global settings for remote syslog server.
        default: null
        type: dict
        suboptions:
            certificate:
                description:
                    - Certificate used to communicate with Syslog server. Source certificate.local.name.
                type: str
            custom_field_name:
                description:
                    - Custom field name for CEF format logging.
                type: list
                suboptions:
                    custom:
                        description:
                            - Field custom name.
                        type: str
                    id:
                        description:
                            - Entry ID.
                        required: true
                        type: int
                    name:
                        description:
                            - Field name.
                        type: str
            enc_algorithm:
                description:
                    - Enable/disable reliable syslogging with TLS encryption.
                type: str
                choices:
                    - high-medium
                    - high
                    - low
                    - disable
            facility:
                description:
                    - Remote syslog facility.
                type: str
                choices:
                    - kernel
                    - user
                    - mail
                    - daemon
                    - auth
                    - syslog
                    - lpr
                    - news
                    - uucp
                    - cron
                    - authpriv
                    - ftp
                    - ntp
                    - audit
                    - alert
                    - clock
                    - local0
                    - local1
                    - local2
                    - local3
                    - local4
                    - local5
                    - local6
                    - local7
            format:
                description:
                    - Log format.
                type: str
                choices:
                    - default
                    - csv
                    - cef
            max_log_rate:
                description:
                    - Syslog maximum log rate in MBps (0 = unlimited).
                type: int
            mode:
                description:
                    - Remote syslog logging over UDP/Reliable TCP.
                type: str
                choices:
                    - udp
                    - legacy-reliable
                    - reliable
            port:
                description:
                    - Server listen port.
                type: int
            priority:
                description:
                    - Set log transmission priority.
                type: str
                choices:
                    - default
                    - low
            server:
                description:
                    - Address of remote syslog server.
                type: str
            source_ip:
                description:
                    - Source IP address of syslog.
                type: str
            ssl_min_proto_version:
                description:
                    - Minimum supported protocol version for SSL/TLS connections .
                type: str
                choices:
                    - default
                    - SSLv3
                    - TLSv1
                    - TLSv1-1
                    - TLSv1-2
            status:
                description:
                    - Enable/disable remote syslog logging.
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
  - name: Global settings for remote syslog server.
    fortios_log_syslogd_setting:
      vdom:  "{{ vdom }}"
      log_syslogd_setting:
        certificate: "<your_own_value> (source certificate.local.name)"
        custom_field_name:
         -
            custom: "<your_own_value>"
            id:  "6"
            name: "default_name_7"
        enc_algorithm: "high-medium"
        facility: "kernel"
        format: "default"
        max_log_rate: "11"
        mode: "udp"
        port: "13"
        priority: "default"
        server: "192.168.100.40"
        source_ip: "84.230.14.43"
        ssl_min_proto_version: "default"
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


def filter_log_syslogd_setting_data(json):
    option_list = ['certificate', 'custom_field_name', 'enc_algorithm',
                   'facility', 'format', 'max_log_rate',
                   'mode', 'port', 'priority',
                   'server', 'source_ip', 'ssl_min_proto_version',
                   'status']
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


def log_syslogd_setting(data, fos):
    vdom = data['vdom']
    log_syslogd_setting_data = data['log_syslogd_setting']
    filtered_data = underscore_to_hyphen(filter_log_syslogd_setting_data(log_syslogd_setting_data))

    return fos.set('log.syslogd',
                   'setting',
                   data=filtered_data,
                   vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_log_syslogd(data, fos):

    if data['log_syslogd_setting']:
        resp = log_syslogd_setting(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('log_syslogd_setting'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = None
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "log_syslogd_setting": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "certificate": {"required": False, "type": "str"},
                "custom_field_name": {"required": False, "type": "list",
                                      "options": {
                                          "custom": {"required": False, "type": "str"},
                                          "id": {"required": True, "type": "int"},
                                          "name": {"required": False, "type": "str"}
                                      }},
                "enc_algorithm": {"required": False, "type": "str",
                                  "choices": ["high-medium",
                                              "high",
                                              "low",
                                              "disable"]},
                "facility": {"required": False, "type": "str",
                             "choices": ["kernel",
                                         "user",
                                         "mail",
                                         "daemon",
                                         "auth",
                                         "syslog",
                                         "lpr",
                                         "news",
                                         "uucp",
                                         "cron",
                                         "authpriv",
                                         "ftp",
                                         "ntp",
                                         "audit",
                                         "alert",
                                         "clock",
                                         "local0",
                                         "local1",
                                         "local2",
                                         "local3",
                                         "local4",
                                         "local5",
                                         "local6",
                                         "local7"]},
                "format": {"required": False, "type": "str",
                           "choices": ["default",
                                       "csv",
                                       "cef"]},
                "max_log_rate": {"required": False, "type": "int"},
                "mode": {"required": False, "type": "str",
                         "choices": ["udp",
                                     "legacy-reliable",
                                     "reliable"]},
                "port": {"required": False, "type": "int"},
                "priority": {"required": False, "type": "str",
                             "choices": ["default",
                                         "low"]},
                "server": {"required": False, "type": "str"},
                "source_ip": {"required": False, "type": "str"},
                "ssl_min_proto_version": {"required": False, "type": "str",
                                          "choices": ["default",
                                                      "SSLv3",
                                                      "TLSv1",
                                                      "TLSv1-1",
                                                      "TLSv1-2"]},
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

        is_error, has_changed, result = fortios_log_syslogd(module.params, fos)
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
