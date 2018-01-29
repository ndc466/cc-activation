# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class DeploymentList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, fleet_sid):
        """
        Initialize the DeploymentList

        :param Version version: Version that contains the resource
        :param fleet_sid: The unique identifier of the Fleet.

        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentList
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentList
        """
        super(DeploymentList, self).__init__(version)

        # Path Solution
        self._solution = {
            'fleet_sid': fleet_sid,
        }
        self._uri = '/Fleets/{fleet_sid}/Deployments'.format(**self._solution)

    def create(self, friendly_name=values.unset, sync_service_sid=values.unset):
        """
        Create a new DeploymentInstance

        :param unicode friendly_name: A human readable description for this Deployment.
        :param unicode sync_service_sid: The unique identifier of the Sync service instance.

        :returns: Newly created DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'SyncServiceSid': sync_service_sid,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return DeploymentInstance(
            self._version,
            payload,
            fleet_sid=self._solution['fleet_sid'],
        )

    def stream(self, limit=None, page_size=None):
        """
        Streams DeploymentInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists DeploymentInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of DeploymentInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentPage
        """
        params = values.of({
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return DeploymentPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of DeploymentInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return DeploymentPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a DeploymentContext

        :param sid: A string that uniquely identifies the Deployment.

        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        """
        return DeploymentContext(
            self._version,
            fleet_sid=self._solution['fleet_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a DeploymentContext

        :param sid: A string that uniquely identifies the Deployment.

        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        """
        return DeploymentContext(
            self._version,
            fleet_sid=self._solution['fleet_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.DeploymentList>'


class DeploymentPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the DeploymentPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param fleet_sid: The unique identifier of the Fleet.

        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentPage
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentPage
        """
        super(DeploymentPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DeploymentInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        return DeploymentInstance(
            self._version,
            payload,
            fleet_sid=self._solution['fleet_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.DeployedDevices.DeploymentPage>'


class DeploymentContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, fleet_sid, sid):
        """
        Initialize the DeploymentContext

        :param Version version: Version that contains the resource
        :param fleet_sid: The fleet_sid
        :param sid: A string that uniquely identifies the Deployment.

        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        """
        super(DeploymentContext, self).__init__(version)

        # Path Solution
        self._solution = {
            'fleet_sid': fleet_sid,
            'sid': sid,
        }
        self._uri = '/Fleets/{fleet_sid}/Deployments/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a DeploymentInstance

        :returns: Fetched DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return DeploymentInstance(
            self._version,
            payload,
            fleet_sid=self._solution['fleet_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the DeploymentInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def update(self, friendly_name=values.unset, sync_service_sid=values.unset):
        """
        Update the DeploymentInstance

        :param unicode friendly_name: A human readable description for this Deployment.
        :param unicode sync_service_sid: The unique identifier of the Sync service instance.

        :returns: Updated DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
            'SyncServiceSid': sync_service_sid,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return DeploymentInstance(
            self._version,
            payload,
            fleet_sid=self._solution['fleet_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.DeployedDevices.DeploymentContext {}>'.format(context)


class DeploymentInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, fleet_sid, sid=None):
        """
        Initialize the DeploymentInstance

        :returns: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        super(DeploymentInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'url': payload['url'],
            'friendly_name': payload['friendly_name'],
            'fleet_sid': payload['fleet_sid'],
            'account_sid': payload['account_sid'],
            'sync_service_sid': payload['sync_service_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
        }

        # Context
        self._context = None
        self._solution = {
            'fleet_sid': fleet_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: DeploymentContext for this DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentContext
        """
        if self._context is None:
            self._context = DeploymentContext(
                self._version,
                fleet_sid=self._solution['fleet_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this Deployment.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def url(self):
        """
        :returns: URL of this Deployment.
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description for this Deployment
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def fleet_sid(self):
        """
        :returns: The unique identifier of the Fleet.
        :rtype: unicode
        """
        return self._properties['fleet_sid']

    @property
    def account_sid(self):
        """
        :returns: The unique SID that identifies this Account.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def sync_service_sid(self):
        """
        :returns: The unique identifier of the Sync service instance.
        :rtype: unicode
        """
        return self._properties['sync_service_sid']

    @property
    def date_created(self):
        """
        :returns: The date this Deployment was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this Deployment was updated.
        :rtype: datetime
        """
        return self._properties['date_updated']

    def fetch(self):
        """
        Fetch a DeploymentInstance

        :returns: Fetched DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the DeploymentInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def update(self, friendly_name=values.unset, sync_service_sid=values.unset):
        """
        Update the DeploymentInstance

        :param unicode friendly_name: A human readable description for this Deployment.
        :param unicode sync_service_sid: The unique identifier of the Sync service instance.

        :returns: Updated DeploymentInstance
        :rtype: twilio.rest.preview.deployed_devices.fleet.deployment.DeploymentInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            sync_service_sid=sync_service_sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.DeployedDevices.DeploymentInstance {}>'.format(context)
