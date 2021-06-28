# evpn-ipsec-dci-ansible
evpn-ipsec-dci-ansible

This is a topology the has two datacenters using a SPINE and LEAF network desing.
Interconnceted by 2 Fortigate Firewalls using BGP over an IPSec tunnel.

The Automation of the topology is done in Ansible.

Roles have been defined for the different service functions in the topology.
- SPINE Role
- LEAF Role
- EXIT Role

Also defined are playbooks for
- Firewall
- Spines
- Leafs
- Borders
![EVPN DCI FGT Topology](evpn-dci-ftg.png)
