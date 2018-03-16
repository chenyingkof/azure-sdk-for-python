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

from msrest.serialization import Model


class ApplicationInsightsComponentProactiveDetectionConfiguration(Model):
    """Properties that define a ProactiveDetection configuration.

    :param name: The rule name
    :type name: str
    :param enabled: A flag that indicates whether this rule is enabled by the
     user
    :type enabled: bool
    :param send_emails_to_subscription_owners: A flag that indicated whether
     notifications on this rule should be sent to subscription owners
    :type send_emails_to_subscription_owners: bool
    :param custom_emails: Custom email addresses for this rule notifications
    :type custom_emails: list[str]
    :param last_updated_time: The last time this rule was updated
    :type last_updated_time: str
    :param rule_definitions: Static definitions of the ProactiveDetection
     configuration rule (same values for all components).
    :type rule_definitions:
     ~azure.mgmt.applicationinsights.models.ApplicationInsightsComponentProactiveDetectionConfigurationRuleDefinitions
    """

    _attribute_map = {
        'name': {'key': 'Name', 'type': 'str'},
        'enabled': {'key': 'Enabled', 'type': 'bool'},
        'send_emails_to_subscription_owners': {'key': 'SendEmailsToSubscriptionOwners', 'type': 'bool'},
        'custom_emails': {'key': 'CustomEmails', 'type': '[str]'},
        'last_updated_time': {'key': 'LastUpdatedTime', 'type': 'str'},
        'rule_definitions': {'key': 'RuleDefinitions', 'type': 'ApplicationInsightsComponentProactiveDetectionConfigurationRuleDefinitions'},
    }

    def __init__(self, **kwargs):
        super(ApplicationInsightsComponentProactiveDetectionConfiguration, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.enabled = kwargs.get('enabled', None)
        self.send_emails_to_subscription_owners = kwargs.get('send_emails_to_subscription_owners', None)
        self.custom_emails = kwargs.get('custom_emails', None)
        self.last_updated_time = kwargs.get('last_updated_time', None)
        self.rule_definitions = kwargs.get('rule_definitions', None)
