
from time import time
import uuid
from wsgiref.handlers import format_date_time

from generated.azure_table_storage._azure_table_storage import AzureTableStorage
from generated.azure_table_storage.models._models import TableProperties
from azure.storage.blob._shared.authentication import SharedKeyCredentialPolicy

account_name = ""
account_key = ""
account_url = "https://{}.table.core.windows.net:443/".format(account_name)

account_name = ""
account_key = ""
account_url = "https://{}.table.cosmos.azure.com:443/".format(account_name)

class TablesSharedKeyCredentialPolicy(SharedKeyCredentialPolicy):

    def _get_canonicalized_resource_query(self, request):
        for name, value in request.http_request.query.items():
            if name == 'comp':
                return '?comp=' + value
        return ''

    def _get_headers(self, request, headers_to_sign):
        headers = dict((name.lower(), value) for name, value in request.http_request.headers.items() if value)
        return '\n'.join(headers.get(x, '') for x in headers_to_sign) + '\n'

    def on_request(self, request):
        string_to_sign = \
            self._get_verb(request) + \
            self._get_headers(
                request,
                ['content-md5', 'content-type', 'x-ms-date'],
            ) + \
            self._get_canonicalized_resource(request) + \
            self._get_canonicalized_resource_query(request)

        self._add_authorization_header(request, string_to_sign)


credential = TablesSharedKeyCredentialPolicy(account_name, account_key)

client = AzureTableStorage(account_url, authentication_policy=credential)
current_time = format_date_time(time())
extra_headers = {
    'Date': current_time,
    'x-ms-date': current_time,
    'x-ms-client-request-id': str(uuid.uuid1()),
}

# Create a Table
sample_table = TableProperties(table_name="sampletable6")
client.table.create(sample_table, headers=extra_headers)

# Create Entity
entity_properties = {"PartitionKey": "key1", "RowKey": "row1", "number": 15}
client.table.insert_entity(sample_table.table_name, table_entity_properties=entity_properties, headers=extra_headers)

# Update Entity - Fails for Cosmos DB
# b'{"odata.error":{"code":"MediaTypeNotSupported","message":{"lang":"en-us","value":"None of the provided media types are supported\\r\\n
# ActivityId: 3f9f275a-395f-446b-96c0-b900bc620eda, documentdb-dotnet-sdk/2.9.2 Host/64-bit MicrosoftWindowsNT/6.2.9200.0\\nRequestID:3f9f275a-395f-446b-96c0-b900bc620eda\\n"}}}\r\n'
entity_properties["number"] = 16
client.table.update_entity(sample_table.table_name, entity_properties["PartitionKey"], entity_properties["RowKey"], table_entity_properties=entity_properties, headers=extra_headers)

# Query Entity to Ensure it exists
entity = client.table.query_entities_with_partition_and_row_key(sample_table.table_name, entity_properties["PartitionKey"], entity_properties["RowKey"], headers=extra_headers)

# Delete Entity - Fails for Storage but not Cosmos DB accounts
# b'<?xml version="1.0" encoding="utf-8"?><error xmlns="http://schemas.microsoft.com/ado/2007/08/dataservices/metadata">
# <code>InvalidInput</code><message xml:lang="en-US">One of the request inputs is not valid.\nRequestId:6888f75d-c002-00a3-80ae-e2142b000000\nTime:2020-02-13T20:46:43.3583718Z</message></error>'
client.table.delete_entity(sample_table.table_name, entity_properties["PartitionKey"], entity_properties["RowKey"], headers=extra_headers)

# Query Entity to ensure none exist
entities = client.table.query_entities(sample_table.table_name, headers=extra_headers)
if len(entities.value) != 0:
    print("Entity not deleted correctly")

# Query Tables
tables = client.table.query(headers=extra_headers)
for table in tables.value:
    client.table.delete(table.table_name, headers=extra_headers)
