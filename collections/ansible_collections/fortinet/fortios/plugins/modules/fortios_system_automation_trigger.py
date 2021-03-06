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
module: fortios_system_automation_trigger
short_description: Trigger for automation stitches in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify system feature and automation_trigger category.
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
    system_automation_trigger:
        description:
            - Trigger for automation stitches.
        default: null
        type: dict
        suboptions:
            event_type:
                description:
                    - Event type.
                type: str
                choices:
                    - ioc
                    - event-log
                    - reboot
                    - low-memory
                    - high-cpu
                    - license-near-expiry
                    - ha-failover
                    - config-change
                    - security-rating-summary
                    - virus-ips-db-updated
                    - faz-event
                    - incoming-webhook
            faz_event_name:
                description:
                    - FortiAnalyzer event handler name.
                type: str
            faz_event_severity:
                description:
                    - FortiAnalyzer event severity.
                type: str
            faz_event_tags:
                description:
                    - FortiAnalyzer event tags.
                type: str
            fields:
                description:
                    - Customized trigger field settings.
                type: list
                suboptions:
                    id:
                        description:
                            - Entry ID.
                        required: true
                        type: int
                    name:
                        description:
                            - Name.
                        type: str
                    value:
                        description:
                            - Value.
                        type: str
            ioc_level:
                description:
                    - IOC threat level.
                type: str
                choices:
                    - medium
                    - high
            license_type:
                description:
                    - License type.
                type: str
                choices:
                    - forticare-support
                    - fortiguard-webfilter
                    - fortiguard-antispam
                    - fortiguard-antivirus
                    - fortiguard-ips
                    - fortiguard-management
                    - forticloud
                    - any
            logid:
                description:
                    - Log ID to trigger event.
                type: int
            name:
                description:
                    - Name.
                required: true
                type: str
            report_type:
                description:
                    - Security Rating report.
                type: str
                choices:
                    - PostureReport
                    - CoverageReport
                    - OptimizationReport
            trigger_day:
                description:
                    - Day within a month to trigger.
                type: int
            trigger_frequency:
                description:
                    - Scheduled trigger frequency .
                type: str
                choices:
                    - hourly
                    - daily
                    - weekly
                    - monthly
            trigger_hour:
                description:
                    - Hour of the day on which to trigger (0 - 23).
                type: int
            trigger_minute:
                description:
                    - Minute of the hour on which to trigger (0 - 59).
                type: int
            trigger_type:
                description:
                    - Trigger type.
                type: str
                choices:
                    - event-based
                    - scheduled
            trigger_weekday:
                description:
                    - Day of week for trigger.
                type: str
                choices:
                    - sunday
                    - monday
                    - tuesday
                    - wednesday
                    - thursday
                    - friday
                    - saturday
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
  - name: Trigger for automation stitches.
    fortios_system_automation_trigger:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_automation_trigger:
        event_type: "ioc"
        faz_event_name: "<your_own_value>"
        faz_event_severity: "<your_own_value>"
        faz_event_tags: "<your_own_value>"
        fields:
         -
            id:  "8"
            name: "default_name_9"
            value: "<your_own_value>"
        ioc_level: "medium"
        license_type: "forticare-support"
        logid: "13"
        name: "default_name_14"
        report_type: "PostureReport"
        trigger_day: "16"
        trigger_frequency: "hourly"
        trigger_hour: "18"
        trigger_minute: "19"
        trigger_type: "event-based"
        trigger_weekday: "sunday"

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


def filter_system_automation_trigger_data(json):
    option_list = ['event_type', 'faz_event_name', 'faz_event_severity',
                   'faz_event_tags', 'fields', 'ioc_level',
                   'license_type', 'logid', 'name',
                   'report_type', 'trigger_day', 'trigger_frequency',
                   'trigger_hour', 'trigger_minute', 'trigger_type',
                   'trigger_weekday']
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


def system_automation_trigger(data, fos):
    vdom = data['vdom']
    state = data['state']
    system_automation_trigger_data = data['system_automation_trigger']
    filtered_data = underscore_to_hyphen(filter_system_automation_trigger_data(system_automation_trigger_data))

    if state == "present":
        return fos.set('system',
                       'automation-trigger',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('system',
                          'automation-trigger',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_system(data, fos):

    if data['system_automation_trigger']:
        resp = system_automation_trigger(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('system_automation_trigger'))

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
        "system_automation_trigger": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "event_type": {"required": False, "type": "str",
                               "choices": ["ioc",
                                           "event-log",
                                           "reboot",
                                           "low-memory",
                                           "high-cpu",
                                           "license-near-expiry",
                                           "ha-failover",
                                           "config-change",
                                           "security-rating-summary",
                                           "virus-ips-db-updated",
                                           "faz-event",
                                           "incoming-webhook"]},
                "faz_event_name": {"required": False, "type": "str"},
                "faz_event_severity": {"required": False, "type": "str"},
                "faz_event_tags": {"required": False, "type": "str"},
                "fields": {"required": False, "type": "list",
                           "options": {
                               "id": {"required": True, "type": "int"},
                               "name": {"required": False, "type": "str"},
                               "value": {"required": False, "type": "str"}
                           }},
                "ioc_level": {"required": False, "type": "str",
                              "choices": ["medium",
                                          "high"]},
                "license_type": {"required": False, "type": "str",
                                 "choices": ["forticare-support",
                                             "fortiguard-webfilter",
                                             "fortiguard-antispam",
                                             "fortiguard-antivirus",
                                             "fortiguard-ips",
                                             "fortiguard-management",
                                             "forticloud",
                                             "any"]},
                "logid": {"required": False, "type": "int"},
                "name": {"required": True, "type": "str"},
                "report_type": {"required": False, "type": "str",
                                "choices": ["PostureReport",
                                            "CoverageReport",
                                            "OptimizationReport"]},
                "trigger_day": {"required": False, "type": "int"},
                "trigger_frequency": {"required": False, "type": "str",
                                      "choices": ["hourly",
                                                  "daily",
                                                  "weekly",
                                                  "monthly"]},
                "trigger_hour": {"required": False, "type": "int"},
                "trigger_minute": {"required": False, "type": "int"},
                "trigger_type": {"required": False, "type": "str",
                                 "choices": ["event-based",
                                             "scheduled"]},
                "trigger_weekday": {"required": False, "type": "str",
                                    "choices": ["sunday",
                                                "monday",
                                                "tuesday",
                                                "wednesday",
                                                "thursday",
                                                "friday",
                                                "saturday"]}

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

        is_error, has_changed, result = fortios_system(module.params, fos)
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
