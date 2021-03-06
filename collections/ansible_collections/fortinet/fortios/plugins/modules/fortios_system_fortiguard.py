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
module: fortios_system_fortiguard
short_description: Configure FortiGuard services in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify system feature and fortiguard category.
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

    system_fortiguard:
        description:
            - Configure FortiGuard services.
        default: null
        type: dict
        suboptions:
            antispam_cache:
                description:
                    - Enable/disable FortiGuard antispam request caching. Uses a small amount of memory but improves performance.
                type: str
                choices:
                    - enable
                    - disable
            antispam_cache_mpercent:
                description:
                    - Maximum percent of FortiGate memory the antispam cache is allowed to use (1 - 15%).
                type: int
            antispam_cache_ttl:
                description:
                    - Time-to-live for antispam cache entries in seconds (300 - 86400). Lower times reduce the cache size. Higher times may improve
                       performance since the cache will have more entries.
                type: int
            antispam_expiration:
                description:
                    - Expiration date of the FortiGuard antispam contract.
                type: int
            antispam_force_off:
                description:
                    - Enable/disable turning off the FortiGuard antispam service.
                type: str
                choices:
                    - enable
                    - disable
            antispam_license:
                description:
                    - Interval of time between license checks for the FortiGuard antispam contract.
                type: int
            antispam_timeout:
                description:
                    - Antispam query time out (1 - 30 sec).
                type: int
            auto_join_forticloud:
                description:
                    - Automatically connect to and login to FortiCloud.
                type: str
                choices:
                    - enable
                    - disable
            ddns_server_ip:
                description:
                    - IP address of the FortiDDNS server.
                type: str
            ddns_server_port:
                description:
                    - Port used to communicate with FortiDDNS servers.
                type: int
            fortiguard_anycast:
                description:
                    - Enable/disable use of FortiGuard"s anycast network.
                type: str
                choices:
                    - enable
                    - disable
            fortiguard_anycast_source:
                description:
                    - Configure which of Fortinet"s servers to provide FortiGuard services in FortiGuard"s anycast network. Default is Fortinet.
                type: str
                choices:
                    - fortinet
                    - aws
                    - debug
            load_balance_servers:
                description:
                    - Number of servers to alternate between as first FortiGuard option.
                type: int
            outbreak_prevention_cache:
                description:
                    - Enable/disable FortiGuard Virus Outbreak Prevention cache.
                type: str
                choices:
                    - enable
                    - disable
            outbreak_prevention_cache_mpercent:
                description:
                    - Maximum percent of memory FortiGuard Virus Outbreak Prevention cache can use (1 - 15%).
                type: int
            outbreak_prevention_cache_ttl:
                description:
                    - Time-to-live for FortiGuard Virus Outbreak Prevention cache entries (300 - 86400 sec).
                type: int
            outbreak_prevention_expiration:
                description:
                    - Expiration date of FortiGuard Virus Outbreak Prevention contract.
                type: int
            outbreak_prevention_force_off:
                description:
                    - Turn off FortiGuard Virus Outbreak Prevention service.
                type: str
                choices:
                    - enable
                    - disable
            outbreak_prevention_license:
                description:
                    - Interval of time between license checks for FortiGuard Virus Outbreak Prevention contract.
                type: int
            outbreak_prevention_timeout:
                description:
                    - FortiGuard Virus Outbreak Prevention time out (1 - 30 sec).
                type: int
            port:
                description:
                    - Port used to communicate with the FortiGuard servers.
                type: str
                choices:
                    - 8888
                    - 53
                    - 80
                    - 443
            protocol:
                description:
                    - Protocol used to communicate with the FortiGuard servers.
                type: str
                choices:
                    - udp
                    - http
                    - https
            proxy_password:
                description:
                    - Proxy user password.
                type: str
            proxy_server_ip:
                description:
                    - IP address of the proxy server.
                type: str
            proxy_server_port:
                description:
                    - Port used to communicate with the proxy server.
                type: int
            proxy_username:
                description:
                    - Proxy user name.
                type: str
            sandbox_region:
                description:
                    - Cloud sandbox region.
                type: str
            sdns_options:
                description:
                    - Customization options for the FortiGuard DNS service.
                type: str
                choices:
                    - include-question-section
            sdns_server_ip:
                description:
                    - IP address of the FortiDNS server.
                type: str
            sdns_server_port:
                description:
                    - Port used to communicate with FortiDNS servers.
                type: int
            source_ip:
                description:
                    - Source IPv4 address used to communicate with FortiGuard.
                type: str
            source_ip6:
                description:
                    - Source IPv6 address used to communicate with FortiGuard.
                type: str
            update_server_location:
                description:
                    - Signature update server location.
                type: str
                choices:
                    - usa
                    - any
            webfilter_cache:
                description:
                    - Enable/disable FortiGuard web filter caching.
                type: str
                choices:
                    - enable
                    - disable
            webfilter_cache_ttl:
                description:
                    - Time-to-live for web filter cache entries in seconds (300 - 86400).
                type: int
            webfilter_expiration:
                description:
                    - Expiration date of the FortiGuard web filter contract.
                type: int
            webfilter_force_off:
                description:
                    - Enable/disable turning off the FortiGuard web filtering service.
                type: str
                choices:
                    - enable
                    - disable
            webfilter_license:
                description:
                    - Interval of time between license checks for the FortiGuard web filter contract.
                type: int
            webfilter_timeout:
                description:
                    - Web filter query time out (1 - 30 sec).
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
  - name: Configure FortiGuard services.
    fortios_system_fortiguard:
      vdom:  "{{ vdom }}"
      system_fortiguard:
        antispam_cache: "enable"
        antispam_cache_mpercent: "4"
        antispam_cache_ttl: "5"
        antispam_expiration: "6"
        antispam_force_off: "enable"
        antispam_license: "8"
        antispam_timeout: "9"
        auto_join_forticloud: "enable"
        ddns_server_ip: "<your_own_value>"
        ddns_server_port: "12"
        fortiguard_anycast: "enable"
        fortiguard_anycast_source: "fortinet"
        load_balance_servers: "15"
        outbreak_prevention_cache: "enable"
        outbreak_prevention_cache_mpercent: "17"
        outbreak_prevention_cache_ttl: "18"
        outbreak_prevention_expiration: "19"
        outbreak_prevention_force_off: "enable"
        outbreak_prevention_license: "21"
        outbreak_prevention_timeout: "22"
        port: "8888"
        protocol: "udp"
        proxy_password: "<your_own_value>"
        proxy_server_ip: "<your_own_value>"
        proxy_server_port: "27"
        proxy_username: "<your_own_value>"
        sandbox_region: "<your_own_value>"
        sdns_options: "include-question-section"
        sdns_server_ip: "<your_own_value>"
        sdns_server_port: "32"
        source_ip: "84.230.14.43"
        source_ip6: "<your_own_value>"
        update_server_location: "usa"
        webfilter_cache: "enable"
        webfilter_cache_ttl: "37"
        webfilter_expiration: "38"
        webfilter_force_off: "enable"
        webfilter_license: "40"
        webfilter_timeout: "41"

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


def filter_system_fortiguard_data(json):
    option_list = ['antispam_cache', 'antispam_cache_mpercent', 'antispam_cache_ttl',
                   'antispam_expiration', 'antispam_force_off', 'antispam_license',
                   'antispam_timeout', 'auto_join_forticloud', 'ddns_server_ip',
                   'ddns_server_port', 'fortiguard_anycast', 'fortiguard_anycast_source',
                   'load_balance_servers', 'outbreak_prevention_cache', 'outbreak_prevention_cache_mpercent',
                   'outbreak_prevention_cache_ttl', 'outbreak_prevention_expiration', 'outbreak_prevention_force_off',
                   'outbreak_prevention_license', 'outbreak_prevention_timeout', 'port',
                   'protocol', 'proxy_password', 'proxy_server_ip',
                   'proxy_server_port', 'proxy_username', 'sandbox_region',
                   'sdns_options', 'sdns_server_ip', 'sdns_server_port',
                   'source_ip', 'source_ip6', 'update_server_location',
                   'webfilter_cache', 'webfilter_cache_ttl', 'webfilter_expiration',
                   'webfilter_force_off', 'webfilter_license', 'webfilter_timeout']
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


def system_fortiguard(data, fos):
    vdom = data['vdom']
    system_fortiguard_data = data['system_fortiguard']
    filtered_data = underscore_to_hyphen(filter_system_fortiguard_data(system_fortiguard_data))

    return fos.set('system',
                   'fortiguard',
                   data=filtered_data,
                   vdom=vdom)


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_system(data, fos):

    if data['system_fortiguard']:
        resp = system_fortiguard(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('system_fortiguard'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = None
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "system_fortiguard": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "antispam_cache": {"required": False, "type": "str",
                                   "choices": ["enable",
                                               "disable"]},
                "antispam_cache_mpercent": {"required": False, "type": "int"},
                "antispam_cache_ttl": {"required": False, "type": "int"},
                "antispam_expiration": {"required": False, "type": "int"},
                "antispam_force_off": {"required": False, "type": "str",
                                       "choices": ["enable",
                                                   "disable"]},
                "antispam_license": {"required": False, "type": "int"},
                "antispam_timeout": {"required": False, "type": "int"},
                "auto_join_forticloud": {"required": False, "type": "str",
                                         "choices": ["enable",
                                                     "disable"]},
                "ddns_server_ip": {"required": False, "type": "str"},
                "ddns_server_port": {"required": False, "type": "int"},
                "fortiguard_anycast": {"required": False, "type": "str",
                                       "choices": ["enable",
                                                   "disable"]},
                "fortiguard_anycast_source": {"required": False, "type": "str",
                                              "choices": ["fortinet",
                                                          "aws",
                                                          "debug"]},
                "load_balance_servers": {"required": False, "type": "int"},
                "outbreak_prevention_cache": {"required": False, "type": "str",
                                              "choices": ["enable",
                                                          "disable"]},
                "outbreak_prevention_cache_mpercent": {"required": False, "type": "int"},
                "outbreak_prevention_cache_ttl": {"required": False, "type": "int"},
                "outbreak_prevention_expiration": {"required": False, "type": "int"},
                "outbreak_prevention_force_off": {"required": False, "type": "str",
                                                  "choices": ["enable",
                                                              "disable"]},
                "outbreak_prevention_license": {"required": False, "type": "int"},
                "outbreak_prevention_timeout": {"required": False, "type": "int"},
                "port": {"required": False, "type": "str",
                         "choices": ["8888",
                                     "53",
                                     "80",
                                     "443"]},
                "protocol": {"required": False, "type": "str",
                             "choices": ["udp",
                                         "http",
                                         "https"]},
                "proxy_password": {"required": False, "type": "str"},
                "proxy_server_ip": {"required": False, "type": "str"},
                "proxy_server_port": {"required": False, "type": "int"},
                "proxy_username": {"required": False, "type": "str"},
                "sandbox_region": {"required": False, "type": "str"},
                "sdns_options": {"required": False, "type": "str",
                                 "choices": ["include-question-section"]},
                "sdns_server_ip": {"required": False, "type": "str"},
                "sdns_server_port": {"required": False, "type": "int"},
                "source_ip": {"required": False, "type": "str"},
                "source_ip6": {"required": False, "type": "str"},
                "update_server_location": {"required": False, "type": "str",
                                           "choices": ["usa",
                                                       "any"]},
                "webfilter_cache": {"required": False, "type": "str",
                                    "choices": ["enable",
                                                "disable"]},
                "webfilter_cache_ttl": {"required": False, "type": "int"},
                "webfilter_expiration": {"required": False, "type": "int"},
                "webfilter_force_off": {"required": False, "type": "str",
                                        "choices": ["enable",
                                                    "disable"]},
                "webfilter_license": {"required": False, "type": "int"},
                "webfilter_timeout": {"required": False, "type": "int"}

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
