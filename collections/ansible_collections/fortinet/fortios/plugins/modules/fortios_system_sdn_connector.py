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
module: fortios_system_sdn_connector
short_description: Configure connection to SDN Connector in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify system feature and sdn_connector category.
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
    system_sdn_connector:
        description:
            - Configure connection to SDN Connector.
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
            access_key:
                description:
                    - AWS / ACS access key ID.
                type: str
            azure_region:
                description:
                    - Azure server region.
                type: str
                choices:
                    - global
                    - china
                    - germany
                    - usgov
                    - local
            client_id:
                description:
                    - Azure client ID (application ID).
                type: str
            client_secret:
                description:
                    - Azure client secret (application key).
                type: str
            compartment_id:
                description:
                    - Compartment ID.
                type: str
            domain:
                description:
                    - Domain name.
                type: str
            external_ip:
                description:
                    - Configure GCP external IP.
                type: list
                suboptions:
                    name:
                        description:
                            - External IP name.
                        required: true
                        type: str
            gcp_project:
                description:
                    - GCP project name.
                type: str
            group_name:
                description:
                    - Group name of computers.
                type: str
            ha_status:
                description:
                    - Enable/disable use for FortiGate HA service.
                type: str
                choices:
                    - disable
                    - enable
            login_endpoint:
                description:
                    - Azure Stack login endpoint.
                type: str
            name:
                description:
                    - SDN connector name.
                required: true
                type: str
            nic:
                description:
                    - Configure Azure network interface.
                type: list
                suboptions:
                    ip:
                        description:
                            - Configure IP configuration.
                        type: list
                        suboptions:
                            name:
                                description:
                                    - IP configuration name.
                                required: true
                                type: str
                            public_ip:
                                description:
                                    - Public IP name.
                                type: str
                            resource_group:
                                description:
                                    - Resource group of Azure public IP.
                                type: str
                    name:
                        description:
                            - Network interface name.
                        required: true
                        type: str
            oci_cert:
                description:
                    - OCI certificate. Source certificate.local.name.
                type: str
            oci_fingerprint:
                description:
                    - OCI pubkey fingerprint.
                type: str
            oci_region:
                description:
                    - OCI server region.
                type: str
            oci_region_type:
                description:
                    - OCI region type.
                type: str
                choices:
                    - commercial
                    - government
            password:
                description:
                    - Password of the remote SDN connector as login credentials.
                type: password_aes256
            private_key:
                description:
                    - Private key of GCP service account.
                type: str
            region:
                description:
                    - AWS / ACS region name.
                type: str
            resource_group:
                description:
                    - Azure resource group.
                type: str
            resource_url:
                description:
                    - Azure Stack resource URL.
                type: str
            route:
                description:
                    - Configure GCP route.
                type: list
                suboptions:
                    name:
                        description:
                            - Route name.
                        required: true
                        type: str
            route_table:
                description:
                    - Configure Azure route table.
                type: list
                suboptions:
                    name:
                        description:
                            - Route table name.
                        required: true
                        type: str
                    resource_group:
                        description:
                            - Resource group of Azure route table.
                        type: str
                    route:
                        description:
                            - Configure Azure route.
                        type: list
                        suboptions:
                            name:
                                description:
                                    - Route name.
                                required: true
                                type: str
                            next_hop:
                                description:
                                    - Next hop address.
                                type: str
            secret_key:
                description:
                    - AWS / ACS secret access key.
                type: str
            secret_token:
                description:
                    - Secret token of Kubernetes service account.
                type: str
            server:
                description:
                    - Server address of the remote SDN connector.
                type: str
            server_port:
                description:
                    - Port number of the remote SDN connector.
                type: int
            service_account:
                description:
                    - GCP service account email.
                type: str
            status:
                description:
                    - Enable/disable connection to the remote SDN connector.
                type: str
                choices:
                    - disable
                    - enable
            subscription_id:
                description:
                    - Azure subscription ID.
                type: str
            tenant_id:
                description:
                    - Tenant ID (directory ID).
                type: str
            type:
                description:
                    - Type of SDN connector.
                type: str
                choices:
                    - aci
                    - alicloud
                    - aws
                    - azure
                    - gcp
                    - nsx
                    - nuage
                    - oci
                    - openstack
                    - kubernetes
                    - vmware
                    - sepm
                    - aci-direct
            update_interval:
                description:
                    - Dynamic object update interval (30 - 3600 sec).
                type: int
            use_metadata_iam:
                description:
                    - Enable/disable use of IAM role from metadata to call API.
                type: str
                choices:
                    - disable
                    - enable
            user_id:
                description:
                    - User ID.
                type: str
            username:
                description:
                    - Username of the remote SDN connector as login credentials.
                type: str
            vpc_id:
                description:
                    - AWS VPC ID.
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
  - name: Configure connection to SDN Connector.
    fortios_system_sdn_connector:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      system_sdn_connector:
        access_key: "<your_own_value>"
        azure_region: "global"
        client_id: "<your_own_value>"
        client_secret: "<your_own_value>"
        compartment_id: "<your_own_value>"
        domain: "<your_own_value>"
        external_ip:
         -
            name: "default_name_10"
        gcp_project: "<your_own_value>"
        group_name: "<your_own_value>"
        ha_status: "disable"
        login_endpoint: "<your_own_value>"
        name: "default_name_15"
        nic:
         -
            ip:
             -
                name: "default_name_18"
                public_ip: "<your_own_value>"
                resource_group: "<your_own_value>"
            name: "default_name_21"
        oci_cert: "<your_own_value> (source certificate.local.name)"
        oci_fingerprint: "<your_own_value>"
        oci_region: "<your_own_value>"
        oci_region_type: "commercial"
        password: "<your_own_value>"
        private_key: "<your_own_value>"
        region: "<your_own_value>"
        resource_group: "<your_own_value>"
        resource_url: "<your_own_value>"
        route:
         -
            name: "default_name_32"
        route_table:
         -
            name: "default_name_34"
            resource_group: "<your_own_value>"
            route:
             -
                name: "default_name_37"
                next_hop: "<your_own_value>"
        secret_key: "<your_own_value>"
        secret_token: "<your_own_value>"
        server: "192.168.100.40"
        server_port: "42"
        service_account: "<your_own_value>"
        status: "disable"
        subscription_id: "<your_own_value>"
        tenant_id: "<your_own_value>"
        type: "aci"
        update_interval: "48"
        use_metadata_iam: "disable"
        user_id: "<your_own_value>"
        username: "<your_own_value>"
        vpc_id: "<your_own_value>"

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


def filter_system_sdn_connector_data(json):
    option_list = ['access_key', 'azure_region', 'client_id',
                   'client_secret', 'compartment_id', 'domain',
                   'external_ip', 'gcp_project', 'group_name',
                   'ha_status', 'login_endpoint', 'name',
                   'nic', 'oci_cert', 'oci_fingerprint',
                   'oci_region', 'oci_region_type', 'password',
                   'private_key', 'region', 'resource_group',
                   'resource_url', 'route', 'route_table',
                   'secret_key', 'secret_token', 'server',
                   'server_port', 'service_account', 'status',
                   'subscription_id', 'tenant_id', 'type',
                   'update_interval', 'use_metadata_iam', 'user_id',
                   'username', 'vpc_id']
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


def system_sdn_connector(data, fos):
    vdom = data['vdom']
    if 'state' in data and data['state']:
        state = data['state']
    elif 'state' in data['system_sdn_connector'] and data['system_sdn_connector']['state']:
        state = data['system_sdn_connector']['state']
    else:
        state = True
    system_sdn_connector_data = data['system_sdn_connector']
    filtered_data = underscore_to_hyphen(filter_system_sdn_connector_data(system_sdn_connector_data))

    if state == "present":
        return fos.set('system',
                       'sdn-connector',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('system',
                          'sdn-connector',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_system(data, fos):

    if data['system_sdn_connector']:
        resp = system_sdn_connector(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('system_sdn_connector'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = 'name'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": False, "type": "str",
                  "choices": ["present", "absent"]},
        "system_sdn_connector": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "state": {"required": False, "type": "str",
                          "choices": ["present", "absent"]},
                "access_key": {"required": False, "type": "str"},
                "azure_region": {"required": False, "type": "str",
                                 "choices": ["global",
                                             "china",
                                             "germany",
                                             "usgov",
                                             "local"]},
                "client_id": {"required": False, "type": "str"},
                "client_secret": {"required": False, "type": "str"},
                "compartment_id": {"required": False, "type": "str"},
                "domain": {"required": False, "type": "str"},
                "external_ip": {"required": False, "type": "list",
                                "options": {
                                    "name": {"required": True, "type": "str"}
                                }},
                "gcp_project": {"required": False, "type": "str"},
                "group_name": {"required": False, "type": "str"},
                "ha_status": {"required": False, "type": "str",
                              "choices": ["disable",
                                          "enable"]},
                "login_endpoint": {"required": False, "type": "str"},
                "name": {"required": True, "type": "str"},
                "nic": {"required": False, "type": "list",
                        "options": {
                            "ip": {"required": False, "type": "list",
                                   "options": {
                                       "name": {"required": True, "type": "str"},
                                       "public_ip": {"required": False, "type": "str"},
                                       "resource_group": {"required": False, "type": "str"}
                                   }},
                            "name": {"required": True, "type": "str"}
                        }},
                "oci_cert": {"required": False, "type": "str"},
                "oci_fingerprint": {"required": False, "type": "str"},
                "oci_region": {"required": False, "type": "str"},
                "oci_region_type": {"required": False, "type": "str",
                                    "choices": ["commercial",
                                                "government"]},
                "password": {"required": False, "type": "password_aes256"},
                "private_key": {"required": False, "type": "str"},
                "region": {"required": False, "type": "str"},
                "resource_group": {"required": False, "type": "str"},
                "resource_url": {"required": False, "type": "str"},
                "route": {"required": False, "type": "list",
                          "options": {
                              "name": {"required": True, "type": "str"}
                          }},
                "route_table": {"required": False, "type": "list",
                                "options": {
                                    "name": {"required": True, "type": "str"},
                                    "resource_group": {"required": False, "type": "str"},
                                    "route": {"required": False, "type": "list",
                                              "options": {
                                                  "name": {"required": True, "type": "str"},
                                                  "next_hop": {"required": False, "type": "str"}
                                              }}
                                }},
                "secret_key": {"required": False, "type": "str"},
                "secret_token": {"required": False, "type": "str"},
                "server": {"required": False, "type": "str"},
                "server_port": {"required": False, "type": "int"},
                "service_account": {"required": False, "type": "str"},
                "status": {"required": False, "type": "str",
                           "choices": ["disable",
                                       "enable"]},
                "subscription_id": {"required": False, "type": "str"},
                "tenant_id": {"required": False, "type": "str"},
                "type": {"required": False, "type": "str",
                         "choices": ["aci",
                                     "alicloud",
                                     "aws",
                                     "azure",
                                     "gcp",
                                     "nsx",
                                     "nuage",
                                     "oci",
                                     "openstack",
                                     "kubernetes",
                                     "vmware",
                                     "sepm",
                                     "aci-direct"]},
                "update_interval": {"required": False, "type": "int"},
                "use_metadata_iam": {"required": False, "type": "str",
                                     "choices": ["disable",
                                                 "enable"]},
                "user_id": {"required": False, "type": "str"},
                "username": {"required": False, "type": "str"},
                "vpc_id": {"required": False, "type": "str"}

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
