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

from enum import Enum


class CategoryType(str, Enum):

    cost = "Cost"
    usage = "Usage"


class TimeGrainType(str, Enum):

    monthly = "Monthly"
    quarterly = "Quarterly"
    annually = "Annually"


class OperatorType(str, Enum):

    equal_to = "EqualTo"
    greater_than = "GreaterThan"
    greater_than_or_equal_to = "GreaterThanOrEqualTo"


class Datagrain(str, Enum):

    daily_grain = "daily"
    monthly_grain = "monthly"
