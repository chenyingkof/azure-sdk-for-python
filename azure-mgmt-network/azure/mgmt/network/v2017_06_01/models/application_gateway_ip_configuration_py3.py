# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class ApplicationGatewayIPConfiguration(SubResource):
    """IP configuration of an application gateway. Currently 1 public and 1
    private IP configuration is allowed.

    :param id: Resource ID.
    :type id: str
    :param subnet: Reference of the subnet resource. A subnet from where
     application gateway gets its private address.
    :type subnet: ~azure.mgmt.network.v2017_06_01.models.SubResource
    :param provisioning_state: Provisioning state of the application gateway
     subnet resource. Possible values are: 'Updating', 'Deleting', and
     'Failed'.
    :type provisioning_state: str
    :param name: Name of the resource that is unique within a resource group.
     This name can be used to access the resource.
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated.
    :type etag: str
    :param type: Type of the resource.
    :type type: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subnet': {'key': 'properties.subnet', 'type': 'SubResource'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, subnet=None, provisioning_state: str=None, name: str=None, etag: str=None, type: str=None, **kwargs) -> None:
        super(ApplicationGatewayIPConfiguration, self).__init__(id=id, **kwargs)
        self.subnet = subnet
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
        self.type = type
