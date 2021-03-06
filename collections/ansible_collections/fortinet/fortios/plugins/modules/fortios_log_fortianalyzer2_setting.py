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
module: fortios_log_fortianalyzer2_setting
short_description: Global FortiAnalyzer settings in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify log_fortianalyzer2 feature and setting category.
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

    log_fortianalyzer2_setting:
        description:
            - Global FortiAnalyzer settings.
        default: null
        type: dict
        suboptions:
            access_config:
                description:
                    - Enable/disable FortiAnalyzer access to configuration and data.
                type: str
                choices:
                    - enable
                    - disable
            certificate:
                description:
                    - Certificate used to communicate with FortiAnalyzer. Source certificate.local.name.
                type: str
            certificate_verification:
                description:
                    - Enable/disable identity verification of FortiAnalyzer by use of certificate.
                type: str
                choices:
                    - enable
                    - disable
            conn_timeout:
                description:
                    - FortiAnalyzer connection time-out in seconds (for status and log buffer).
                type: int
            enc_algorithm:
                description:
                    - Configure the level of SSL protection for secure communication with FortiAnalyzer.
                type: str
                choices:
                    - high-medium
                    - high
                    - low
            hmac_algorithm:
                description:
                    - FortiAnalyzer IPsec tunnel HMAC algorithm.
                type: str
                choices:
                    - sha256
                    - sha1
            ips_archive:
                description:
                    - Enable/disable IPS packet archive logging.
                type: str
                choices:
                    - enable
                    - disable
            max_log_rate:
                description:
                    - FortiAnalyzer maximum log rate in MBps (0 = unlimited).
                type: int
            monitor_failure_retry_period:
                description:
                    - Time between FortiAnalyzer connection retries in seconds (for status and log buffer).
                type: int
            monitor_keepalive_period:
                description:
                    - Time between OFTP keepalives in seconds (for status and log buffer).
                type: int
            priority:
                description:
                    - Set log transmission priority.
                type: str
                choices:
                    - default
                    - low
            reliable:
                description:
                    - Enable/disable reliable logging to FortiAnalyzer.
                type: str
                choices:
                    - enable
                    - disable
            serial:
                description:
                    - Serial numbers of the FortiAnalyzer.
                type: list
                suboptions:
                    name:
                        description:
                            - Serial Number.
                        required: true
                        type: str
            server:
                description:
                    - The remote FortiAnalyzer.
                type: str
            source_ip:
                description:
                    - Source IPv4 or IPv6 address used to communicate with FortiAnalyzer.
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
                    - Enable/disable logging to FortiAnalyzer.
                type: str
                choices:
                    - enable
                    - disable
            upload_day:
                description:
                    - Day of week (month) to upload logs.
                type: str
            upload_interval:
                description:
                    - Frequency to upload log files to FortiAnalyzer.
                type: str
                choices:
                    - daily
                    - weekly
                    - monthly
            upload_option:
                description:
                    - Enable/disable logging to hard disk and then uploading to FortiAnalyzer.
                type: str
                choices:
                    - store-and-upload
                    - realtime
                    - 1-minute
                    - 5-minute
            upload_time:
                description:
                    - 'Time to upload logs (hh:mm).'
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
  - name: Global FortiAnalyzer settings.
    fortios_log_fortianalyzer2_setting:
      vdom:  "{{ vdom }}"
      log_fortianalyzer2_setting:
        access_config: "enable"
        certificate: "<your_own_value> (source certificate.local.name)"
        certificate_verification: "enable"
        conn_timeout: "6"
        enc_algorithm: "high-medium"
        hmac_algorithm: "sha256"
        ips_archive: "enable"
        max_log_rate: "10"
        monitor_failure_retry_period: "11"
        monitor_keepalive_period: "12"
        priority: "default"
        reliable: "enable"
        serial:
         -
            name: "default_name_16"
        server: "192.168.100.40"
        source_ip: "84.230.14.43"
        ssl_min_proto_version: "default"
        status: "enable"
        upload_day: "<your_own_value>"
        upload_interval: "daily"
        upload_option: "store-and-upload"
        upload_time: "<your_own_value>"

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


def filter_log_fortianalyzer2_setting_data(json):
    option_list = ['access_config', 'certificate', 'certificate_verification',
                   'conn_timeout', 'enc_algorithm', 'hmac_algorithm',
                   'ips_archive', 'max_log_rate', 'monitor_failure_retry_period',
                   'monitor_keepalive_period', 'priority', 'reliable',
                   'serial', 'server', 'source_ip',
                   'ssl_min_proto_version', 'status', 'upload_day',
                   'upload_interval', 'upload_option', 'upload_time']
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


def log_fortianalyzer2_setting(data, fos):
    vdom = data['vdom']
    log_fortianalyzer2_setting_data = data['log_fortianalyzer2_setting']
    filtered_data = underscore_to_hyphen(filter_log_fortianalyzer2_setting_data(log_fortianalyzer2_setting_data))

    return fos.set('log.fortianalyzer2',
                   'setting',
                   data=filtered_data,
                   vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_log_fortianalyzer2(data, fos):

    if data['log_fortianalyzer2_setting']:
        resp = log_fortianalyzer2_setting(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('log_fortianalyzer2_setting'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = None
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "log_fortianalyzer2_setting": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "access_config": {"required": False, "type": "str",
                                  "choices": ["enable",
                                              "disable"]},
                "certificate": {"required": False, "type": "str"},
                "certificate_verification": {"required": False, "type": "str",
                                             "choices": ["enable",
                                                         "disable"]},
                "conn_timeout": {"required": False, "type": "int"},
                "enc_algorithm": {"required": False, "type": "str",
                                  "choices": ["high-medium",
                                              "high",
                                              "low"]},
                "hmac_algorithm": {"required": False, "type": "str",
                                   "choices": ["sha256",
                                               "sha1"]},
                "ips_archive": {"required": False, "type": "str",
                                "choices": ["enable",
                                            "disable"]},
                "max_log_rate": {"required": False, "type": "int"},
                "monitor_failure_retry_period": {"required": False, "type": "int"},
                "monitor_keepalive_period": {"required": False, "type": "int"},
                "priority": {"required": False, "type": "str",
                             "choices": ["default",
                                         "low"]},
                "reliable": {"required": False, "type": "str",
                             "choices": ["enable",
                                         "disable"]},
                "serial": {"required": False, "type": "list",
                           "options": {
                               "name": {"required": True, "type": "str"}
                           }},
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
                                       "disable"]},
                "upload_day": {"required": False, "type": "str"},
                "upload_interval": {"required": False, "type": "str",
                                    "choices": ["daily",
                                                "weekly",
                                                "monthly"]},
                "upload_option": {"required": False, "type": "str",
                                  "choices": ["store-and-upload",
                                              "realtime",
                                              "1-minute",
                                              "5-minute"]},
                "upload_time": {"required": False, "type": "str"}

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

        is_error, has_changed, result = fortios_log_fortianalyzer2(module.params, fos)
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
