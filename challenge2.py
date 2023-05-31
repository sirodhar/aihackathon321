from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

endpoint = 'https://searchaihackathon321dummy.search.windows.net'
index_name = 'margis-index'
api_version = '2021-04-30'
api_key = 'tXNKheBcRlrGd07s0BJ0HKdmIMm2mOzRNiMBO9Ncw9AzSeAsi9T7'
credential = AzureKeyCredential(api_key)
client = SearchClient(endpoint=endpoint, index_name=index_name, credential=credential, api_version=api_version)

search_results = client.search(search_text='your-search-term')

for result in search_results:
    print(result)

