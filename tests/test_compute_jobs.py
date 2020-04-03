
import pytest
import requests_mock

from c20_client.reggov_api_doc_error import (
    IncorrectApiKeyException,
    ExceedCallLimitException
)

from c20_client.compute_jobs import compute_jobs, get_number_of_docs
from c20_client.get_documents import get_response_from_api

URL = "https://api.data.gov:443/regulations/v3/documents.json?api_key="
API_KEY = "Valid"
START_DATE = "01/01/20"
END_DATE = "03/31/20"


def test_good_response_from_api():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json={"result": "The test is successful",
                       "totalNumRecords": 100})
        response = get_response_from_api(API_KEY, START_DATE, END_DATE)

        assert response == {"result": "The test is successful",
                            "totalNumRecords": 100}


def test_valid_jobs_list():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json={"result": "The test is successful",
                       "totalNumRecords": 2000})
        data = get_response_from_api(API_KEY, START_DATE, END_DATE)
        job_list = compute_jobs(data)

        assert job_list == [0, 1000]


def test_response_with_num_records():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json={"result": "The test is successful",
                       "totalNumRecords": 10})
        response = get_response_from_api(API_KEY, START_DATE, END_DATE)
        total_num_records = get_number_of_docs(response)

        assert total_num_records == 10


def test_bad_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(URL + 'INVALID',
                 json='The test yields a bad api key', status_code=403)

        with pytest.raises(IncorrectApiKeyException):
            get_response_from_api('INVALID', START_DATE, END_DATE)


def test_overused_api_key():
    with requests_mock.Mocker() as mock:
        mock.get(URL + API_KEY,
                 json='The test yields a overused api key', status_code=429)

        with pytest.raises(ExceedCallLimitException):
            get_response_from_api(API_KEY, START_DATE, END_DATE)
