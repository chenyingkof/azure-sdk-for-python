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

from .rule_data_source import RuleDataSource


class RuleMetricDataSource(RuleDataSource):
    """A rule metric data source. The discriminator value is always
    RuleMetricDataSource in this case.

    All required parameters must be populated in order to send to Azure.

    :param resource_uri: the resource identifier of the resource the rule
     monitors. **NOTE**: this property cannot be updated for an existing rule.
    :type resource_uri: str
    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param metric_name: the name of the metric that defines what the rule
     monitors.
    :type metric_name: str
    """

    _validation = {
        'odatatype': {'required': True},
    }

    _attribute_map = {
        'resource_uri': {'key': 'resourceUri', 'type': 'str'},
        'odatatype': {'key': 'odata\\.type', 'type': 'str'},
        'metric_name': {'key': 'metricName', 'type': 'str'},
    }

    def __init__(self, *, resource_uri: str=None, metric_name: str=None, **kwargs) -> None:
        super(RuleMetricDataSource, self).__init__(resource_uri=resource_uri, **kwargs)
        self.metric_name = metric_name
        self.odatatype = 'Microsoft.Azure.Management.Insights.Models.RuleMetricDataSource'
