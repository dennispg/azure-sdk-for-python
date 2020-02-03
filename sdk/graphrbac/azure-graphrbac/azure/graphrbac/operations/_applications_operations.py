# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import warnings

from azure.core.exceptions import map_error
from azure.core.paging import ItemPaged

from .. import models


class ApplicationsOperations(object):
    """ApplicationsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.graphrbac.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    
    def create(self, parameters, cls=None, **kwargs):
        """Create a new application.

        FIXME: add operation.summary

        :param parameters: The parameters for creating an application.
        :type parameters: ~azure.graphrbac.models.ApplicationCreateParameters
        :param callable cls: A custom type or function that will be passed the direct response
        :return: Application or the result of cls(response)
        :rtype: ~azure.graphrbac.models.Application
        :raises: ~azure.graphrbac.models.GraphErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        # Construct URL
        url = self.create.metadata['url']
        path_format_arguments = {
            'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(parameters, 'ApplicationCreateParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.GraphErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('Application', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    create.metadata = {'url': '/{tenantID}/applications'}

    
    def list(self, filter=None, cls=None, **kwargs):
        """Lists applications by filter parameters.

        FIXME: add operation.summary


        :param filter: The filters to apply to the operation.
        :type filter: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: ApplicationListResult or the result of cls(response)
        :rtype: ~azure.graphrbac.models.ApplicationListResult
        :raises: ~azure.graphrbac.models.GraphErrorException:
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
                url = '/{tenantID}/{nextLink}'
                path_format_arguments = {
                    'nextLink': self._serialize.url("next_link", next_link, 'str', skip_quote=True),
                    'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)

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

        def extract_data(response):
            deserialized = self._deserialize('ApplicationListResult', response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.GraphErrorException.from_response(response, self._deserialize)

            return response

        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': '/{tenantID}/applications'}


    
    def delete(self, application_object_id, cls=None, **kwargs):
        """Delete an application.

        FIXME: add operation.summary

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.graphrbac.models.GraphErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
            'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.GraphErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    delete.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}'}

    
    def get(self, application_object_id, cls=None, **kwargs):
        """Get an application by object ID.

        FIXME: add operation.summary

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: Application or the result of cls(response)
        :rtype: ~azure.graphrbac.models.Application
        :raises: ~azure.graphrbac.models.GraphErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.GraphErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('Application', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}'}

    
    def patch(self, application_object_id, parameters, cls=None, **kwargs):
        """Update an existing application.

        FIXME: add operation.summary

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param parameters: Parameters to update an existing application.
        :type parameters: ~azure.graphrbac.models.ApplicationUpdateParameters
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.graphrbac.models.GraphErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        # Construct URL
        url = self.patch.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
            'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(parameters, 'ApplicationUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.GraphErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    patch.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}'}

    
    def list_owners(self, application_object_id, cls=None, **kwargs):
        """The owners are a set of non-admin users who are allowed to modify this object.

        FIXME: add operation.summary


        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: DirectoryObjectListResult or the result of cls(response)
        :rtype: ~azure.graphrbac.models.DirectoryObjectListResult
        :raises: ~azure.graphrbac.models.GraphErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_owners.metadata['url']
                path_format_arguments = {
                    'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
                    'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(response):
            deserialized = self._deserialize('DirectoryObjectListResult', response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.GraphErrorException.from_response(response, self._deserialize)

            return response

        return ItemPaged(
            get_next, extract_data
        )
    list_owners.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/owners'}


    
    def add_owner(self, application_object_id, url, cls=None, **kwargs):
        """Add an owner to an application.

        FIXME: add operation.summary

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param url: A owner object URL, such as "https://graph.windows.net/0b1f9851-1bf0-433f-aec3-cb9272f093dc/directoryObjects/f260bbc4-c254-447b-94cf-293b5ec434dd", where "0b1f9851-1bf0-433f-aec3-cb9272f093dc" is the tenantId and "f260bbc4-c254-447b-94cf-293b5ec434dd" is the objectId of the owner (user, application, servicePrincipal, group) to be added.
        :type url: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.graphrbac.models.GraphErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        parameters = models.AddOwnerParameters(url=url)
        api_version = "1.6"

        # Construct URL
        url = self.add_owner.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
            'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(parameters, 'AddOwnerParameters')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.GraphErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    add_owner.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/$links/owners'}

    
    def remove_owner(self, application_object_id, owner_object_id, cls=None, **kwargs):
        """Remove a member from owners.

        FIXME: add operation.summary

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param owner_object_id: Owner object id.
        :type owner_object_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.graphrbac.models.GraphErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        # Construct URL
        url = self.remove_owner.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
            'ownerObjectId': self._serialize.url("owner_object_id", owner_object_id, 'str'),
            'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


        # Construct headers
        header_parameters = {}


        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.GraphErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    remove_owner.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/$links/owners/{ownerObjectId}'}

    
    def list_key_credentials(self, application_object_id, cls=None, **kwargs):
        """Get the keyCredentials associated with an application.

        FIXME: add operation.summary


        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: KeyCredentialListResult or the result of cls(response)
        :rtype: ~azure.graphrbac.models.KeyCredentialListResult
        :raises: ~azure.graphrbac.models.GraphErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_key_credentials.metadata['url']
                path_format_arguments = {
                    'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
                    'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(response):
            deserialized = self._deserialize('KeyCredentialListResult', response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.GraphErrorException.from_response(response, self._deserialize)

            return response

        return ItemPaged(
            get_next, extract_data
        )
    list_key_credentials.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/keyCredentials'}


    
    def update_key_credentials(self, application_object_id, value, cls=None, **kwargs):
        """Update the keyCredentials associated with an application.

        FIXME: add operation.summary

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param value: A collection of KeyCredentials.
        :type value: list[~azure.graphrbac.models.KeyCredential]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.graphrbac.models.GraphErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        parameters = models.KeyCredentialsUpdateParameters(value=value)
        api_version = "1.6"

        # Construct URL
        url = self.update_key_credentials.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
            'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(parameters, 'KeyCredentialsUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.GraphErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    update_key_credentials.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/keyCredentials'}

    
    def list_password_credentials(self, application_object_id, cls=None, **kwargs):
        """Get the passwordCredentials associated with an application.

        FIXME: add operation.summary


        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: PasswordCredentialListResult or the result of cls(response)
        :rtype: ~azure.graphrbac.models.PasswordCredentialListResult
        :raises: ~azure.graphrbac.models.GraphErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_password_credentials.metadata['url']
                path_format_arguments = {
                    'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
                    'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}
            query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'


            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(response):
            deserialized = self._deserialize('PasswordCredentialListResult', response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise models.GraphErrorException.from_response(response, self._deserialize)

            return response

        return ItemPaged(
            get_next, extract_data
        )
    list_password_credentials.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/passwordCredentials'}


    
    def update_password_credentials(self, application_object_id, value, cls=None, **kwargs):
        """Update passwordCredentials associated with an application.

        FIXME: add operation.summary

        :param application_object_id: Application object ID.
        :type application_object_id: str
        :param value: A collection of PasswordCredentials.
        :type value: list[~azure.graphrbac.models.PasswordCredential]
        :param callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.graphrbac.models.GraphErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        parameters = models.PasswordCredentialsUpdateParameters(value=value)
        api_version = "1.6"

        # Construct URL
        url = self.update_password_credentials.metadata['url']
        path_format_arguments = {
            'applicationObjectId': self._serialize.url("application_object_id", application_object_id, 'str'),
            'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')


        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json'


        # Construct body
        body_content = self._serialize.body(parameters, 'PasswordCredentialsUpdateParameters')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.GraphErrorException.from_response(response, self._deserialize)

        if cls:
          return cls(response, None, {})

    update_password_credentials.metadata = {'url': '/{tenantID}/applications/{applicationObjectId}/passwordCredentials'}

    
    def get_service_principals_id_by_app_id(self, application_id, cls=None, **kwargs):
        """Gets an object id for a given application id from the current tenant.

        FIXME: add operation.summary

        :param application_id: The application ID.
        :type application_id: str
        :param callable cls: A custom type or function that will be passed the direct response
        :return: ServicePrincipalObjectResult or the result of cls(response)
        :rtype: ~azure.graphrbac.models.ServicePrincipalObjectResult
        :raises: ~azure.graphrbac.models.GraphErrorException:
        """
        error_map = kwargs.pop('error_map', {})
        api_version = "1.6"

        # Construct URL
        url = self.get_service_principals_id_by_app_id.metadata['url']
        path_format_arguments = {
            'tenantID': self._serialize.url("self._config.tenant_id", self._config.tenant_id, 'str'),
            'applicationID': self._serialize.url("application_id", application_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise models.GraphErrorException.from_response(response, self._deserialize)

        deserialized = self._deserialize('ServicePrincipalObjectResult', response)

        if cls:
          return cls(response, deserialized, {})

        return deserialized
    get_service_principals_id_by_app_id.metadata = {'url': '/{tenantID}/servicePrincipalsByAppId/{applicationID}/objectId'}
