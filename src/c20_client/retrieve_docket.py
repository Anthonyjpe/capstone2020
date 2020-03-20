"""
Contains class used to retreive dockets from regulations.gov
"""
import requests
from c20_client import reggov_api_doc_error
from c20_client.docket_packager import get_docket_package


def get_docket_data(api_key, url):
    """
    Makes call to regulations.gov and retrieves the docket data
    """
    # Add api_key to make a valid call to reg.gov
    active_url = url + "&api_key=" + api_key
    response = requests.get(active_url)

    if response.status_code == 400:
        raise reggov_api_doc_error.IncorrectIDPatternException
    if response.status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
    if response.status_code == 404:
        raise reggov_api_doc_error.BadDocIDException
    if response.status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException

    return response.json()


def get_docket(api_key, url):
    """
    Returns a package of the docket data and job as a JSON object
    """
    data = get_docket_data(api_key, url)
    return get_docket_package(data, url)
