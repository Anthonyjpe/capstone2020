"""
Test the retrieve_docket.py file
"""
import requests_mock
import pytest
from c20_server.retrieve_docket import (
    jformat,
    get_docket,
    get_data_json,
    get_data_string,
    get_job_string,
    get_job_json
)
from c20_server import reggov_api_doc_error

NO_ID_URL = "https://api.data.gov:443/regulations/v3/docket.json?&docketId="
MOCK_URL = "https://api.data.gov:443/regulations/v3/docket.json?api_key="
API_KEY = "VALID KEY"
DOCKET_ID = "EPA-HQ-OAR-2011-0028"


def test_get_docket():
    with requests_mock.Mocker() as mock:
        mock.get(MOCK_URL + API_KEY + "&docketID=" + DOCKET_ID,
                 json={'test': 'The test is successful'})
        response = get_docket(API_KEY, NO_ID_URL + DOCKET_ID)

        assert (response ==
                {'data': {'test': 'The test is successful'},
                 'job': {'url': NO_ID_URL + DOCKET_ID, 'job_type': 'docket'}})


def test_bad_docket_id():
    with requests_mock.Mocker() as mock:
        bad_docket = DOCKET_ID + '-0101'
        mock.get(MOCK_URL + API_KEY + "&docketID=" + bad_docket,
                 json='The test yields a bad id', status_code=404)

        with pytest.raises(reggov_api_doc_error.BadDocIDException):
            get_docket(API_KEY, NO_ID_URL + bad_docket)


def test_no_docket_id():
    with requests_mock.Mocker() as mock:
        mock.get(MOCK_URL + API_KEY + "&docketID=",
                 json='The test yields a bad id', status_code=404)

        with pytest.raises(reggov_api_doc_error.BadDocIDException):
            get_docket(API_KEY, NO_ID_URL)


def test_bad_docket_id_pattern():
    with requests_mock.Mocker() as mock:
        bad_docket = 'b4d' + DOCKET_ID + 'b4d'
        mock.get(MOCK_URL + API_KEY + "&docketID=" + bad_docket,
                 json='The test yields a bad id pattern', status_code=400)

        with pytest.raises(reggov_api_doc_error.IncorrectIDPatternException):
            get_docket(API_KEY, NO_ID_URL + bad_docket)


def test_bad_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(MOCK_URL + 'INVALID' + "&docketID=" + DOCKET_ID,
                 json='The test yields a bad api key', status_code=403)

        with pytest.raises(reggov_api_doc_error.IncorrectApiKeyException):
            get_docket('INVALID', NO_ID_URL + DOCKET_ID)


def test_no_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(MOCK_URL + "&docketID=" + DOCKET_ID,
                 json='The test yields a bad api key', status_code=403)

        with pytest.raises(reggov_api_doc_error.IncorrectApiKeyException):
            get_docket('', NO_ID_URL + DOCKET_ID)


def test_maxed_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(MOCK_URL + API_KEY + "&docketID=" + DOCKET_ID,
                 json='The test yields a overused api key', status_code=429)

        with pytest.raises(reggov_api_doc_error.ExceedCallLimitException):
            get_docket(API_KEY, NO_ID_URL + DOCKET_ID)


def test_get_docket_data():
    with requests_mock.Mocker() as mock:
        mock.get(MOCK_URL + API_KEY + "&docketID=" + DOCKET_ID,
                 json={'test': 'The test is successful'})
        json_response = get_data_json(API_KEY, NO_ID_URL + DOCKET_ID)
        string_response = get_data_string(API_KEY, NO_ID_URL + DOCKET_ID)

        assert json_response == {'data': {'test': 'The test is successful'}}
        assert string_response == jformat(json_response)


def test_get_job_information():
    with requests_mock.Mocker() as mock:
        mock.get(MOCK_URL + API_KEY + "&docketID=" + DOCKET_ID,
                 json={'test': 'The test is successful'})
        json_response = get_job_json(NO_ID_URL + DOCKET_ID)
        string_response = get_job_string(NO_ID_URL + DOCKET_ID)

        assert json_response == {'job':
                                 {'url': NO_ID_URL + DOCKET_ID,
                                  'job_type': 'docket'}}
        assert string_response == jformat(json_response)


def test_unsplitable_url():
    with requests_mock.Mocker() as mock:
        mock.get(MOCK_URL + API_KEY + "&docketID=" + DOCKET_ID,
                 json='The test yields a bad id')

        with pytest.raises(IndexError):
            removed_split_key_url = NO_ID_URL.split("?")
            get_docket(API_KEY, removed_split_key_url[0] +
                       removed_split_key_url[1] + DOCKET_ID)


def test_bad_url():
    with requests_mock.Mocker() as mock:
        mock.get("https://api.data.gov:443/regulation/v3/" +
                 "docket.json?api_key=" + API_KEY +
                 "&docketID=" + DOCKET_ID,
                 json='The test yields a bad id', status_code=404)

        with pytest.raises(reggov_api_doc_error.BadDocIDException):
            get_docket(API_KEY,
                       "https://api.data.gov:443/regulation/v3/" +
                       "docket.json?&docketId=" + DOCKET_ID)
