from generated.azure_table_storage._azure_table_storage import AzureTableStorage
from generated.azure_table_storage.models._models import TableProperties
from azure.storage.blob._shared.authentication import SharedKeyCredentialPolicy

account_name = ""
account_key = ""
account_url = "https://{}.table.core.windows.net:443/".format(account_name)

# credential = {"account_name": account_name, "account_key": account_key}
credential = SharedKeyCredentialPolicy(account_name, account_key)

client = AzureTableStorage(account_url, authentication_policy=credential)
print(client.table.query())
