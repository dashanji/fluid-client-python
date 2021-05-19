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

from Fluid.io.fluid-cloudnative.module.api_gateway_status import APIGatewayStatus  # noqa: F401,E501
from Fluid.io.fluid-cloudnative.module.runtime_condition import RuntimeCondition  # noqa: F401,E501


class RuntimeStatus(object):
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
        'api_gateway': 'APIGatewayStatus',
        'cache_states': 'dict(str, str)',
        'conditions': 'list[RuntimeCondition]',
        'current_fuse_number_scheduled': 'int',
        'current_master_number_scheduled': 'int',
        'current_worker_number_scheduled': 'int',
        'desired_fuse_number_scheduled': 'int',
        'desired_master_number_scheduled': 'int',
        'desired_worker_number_scheduled': 'int',
        'fuse_number_available': 'int',
        'fuse_number_ready': 'int',
        'fuse_number_unavailable': 'int',
        'fuse_phase': 'str',
        'fuse_reason': 'str',
        'master_number_ready': 'int',
        'master_phase': 'str',
        'master_reason': 'str',
        'selector': 'str',
        'setup_duration': 'str',
        'value_file': 'str',
        'worker_number_available': 'int',
        'worker_number_ready': 'int',
        'worker_number_unavailable': 'int',
        'worker_phase': 'str',
        'worker_reason': 'str'
    }

    attribute_map = {
        'api_gateway': 'apiGateway',
        'cache_states': 'cacheStates',
        'conditions': 'conditions',
        'current_fuse_number_scheduled': 'currentFuseNumberScheduled',
        'current_master_number_scheduled': 'currentMasterNumberScheduled',
        'current_worker_number_scheduled': 'currentWorkerNumberScheduled',
        'desired_fuse_number_scheduled': 'desiredFuseNumberScheduled',
        'desired_master_number_scheduled': 'desiredMasterNumberScheduled',
        'desired_worker_number_scheduled': 'desiredWorkerNumberScheduled',
        'fuse_number_available': 'fuseNumberAvailable',
        'fuse_number_ready': 'fuseNumberReady',
        'fuse_number_unavailable': 'fuseNumberUnavailable',
        'fuse_phase': 'fusePhase',
        'fuse_reason': 'fuseReason',
        'master_number_ready': 'masterNumberReady',
        'master_phase': 'masterPhase',
        'master_reason': 'masterReason',
        'selector': 'selector',
        'setup_duration': 'setupDuration',
        'value_file': 'valueFile',
        'worker_number_available': 'workerNumberAvailable',
        'worker_number_ready': 'workerNumberReady',
        'worker_number_unavailable': 'workerNumberUnavailable',
        'worker_phase': 'workerPhase',
        'worker_reason': 'workerReason'
    }

    def __init__(self, api_gateway=None, cache_states=None, conditions=None, current_fuse_number_scheduled=None, current_master_number_scheduled=None, current_worker_number_scheduled=None, desired_fuse_number_scheduled=None, desired_master_number_scheduled=None, desired_worker_number_scheduled=None, fuse_number_available=None, fuse_number_ready=None, fuse_number_unavailable=None, fuse_phase=None, fuse_reason=None, master_number_ready=None, master_phase=None, master_reason=None, selector=None, setup_duration=None, value_file=None, worker_number_available=None, worker_number_ready=None, worker_number_unavailable=None, worker_phase=None, worker_reason=None):  # noqa: E501
        """RuntimeStatus - a model defined in Swagger"""  # noqa: E501

        self._api_gateway = None
        self._cache_states = None
        self._conditions = None
        self._current_fuse_number_scheduled = None
        self._current_master_number_scheduled = None
        self._current_worker_number_scheduled = None
        self._desired_fuse_number_scheduled = None
        self._desired_master_number_scheduled = None
        self._desired_worker_number_scheduled = None
        self._fuse_number_available = None
        self._fuse_number_ready = None
        self._fuse_number_unavailable = None
        self._fuse_phase = None
        self._fuse_reason = None
        self._master_number_ready = None
        self._master_phase = None
        self._master_reason = None
        self._selector = None
        self._setup_duration = None
        self._value_file = None
        self._worker_number_available = None
        self._worker_number_ready = None
        self._worker_number_unavailable = None
        self._worker_phase = None
        self._worker_reason = None
        self.discriminator = None

        if api_gateway is not None:
            self.api_gateway = api_gateway
        if cache_states is not None:
            self.cache_states = cache_states
        if conditions is not None:
            self.conditions = conditions
        self.current_fuse_number_scheduled = current_fuse_number_scheduled
        self.current_master_number_scheduled = current_master_number_scheduled
        self.current_worker_number_scheduled = current_worker_number_scheduled
        self.desired_fuse_number_scheduled = desired_fuse_number_scheduled
        self.desired_master_number_scheduled = desired_master_number_scheduled
        self.desired_worker_number_scheduled = desired_worker_number_scheduled
        if fuse_number_available is not None:
            self.fuse_number_available = fuse_number_available
        self.fuse_number_ready = fuse_number_ready
        if fuse_number_unavailable is not None:
            self.fuse_number_unavailable = fuse_number_unavailable
        self.fuse_phase = fuse_phase
        if fuse_reason is not None:
            self.fuse_reason = fuse_reason
        self.master_number_ready = master_number_ready
        self.master_phase = master_phase
        if master_reason is not None:
            self.master_reason = master_reason
        if selector is not None:
            self.selector = selector
        if setup_duration is not None:
            self.setup_duration = setup_duration
        self.value_file = value_file
        if worker_number_available is not None:
            self.worker_number_available = worker_number_available
        self.worker_number_ready = worker_number_ready
        if worker_number_unavailable is not None:
            self.worker_number_unavailable = worker_number_unavailable
        self.worker_phase = worker_phase
        if worker_reason is not None:
            self.worker_reason = worker_reason

    @property
    def api_gateway(self):
        """Gets the api_gateway of this RuntimeStatus.  # noqa: E501

        APIGatewayStatus represents rest api gateway status  # noqa: E501

        :return: The api_gateway of this RuntimeStatus.  # noqa: E501
        :rtype: APIGatewayStatus
        """
        return self._api_gateway

    @api_gateway.setter
    def api_gateway(self, api_gateway):
        """Sets the api_gateway of this RuntimeStatus.

        APIGatewayStatus represents rest api gateway status  # noqa: E501

        :param api_gateway: The api_gateway of this RuntimeStatus.  # noqa: E501
        :type: APIGatewayStatus
        """

        self._api_gateway = api_gateway

    @property
    def cache_states(self):
        """Gets the cache_states of this RuntimeStatus.  # noqa: E501

        CacheStatus represents the total resources of the dataset.  # noqa: E501

        :return: The cache_states of this RuntimeStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._cache_states

    @cache_states.setter
    def cache_states(self, cache_states):
        """Sets the cache_states of this RuntimeStatus.

        CacheStatus represents the total resources of the dataset.  # noqa: E501

        :param cache_states: The cache_states of this RuntimeStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._cache_states = cache_states

    @property
    def conditions(self):
        """Gets the conditions of this RuntimeStatus.  # noqa: E501

        Represents the latest available observations of a ddc runtime's current state.  # noqa: E501

        :return: The conditions of this RuntimeStatus.  # noqa: E501
        :rtype: list[RuntimeCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this RuntimeStatus.

        Represents the latest available observations of a ddc runtime's current state.  # noqa: E501

        :param conditions: The conditions of this RuntimeStatus.  # noqa: E501
        :type: list[RuntimeCondition]
        """

        self._conditions = conditions

    @property
    def current_fuse_number_scheduled(self):
        """Gets the current_fuse_number_scheduled of this RuntimeStatus.  # noqa: E501

        The total number of nodes that can be running the runtime Fuse pod (including nodes correctly running the runtime Fuse pod).  # noqa: E501

        :return: The current_fuse_number_scheduled of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_fuse_number_scheduled

    @current_fuse_number_scheduled.setter
    def current_fuse_number_scheduled(self, current_fuse_number_scheduled):
        """Sets the current_fuse_number_scheduled of this RuntimeStatus.

        The total number of nodes that can be running the runtime Fuse pod (including nodes correctly running the runtime Fuse pod).  # noqa: E501

        :param current_fuse_number_scheduled: The current_fuse_number_scheduled of this RuntimeStatus.  # noqa: E501
        :type: int
        """
        if current_fuse_number_scheduled is None:
            raise ValueError("Invalid value for `current_fuse_number_scheduled`, must not be `None`")  # noqa: E501

        self._current_fuse_number_scheduled = current_fuse_number_scheduled

    @property
    def current_master_number_scheduled(self):
        """Gets the current_master_number_scheduled of this RuntimeStatus.  # noqa: E501

        The total number of nodes that should be running the runtime pod (including nodes correctly running the runtime master pod).  # noqa: E501

        :return: The current_master_number_scheduled of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_master_number_scheduled

    @current_master_number_scheduled.setter
    def current_master_number_scheduled(self, current_master_number_scheduled):
        """Sets the current_master_number_scheduled of this RuntimeStatus.

        The total number of nodes that should be running the runtime pod (including nodes correctly running the runtime master pod).  # noqa: E501

        :param current_master_number_scheduled: The current_master_number_scheduled of this RuntimeStatus.  # noqa: E501
        :type: int
        """
        if current_master_number_scheduled is None:
            raise ValueError("Invalid value for `current_master_number_scheduled`, must not be `None`")  # noqa: E501

        self._current_master_number_scheduled = current_master_number_scheduled

    @property
    def current_worker_number_scheduled(self):
        """Gets the current_worker_number_scheduled of this RuntimeStatus.  # noqa: E501

        The total number of nodes that can be running the runtime worker pod (including nodes correctly running the runtime worker pod).  # noqa: E501

        :return: The current_worker_number_scheduled of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_worker_number_scheduled

    @current_worker_number_scheduled.setter
    def current_worker_number_scheduled(self, current_worker_number_scheduled):
        """Sets the current_worker_number_scheduled of this RuntimeStatus.

        The total number of nodes that can be running the runtime worker pod (including nodes correctly running the runtime worker pod).  # noqa: E501

        :param current_worker_number_scheduled: The current_worker_number_scheduled of this RuntimeStatus.  # noqa: E501
        :type: int
        """
        if current_worker_number_scheduled is None:
            raise ValueError("Invalid value for `current_worker_number_scheduled`, must not be `None`")  # noqa: E501

        self._current_worker_number_scheduled = current_worker_number_scheduled

    @property
    def desired_fuse_number_scheduled(self):
        """Gets the desired_fuse_number_scheduled of this RuntimeStatus.  # noqa: E501

        The total number of nodes that should be running the runtime Fuse pod (including nodes correctly running the runtime Fuse pod).  # noqa: E501

        :return: The desired_fuse_number_scheduled of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._desired_fuse_number_scheduled

    @desired_fuse_number_scheduled.setter
    def desired_fuse_number_scheduled(self, desired_fuse_number_scheduled):
        """Sets the desired_fuse_number_scheduled of this RuntimeStatus.

        The total number of nodes that should be running the runtime Fuse pod (including nodes correctly running the runtime Fuse pod).  # noqa: E501

        :param desired_fuse_number_scheduled: The desired_fuse_number_scheduled of this RuntimeStatus.  # noqa: E501
        :type: int
        """
        if desired_fuse_number_scheduled is None:
            raise ValueError("Invalid value for `desired_fuse_number_scheduled`, must not be `None`")  # noqa: E501

        self._desired_fuse_number_scheduled = desired_fuse_number_scheduled

    @property
    def desired_master_number_scheduled(self):
        """Gets the desired_master_number_scheduled of this RuntimeStatus.  # noqa: E501

        The total number of nodes that should be running the runtime pod (including nodes correctly running the runtime master pod).  # noqa: E501

        :return: The desired_master_number_scheduled of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._desired_master_number_scheduled

    @desired_master_number_scheduled.setter
    def desired_master_number_scheduled(self, desired_master_number_scheduled):
        """Sets the desired_master_number_scheduled of this RuntimeStatus.

        The total number of nodes that should be running the runtime pod (including nodes correctly running the runtime master pod).  # noqa: E501

        :param desired_master_number_scheduled: The desired_master_number_scheduled of this RuntimeStatus.  # noqa: E501
        :type: int
        """
        if desired_master_number_scheduled is None:
            raise ValueError("Invalid value for `desired_master_number_scheduled`, must not be `None`")  # noqa: E501

        self._desired_master_number_scheduled = desired_master_number_scheduled

    @property
    def desired_worker_number_scheduled(self):
        """Gets the desired_worker_number_scheduled of this RuntimeStatus.  # noqa: E501

        The total number of nodes that should be running the runtime worker pod (including nodes correctly running the runtime worker pod).  # noqa: E501

        :return: The desired_worker_number_scheduled of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._desired_worker_number_scheduled

    @desired_worker_number_scheduled.setter
    def desired_worker_number_scheduled(self, desired_worker_number_scheduled):
        """Sets the desired_worker_number_scheduled of this RuntimeStatus.

        The total number of nodes that should be running the runtime worker pod (including nodes correctly running the runtime worker pod).  # noqa: E501

        :param desired_worker_number_scheduled: The desired_worker_number_scheduled of this RuntimeStatus.  # noqa: E501
        :type: int
        """
        if desired_worker_number_scheduled is None:
            raise ValueError("Invalid value for `desired_worker_number_scheduled`, must not be `None`")  # noqa: E501

        self._desired_worker_number_scheduled = desired_worker_number_scheduled

    @property
    def fuse_number_available(self):
        """Gets the fuse_number_available of this RuntimeStatus.  # noqa: E501

        The number of nodes that should be running the runtime Fuse pod and have one or more of the runtime Fuse pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :return: The fuse_number_available of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._fuse_number_available

    @fuse_number_available.setter
    def fuse_number_available(self, fuse_number_available):
        """Sets the fuse_number_available of this RuntimeStatus.

        The number of nodes that should be running the runtime Fuse pod and have one or more of the runtime Fuse pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :param fuse_number_available: The fuse_number_available of this RuntimeStatus.  # noqa: E501
        :type: int
        """

        self._fuse_number_available = fuse_number_available

    @property
    def fuse_number_ready(self):
        """Gets the fuse_number_ready of this RuntimeStatus.  # noqa: E501

        The number of nodes that should be running the runtime Fuse pod and have one or more of the runtime Fuse pod running and ready.  # noqa: E501

        :return: The fuse_number_ready of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._fuse_number_ready

    @fuse_number_ready.setter
    def fuse_number_ready(self, fuse_number_ready):
        """Sets the fuse_number_ready of this RuntimeStatus.

        The number of nodes that should be running the runtime Fuse pod and have one or more of the runtime Fuse pod running and ready.  # noqa: E501

        :param fuse_number_ready: The fuse_number_ready of this RuntimeStatus.  # noqa: E501
        :type: int
        """
        if fuse_number_ready is None:
            raise ValueError("Invalid value for `fuse_number_ready`, must not be `None`")  # noqa: E501

        self._fuse_number_ready = fuse_number_ready

    @property
    def fuse_number_unavailable(self):
        """Gets the fuse_number_unavailable of this RuntimeStatus.  # noqa: E501

        The number of nodes that should be running the runtime fuse pod and have none of the runtime fuse pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :return: The fuse_number_unavailable of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._fuse_number_unavailable

    @fuse_number_unavailable.setter
    def fuse_number_unavailable(self, fuse_number_unavailable):
        """Sets the fuse_number_unavailable of this RuntimeStatus.

        The number of nodes that should be running the runtime fuse pod and have none of the runtime fuse pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :param fuse_number_unavailable: The fuse_number_unavailable of this RuntimeStatus.  # noqa: E501
        :type: int
        """

        self._fuse_number_unavailable = fuse_number_unavailable

    @property
    def fuse_phase(self):
        """Gets the fuse_phase of this RuntimeStatus.  # noqa: E501

        FusePhase is the Fuse running phase  # noqa: E501

        :return: The fuse_phase of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._fuse_phase

    @fuse_phase.setter
    def fuse_phase(self, fuse_phase):
        """Sets the fuse_phase of this RuntimeStatus.

        FusePhase is the Fuse running phase  # noqa: E501

        :param fuse_phase: The fuse_phase of this RuntimeStatus.  # noqa: E501
        :type: str
        """
        if fuse_phase is None:
            raise ValueError("Invalid value for `fuse_phase`, must not be `None`")  # noqa: E501

        self._fuse_phase = fuse_phase

    @property
    def fuse_reason(self):
        """Gets the fuse_reason of this RuntimeStatus.  # noqa: E501

        Reason for the condition's last transition.  # noqa: E501

        :return: The fuse_reason of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._fuse_reason

    @fuse_reason.setter
    def fuse_reason(self, fuse_reason):
        """Sets the fuse_reason of this RuntimeStatus.

        Reason for the condition's last transition.  # noqa: E501

        :param fuse_reason: The fuse_reason of this RuntimeStatus.  # noqa: E501
        :type: str
        """

        self._fuse_reason = fuse_reason

    @property
    def master_number_ready(self):
        """Gets the master_number_ready of this RuntimeStatus.  # noqa: E501

        The number of nodes that should be running the runtime worker pod and have zero or more of the runtime master pod running and ready.  # noqa: E501

        :return: The master_number_ready of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._master_number_ready

    @master_number_ready.setter
    def master_number_ready(self, master_number_ready):
        """Sets the master_number_ready of this RuntimeStatus.

        The number of nodes that should be running the runtime worker pod and have zero or more of the runtime master pod running and ready.  # noqa: E501

        :param master_number_ready: The master_number_ready of this RuntimeStatus.  # noqa: E501
        :type: int
        """
        if master_number_ready is None:
            raise ValueError("Invalid value for `master_number_ready`, must not be `None`")  # noqa: E501

        self._master_number_ready = master_number_ready

    @property
    def master_phase(self):
        """Gets the master_phase of this RuntimeStatus.  # noqa: E501

        MasterPhase is the master running phase  # noqa: E501

        :return: The master_phase of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._master_phase

    @master_phase.setter
    def master_phase(self, master_phase):
        """Sets the master_phase of this RuntimeStatus.

        MasterPhase is the master running phase  # noqa: E501

        :param master_phase: The master_phase of this RuntimeStatus.  # noqa: E501
        :type: str
        """
        if master_phase is None:
            raise ValueError("Invalid value for `master_phase`, must not be `None`")  # noqa: E501

        self._master_phase = master_phase

    @property
    def master_reason(self):
        """Gets the master_reason of this RuntimeStatus.  # noqa: E501

        Reason for Master's condition transition  # noqa: E501

        :return: The master_reason of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._master_reason

    @master_reason.setter
    def master_reason(self, master_reason):
        """Sets the master_reason of this RuntimeStatus.

        Reason for Master's condition transition  # noqa: E501

        :param master_reason: The master_reason of this RuntimeStatus.  # noqa: E501
        :type: str
        """

        self._master_reason = master_reason

    @property
    def selector(self):
        """Gets the selector of this RuntimeStatus.  # noqa: E501

        Selector is used for auto-scaling  # noqa: E501

        :return: The selector of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this RuntimeStatus.

        Selector is used for auto-scaling  # noqa: E501

        :param selector: The selector of this RuntimeStatus.  # noqa: E501
        :type: str
        """

        self._selector = selector

    @property
    def setup_duration(self):
        """Gets the setup_duration of this RuntimeStatus.  # noqa: E501

        Duration tell user how much time was spent to setup the runtime  # noqa: E501

        :return: The setup_duration of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._setup_duration

    @setup_duration.setter
    def setup_duration(self, setup_duration):
        """Sets the setup_duration of this RuntimeStatus.

        Duration tell user how much time was spent to setup the runtime  # noqa: E501

        :param setup_duration: The setup_duration of this RuntimeStatus.  # noqa: E501
        :type: str
        """

        self._setup_duration = setup_duration

    @property
    def value_file(self):
        """Gets the value_file of this RuntimeStatus.  # noqa: E501

        config map used to set configurations  # noqa: E501

        :return: The value_file of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._value_file

    @value_file.setter
    def value_file(self, value_file):
        """Sets the value_file of this RuntimeStatus.

        config map used to set configurations  # noqa: E501

        :param value_file: The value_file of this RuntimeStatus.  # noqa: E501
        :type: str
        """
        if value_file is None:
            raise ValueError("Invalid value for `value_file`, must not be `None`")  # noqa: E501

        self._value_file = value_file

    @property
    def worker_number_available(self):
        """Gets the worker_number_available of this RuntimeStatus.  # noqa: E501

        The number of nodes that should be running the runtime worker pod and have one or more of the runtime worker pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :return: The worker_number_available of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._worker_number_available

    @worker_number_available.setter
    def worker_number_available(self, worker_number_available):
        """Sets the worker_number_available of this RuntimeStatus.

        The number of nodes that should be running the runtime worker pod and have one or more of the runtime worker pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :param worker_number_available: The worker_number_available of this RuntimeStatus.  # noqa: E501
        :type: int
        """

        self._worker_number_available = worker_number_available

    @property
    def worker_number_ready(self):
        """Gets the worker_number_ready of this RuntimeStatus.  # noqa: E501

        The number of nodes that should be running the runtime worker pod and have one or more of the runtime worker pod running and ready.  # noqa: E501

        :return: The worker_number_ready of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._worker_number_ready

    @worker_number_ready.setter
    def worker_number_ready(self, worker_number_ready):
        """Sets the worker_number_ready of this RuntimeStatus.

        The number of nodes that should be running the runtime worker pod and have one or more of the runtime worker pod running and ready.  # noqa: E501

        :param worker_number_ready: The worker_number_ready of this RuntimeStatus.  # noqa: E501
        :type: int
        """
        if worker_number_ready is None:
            raise ValueError("Invalid value for `worker_number_ready`, must not be `None`")  # noqa: E501

        self._worker_number_ready = worker_number_ready

    @property
    def worker_number_unavailable(self):
        """Gets the worker_number_unavailable of this RuntimeStatus.  # noqa: E501

        The number of nodes that should be running the runtime worker pod and have none of the runtime worker pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :return: The worker_number_unavailable of this RuntimeStatus.  # noqa: E501
        :rtype: int
        """
        return self._worker_number_unavailable

    @worker_number_unavailable.setter
    def worker_number_unavailable(self, worker_number_unavailable):
        """Sets the worker_number_unavailable of this RuntimeStatus.

        The number of nodes that should be running the runtime worker pod and have none of the runtime worker pod running and available (ready for at least spec.minReadySeconds)  # noqa: E501

        :param worker_number_unavailable: The worker_number_unavailable of this RuntimeStatus.  # noqa: E501
        :type: int
        """

        self._worker_number_unavailable = worker_number_unavailable

    @property
    def worker_phase(self):
        """Gets the worker_phase of this RuntimeStatus.  # noqa: E501

        WorkerPhase is the worker running phase  # noqa: E501

        :return: The worker_phase of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._worker_phase

    @worker_phase.setter
    def worker_phase(self, worker_phase):
        """Sets the worker_phase of this RuntimeStatus.

        WorkerPhase is the worker running phase  # noqa: E501

        :param worker_phase: The worker_phase of this RuntimeStatus.  # noqa: E501
        :type: str
        """
        if worker_phase is None:
            raise ValueError("Invalid value for `worker_phase`, must not be `None`")  # noqa: E501

        self._worker_phase = worker_phase

    @property
    def worker_reason(self):
        """Gets the worker_reason of this RuntimeStatus.  # noqa: E501

        Reason for Worker's condition transition  # noqa: E501

        :return: The worker_reason of this RuntimeStatus.  # noqa: E501
        :rtype: str
        """
        return self._worker_reason

    @worker_reason.setter
    def worker_reason(self, worker_reason):
        """Sets the worker_reason of this RuntimeStatus.

        Reason for Worker's condition transition  # noqa: E501

        :param worker_reason: The worker_reason of this RuntimeStatus.  # noqa: E501
        :type: str
        """

        self._worker_reason = worker_reason

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
        if issubclass(RuntimeStatus, dict):
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
        if not isinstance(other, RuntimeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
