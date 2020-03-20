import requests
from c20_client import reggov_api_doc_error


def download_document(api_key, document_id=""):
    """
    downloads a file based on a url, api key and document_id (if given)
    """
    api_key = "&api_key=" + api_key
    document_id = "&documentId=" + document_id

    url = "https://api.data.gov:443/regulations/v3/document.json?"
    data = requests.get(url + api_key + document_id)
    if data.status_code == 400:
        raise reggov_api_doc_error.IncorrectIDPatternException
    if data.status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
    if data.status_code == 404:
        raise reggov_api_doc_error.BadDocIDException
    if data.status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException
    document = data.json()
    return document
