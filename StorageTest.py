
from time import time
import uuid
from wsgiref.handlers import format_date_time

from generated.azure_table_storage._azure_table_storage import AzureTableStorage
from generated.azure_table_storage.models._models import TableProperties
from azure.storage.blob._shared.authentication import SharedKeyCredentialPolicy

account_name = ""
account_key = ""
account_url = "https://{}.table.core.windows.net:443/".format(account_name)

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
print(client.table.query(headers=extra_headers))

