# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, map_error

from ... import models


class DomainsOperations:
    """DomainsOperations async operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.graphrbac.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    
    def list(self, filter=None, cls=None, **kwargs):
        """Gets a list of domains for the current tenant.

        FIXME: add operation.summary


        :param filter: The filters to apply to the operation.
        :type filter: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: DomainListResult or the result of cls(response)
        :rtype: ~azure.graphrbac.models.DomainListResult
        :raises: ~azure.core.HttpResponseError
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}
            if filter is not None:
                query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(response):
            deserialized = self._deserialize('DomainListResult', response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response)

            return response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/{tenantID}/domains'}


    
    async def get(self, domain_name, cls=None, **kwargs):
        """Gets a specific domain in the current tenant.

        FIXME: add operation.summary

        :param domain_name: name of the domain.
        :type domain_name: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: Domain or the result of cls(response)
        :rtype: ~azure.graphrbac.models.Domain
        :raises: ~azure.core.HttpResponseError
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'domainName': self._serialize.url("domain_name", domain_name, 'str'),
            'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'


        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('Domain', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/{tenantID}/domains/{domainName}'}
