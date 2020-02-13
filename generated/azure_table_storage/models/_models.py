# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.0.6220, generator: {generator})
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class AccessPolicy(msrest.serialization.Model):
    """An Access policy.

    All required parameters must be populated in order to send to Azure.

    :param start: Required. the date-time the policy is active.
    :type start: ~datetime.datetime
    :param expiry: Required. the date-time the policy expires.
    :type expiry: ~datetime.datetime
    :param permission: Required. the permissions for the acl policy.
    :type permission: str
    """

    _validation = {
        'start': {'required': True},
        'expiry': {'required': True},
        'permission': {'required': True},
    }

    _attribute_map = {
        'start': {'key': 'Start', 'type': 'iso-8601'},
        'expiry': {'key': 'Expiry', 'type': 'iso-8601'},
        'permission': {'key': 'Permission', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(AccessPolicy, self).__init__(**kwargs)
        self.start = kwargs.get('start', None)
        self.expiry = kwargs.get('expiry', None)
        self.permission = kwargs.get('permission', None)


class CorsRule(msrest.serialization.Model):
    """CORS is an HTTP feature that enables a web application running under one domain to access resources in another domain. Web browsers implement a security restriction known as same-origin policy that prevents a web page from calling APIs in a different domain; CORS provides a secure way to allow one domain (the origin domain) to call APIs in another domain.

    All required parameters must be populated in order to send to Azure.

    :param allowed_origins: Required. The origin domains that are permitted to make a request
     against the storage service via CORS. The origin domain is the domain from which the request
     originates. Note that the origin must be an exact case-sensitive match with the origin that the
     user age sends to the service. You can also use the wildcard character '*' to allow all origin
     domains to make requests via CORS.
    :type allowed_origins: str
    :param allowed_methods: Required. The methods (HTTP request verbs) that the origin domain may
     use for a CORS request. (comma separated).
    :type allowed_methods: str
    :param allowed_headers: Required. the request headers that the origin domain may specify on the
     CORS request.
    :type allowed_headers: str
    :param exposed_headers: Required. The response headers that may be sent in the response to the
     CORS request and exposed by the browser to the request issuer.
    :type exposed_headers: str
    :param max_age_in_seconds: Required. The maximum amount time that a browser should cache the
     preflight OPTIONS request.
    :type max_age_in_seconds: int
    """

    _validation = {
        'allowed_origins': {'required': True},
        'allowed_methods': {'required': True},
        'allowed_headers': {'required': True},
        'exposed_headers': {'required': True},
        'max_age_in_seconds': {'required': True, 'minimum': 0},
    }

    _attribute_map = {
        'allowed_origins': {'key': 'AllowedOrigins', 'type': 'str'},
        'allowed_methods': {'key': 'AllowedMethods', 'type': 'str'},
        'allowed_headers': {'key': 'AllowedHeaders', 'type': 'str'},
        'exposed_headers': {'key': 'ExposedHeaders', 'type': 'str'},
        'max_age_in_seconds': {'key': 'MaxAgeInSeconds', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CorsRule, self).__init__(**kwargs)
        self.allowed_origins = kwargs.get('allowed_origins', None)
        self.allowed_methods = kwargs.get('allowed_methods', None)
        self.allowed_headers = kwargs.get('allowed_headers', None)
        self.exposed_headers = kwargs.get('exposed_headers', None)
        self.max_age_in_seconds = kwargs.get('max_age_in_seconds', None)


class GeoReplication(msrest.serialization.Model):
    """GeoReplication.

    All required parameters must be populated in order to send to Azure.

    :param status: Required. The status of the secondary location. Possible values include: 'live',
     'bootstrap', 'unavailable'.
    :type status: str or ~azure_table_storage.models.GeoReplicationStatusType
    :param last_sync_time: Required. A GMT date/time value, to the second. All primary writes
     preceding this value are guaranteed to be available for read operations at the secondary.
     Primary writes after this point in time may or may not be available for reads.
    :type last_sync_time: ~datetime.datetime
    """

    _validation = {
        'status': {'required': True},
        'last_sync_time': {'required': True},
    }

    _attribute_map = {
        'status': {'key': 'Status', 'type': 'str'},
        'last_sync_time': {'key': 'LastSyncTime', 'type': 'rfc-1123'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(GeoReplication, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.last_sync_time = kwargs.get('last_sync_time', None)


class Logging(msrest.serialization.Model):
    """Azure Analytics Logging settings.

    All required parameters must be populated in order to send to Azure.

    :param version: Required. The version of Storage Analytics to configure.
    :type version: str
    :param delete: Required. Indicates whether all delete requests should be logged.
    :type delete: bool
    :param read: Required. Indicates whether all read requests should be logged.
    :type read: bool
    :param write: Required. Indicates whether all write requests should be logged.
    :type write: bool
    :param retention_policy: Required. the retention policy.
    :type retention_policy: ~azure_table_storage.models.RetentionPolicy
    """

    _validation = {
        'version': {'required': True},
        'delete': {'required': True},
        'read': {'required': True},
        'write': {'required': True},
        'retention_policy': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'Version', 'type': 'str'},
        'delete': {'key': 'Delete', 'type': 'bool'},
        'read': {'key': 'Read', 'type': 'bool'},
        'write': {'key': 'Write', 'type': 'bool'},
        'retention_policy': {'key': 'RetentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Logging, self).__init__(**kwargs)
        self.version = kwargs.get('version', None)
        self.delete = kwargs.get('delete', None)
        self.read = kwargs.get('read', None)
        self.write = kwargs.get('write', None)
        self.retention_policy = kwargs.get('retention_policy', None)


class Metrics(msrest.serialization.Model):
    """Metrics.

    All required parameters must be populated in order to send to Azure.

    :param version: The version of Storage Analytics to configure.
    :type version: str
    :param enabled: Required. Indicates whether metrics are enabled for the Queue service.
    :type enabled: bool
    :param include_apis: Indicates whether metrics should generate summary statistics for called
     API operations.
    :type include_apis: bool
    :param retention_policy: the retention policy.
    :type retention_policy: ~azure_table_storage.models.RetentionPolicy
    """

    _validation = {
        'enabled': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'Version', 'type': 'str'},
        'enabled': {'key': 'Enabled', 'type': 'bool'},
        'include_apis': {'key': 'IncludeAPIs', 'type': 'bool'},
        'retention_policy': {'key': 'RetentionPolicy', 'type': 'RetentionPolicy'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Metrics, self).__init__(**kwargs)
        self.version = kwargs.get('version', None)
        self.enabled = kwargs.get('enabled', None)
        self.include_apis = kwargs.get('include_apis', None)
        self.retention_policy = kwargs.get('retention_policy', None)


class QueryOptions(msrest.serialization.Model):
    """Parameter group.

    :param format: Specifies the media type for the response. Possible values include:
     'application/json;odata=nometadata', 'application/json;odata=minimalmetadata',
     'application/json;odata=fullmetadata'.
    :type format: str or ~azure_table_storage.models.Enum0
    :param top: Maximum number of records to return.
    :type top: int
    :param select: Select expression using OData notation. Limits the columns on each record to
     just those requested, e.g. "$select=PolicyAssignmentId, ResourceId".
    :type select: str
    :param filter: OData filter expression.
    :type filter: str
    """

    _validation = {
        'top': {'minimum': 0},
    }

    _attribute_map = {
        'format': {'key': 'Format', 'type': 'str'},
        'top': {'key': 'Top', 'type': 'int'},
        'select': {'key': 'Select', 'type': 'str'},
        'filter': {'key': 'Filter', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QueryOptions, self).__init__(**kwargs)
        self.format = kwargs.get('format', None)
        self.top = kwargs.get('top', None)
        self.select = kwargs.get('select', None)
        self.filter = kwargs.get('filter', None)


class RetentionPolicy(msrest.serialization.Model):
    """the retention policy.

    All required parameters must be populated in order to send to Azure.

    :param enabled: Required. Indicates whether a retention policy is enabled for the storage
     service.
    :type enabled: bool
    :param days: Indicates the number of days that metrics or logging or soft-deleted data should
     be retained. All data older than this value will be deleted.
    :type days: int
    """

    _validation = {
        'enabled': {'required': True},
        'days': {'minimum': 1},
    }

    _attribute_map = {
        'enabled': {'key': 'Enabled', 'type': 'bool'},
        'days': {'key': 'Days', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(RetentionPolicy, self).__init__(**kwargs)
        self.enabled = kwargs.get('enabled', None)
        self.days = kwargs.get('days', None)


class SignedIdentifier(msrest.serialization.Model):
    """signed identifier.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. a unique id.
    :type id: str
    :param access_policy: Required. An Access policy.
    :type access_policy: ~azure_table_storage.models.AccessPolicy
    """

    _validation = {
        'id': {'required': True},
        'access_policy': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'access_policy': {'key': 'AccessPolicy', 'type': 'AccessPolicy'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SignedIdentifier, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.access_policy = kwargs.get('access_policy', None)


class StorageErrorException(HttpResponseError):
    """Server responded with exception of type: 'StorageError'.

    :param response: Server response to be deserialized.
    :param error_model: A deserialized model of the response body as model.
    """

    def __init__(self, response, error_model):
        self.error = error_model
        super(StorageErrorException, self).__init__(response=response, error_model=error_model)

    @classmethod
    def from_response(cls, response, deserialize):
        """Deserialize this response as this exception, or a subclass of this exception.

        :param response: Server response to be deserialized.
        :param deserialize: A deserializer
        """
        model_name = 'StorageError'
        error = deserialize(model_name, response)
        if error is None:
            error = deserialize.dependencies[model_name]()
        return error._EXCEPTION_TYPE(response, error)


class StorageError(msrest.serialization.Model):
    """StorageError.

    :param message:
    :type message: str
    """
    _EXCEPTION_TYPE = StorageErrorException

    _attribute_map = {
        'message': {'key': 'Message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageError, self).__init__(**kwargs)
        self.message = kwargs.get('message', None)


class StorageServiceProperties(msrest.serialization.Model):
    """Storage Service Properties.

    :param logging: Azure Analytics Logging settings.
    :type logging: ~azure_table_storage.models.Logging
    :param hour_metrics:
    :type hour_metrics: ~azure_table_storage.models.Metrics
    :param minute_metrics:
    :type minute_metrics: ~azure_table_storage.models.Metrics
    :param cors: The set of CORS rules.
    :type cors: list[~azure_table_storage.models.CorsRule]
    """

    _attribute_map = {
        'logging': {'key': 'Logging', 'type': 'Logging'},
        'hour_metrics': {'key': 'HourMetrics', 'type': 'Metrics'},
        'minute_metrics': {'key': 'MinuteMetrics', 'type': 'Metrics'},
        'cors': {'key': 'Cors', 'type': '[CorsRule]', 'xml': {'wrapped': True}},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageServiceProperties, self).__init__(**kwargs)
        self.logging = kwargs.get('logging', None)
        self.hour_metrics = kwargs.get('hour_metrics', None)
        self.minute_metrics = kwargs.get('minute_metrics', None)
        self.cors = kwargs.get('cors', None)


class StorageServiceStats(msrest.serialization.Model):
    """Stats for the storage service.

    :param geo_replication:
    :type geo_replication: ~azure_table_storage.models.GeoReplication
    """

    _attribute_map = {
        'geo_replication': {'key': 'GeoReplication', 'type': 'GeoReplication'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(StorageServiceStats, self).__init__(**kwargs)
        self.geo_replication = kwargs.get('geo_replication', None)


class TableEntityQueryResponse(msrest.serialization.Model):
    """The properties for the table entity query response.

    :param odata_metadata: The metadata response of the table.
    :type odata_metadata: str
    :param value: List of table entities.
    :type value: list[dict[str, object]]
    """

    _attribute_map = {
        'odata_metadata': {'key': 'odata\\.metadata', 'type': 'str'},
        'value': {'key': 'value', 'type': '[{object}]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TableEntityQueryResponse, self).__init__(**kwargs)
        self.odata_metadata = kwargs.get('odata_metadata', None)
        self.value = kwargs.get('value', None)


class TableProperties(msrest.serialization.Model):
    """The properties for creating a table.

    :param table_name: The name of the table to create.
    :type table_name: str
    """

    _attribute_map = {
        'table_name': {'key': 'TableName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TableProperties, self).__init__(**kwargs)
        self.table_name = kwargs.get('table_name', None)


class TableQueryResponse(msrest.serialization.Model):
    """The properties for the table query response.

    :param odata_metadata: The metadata response of the table.
    :type odata_metadata: str
    :param value: List of tables.
    :type value: list[~azure_table_storage.models.TableResponseProperties]
    """

    _attribute_map = {
        'odata_metadata': {'key': 'odata\\.metadata', 'type': 'str'},
        'value': {'key': 'value', 'type': '[TableResponseProperties]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TableQueryResponse, self).__init__(**kwargs)
        self.odata_metadata = kwargs.get('odata_metadata', None)
        self.value = kwargs.get('value', None)


class TableResponseProperties(msrest.serialization.Model):
    """The properties for the table response.

    :param table_name: The name of the table.
    :type table_name: str
    :param odata_type: The odata type of the table.
    :type odata_type: str
    :param odata_id: The id of the table.
    :type odata_id: str
    :param odata_edit_link: The edit link of the table.
    :type odata_edit_link: str
    """

    _attribute_map = {
        'table_name': {'key': 'TableName', 'type': 'str'},
        'odata_type': {'key': 'odata\\.type', 'type': 'str'},
        'odata_id': {'key': 'odata\\.id', 'type': 'str'},
        'odata_edit_link': {'key': 'odata\\.editLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TableResponseProperties, self).__init__(**kwargs)
        self.table_name = kwargs.get('table_name', None)
        self.odata_type = kwargs.get('odata_type', None)
        self.odata_id = kwargs.get('odata_id', None)
        self.odata_edit_link = kwargs.get('odata_edit_link', None)


class TableResponse(TableResponseProperties):
    """The response for a single table.

    :param table_name: The name of the table.
    :type table_name: str
    :param odata_type: The odata type of the table.
    :type odata_type: str
    :param odata_id: The id of the table.
    :type odata_id: str
    :param odata_edit_link: The edit link of the table.
    :type odata_edit_link: str
    :param odata_metadata: The metadata response of the table.
    :type odata_metadata: str
    """

    _attribute_map = {
        'table_name': {'key': 'TableName', 'type': 'str'},
        'odata_type': {'key': 'odata\\.type', 'type': 'str'},
        'odata_id': {'key': 'odata\\.id', 'type': 'str'},
        'odata_edit_link': {'key': 'odata\\.editLink', 'type': 'str'},
        'odata_metadata': {'key': 'odata\\.metadata', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TableResponse, self).__init__(**kwargs)
        self.odata_metadata = kwargs.get('odata_metadata', None)
