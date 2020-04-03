"""
Get JSON data of documents endpoint from regulations.gov
"""
import requests
from c20_client import reggov_api_doc_error

URL = "https://api.data.gov:443/regulations/v3/documents.json?api_key="

def get_response_from_api(api_key, start_date, end_date):
    """
    Get JSON data for documents
    """
    crd = start_date + "-" + end_date

    response = requests.get(URL+api_key+"&crd="+crd)

    if response.status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
    if response.status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException

    return response.json()