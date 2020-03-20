"""
Contains class used to retreive dockets from regulations.gov
"""
import json
import requests
from c20_server import reggov_api_doc_error


def jformat(obj):
    """
    Create formatted string from a JSON object
    """
    formatted = json.dumps(obj, sort_keys=True, indent=4)
    return formatted


def get_docket_data(api_key, url):
    """
    Makes call to regulations.gov and retrieves the docket data
    """
    try:
        # Put the api key into the url
        split_url = url.split("?")
        activated_url = split_url[0] + "?api_key=" + api_key + split_url[1]
    except Exception:
        raise IndexError

    response = requests.get(activated_url)

    if response.status_code == 400:
        raise reggov_api_doc_error.IncorrectIDPatternException
    if response.status_code == 403:
        raise reggov_api_doc_error.IncorrectApiKeyException
    if response.status_code == 404:
        raise reggov_api_doc_error.BadDocIDException
    if response.status_code == 429:
        raise reggov_api_doc_error.ExceedCallLimitException

    return response.json()


def get_data_string(api_key, url):
    """
    Return the JSON object as a easy to read string
    """
    return jformat(get_data_json(api_key, url))


def get_data_json(api_key, url):
    """
    Returns the JSON object under the key job
    """
    docket_information = get_docket_data(api_key, url)
    return {"data": docket_information}


def get_job_string(url):
    """
    Returns the current job as a formatted easy to read string
    """
    return jformat(get_job_json(url))


def get_job_json(url):
    """
    Returns the current job as a JSON with the keys type and id
    """
    return {"job": {"job_type": "docket", "url": url}}


def get_docket(api_key, url):
    """
    Returns the docket in the format of a JSON file with the current job
    and the data for the current job
    """
    job = get_job_string(url)
    data = get_data_string(api_key, url)
    docket = job[:-1] + ',' + data[1:]
    return json.loads(docket)
