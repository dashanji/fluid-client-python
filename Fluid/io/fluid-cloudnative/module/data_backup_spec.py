# coding: utf-8

"""
    fluid

    client for fluid  # noqa: E501

    OpenAPI spec version: v0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from Fluid.io.fluid-cloudnative.module.user import User  # noqa: F401,E501


class DataBackupSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'backup_path': 'str',
        'dataset': 'str',
        'run_as': 'User'
    }

    attribute_map = {
        'backup_path': 'backupPath',
        'dataset': 'dataset',
        'run_as': 'runAs'
    }

    def __init__(self, backup_path=None, dataset=None, run_as=None):  # noqa: E501
        """DataBackupSpec - a model defined in Swagger"""  # noqa: E501

        self._backup_path = None
        self._dataset = None
        self._run_as = None
        self.discriminator = None

        if backup_path is not None:
            self.backup_path = backup_path
        if dataset is not None:
            self.dataset = dataset
        if run_as is not None:
            self.run_as = run_as

    @property
    def backup_path(self):
        """Gets the backup_path of this DataBackupSpec.  # noqa: E501

        BackupPath defines the target path to save data of the DataBackup  # noqa: E501

        :return: The backup_path of this DataBackupSpec.  # noqa: E501
        :rtype: str
        """
        return self._backup_path

    @backup_path.setter
    def backup_path(self, backup_path):
        """Sets the backup_path of this DataBackupSpec.

        BackupPath defines the target path to save data of the DataBackup  # noqa: E501

        :param backup_path: The backup_path of this DataBackupSpec.  # noqa: E501
        :type: str
        """

        self._backup_path = backup_path

    @property
    def dataset(self):
        """Gets the dataset of this DataBackupSpec.  # noqa: E501

        Dataset defines the target dataset of the DataBackup  # noqa: E501

        :return: The dataset of this DataBackupSpec.  # noqa: E501
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this DataBackupSpec.

        Dataset defines the target dataset of the DataBackup  # noqa: E501

        :param dataset: The dataset of this DataBackupSpec.  # noqa: E501
        :type: str
        """

        self._dataset = dataset

    @property
    def run_as(self):
        """Gets the run_as of this DataBackupSpec.  # noqa: E501

        Manage the user to run Alluxio DataBackup  # noqa: E501

        :return: The run_as of this DataBackupSpec.  # noqa: E501
        :rtype: User
        """
        return self._run_as

    @run_as.setter
    def run_as(self, run_as):
        """Sets the run_as of this DataBackupSpec.

        Manage the user to run Alluxio DataBackup  # noqa: E501

        :param run_as: The run_as of this DataBackupSpec.  # noqa: E501
        :type: User
        """

        self._run_as = run_as

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DataBackupSpec, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DataBackupSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
