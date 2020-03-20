"""
Packages the data and the job of a docket into a single JSON object
"""
import json

def jformat(obj):
    """
    Create formatted string from a JSON object
    """
    formatted = json.dumps(obj, sort_keys=True, indent=4)
    return formatted


def get_data_string(data):
    """
    Return the JSON object as a easy to read string
    """
    return jformat(get_data_json(data))


def get_data_json(data):
    """
    Returns the JSON object under the key job
    """
    return {"data": data}


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


def get_docket_package(data, url):
    """
    Returns the docket in the format of a JSON file with the current job
    and the data for the current job
    """
    job = get_job_string(url)
    data = get_data_string(data)
    # Concatenate the two strings to be one string to make a json obj
    docket = job[:-1] + ',' + data[1:]
    return json.loads(docket)
