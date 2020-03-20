import json
import pytest
from c20_server.upload_job import APP


@pytest.fixture(name='client')
def client_fixture():
    APP.config['TESTING'] = True
    return APP.test_client()


def test_get_job(client):
    response = client.get('/get_job')
    assert response.status_code == 200
    assert response.data == b'{"docketId":"CMS-2014-0115"}\n'


def test_return_result_success(client):
    json_data = {'title': u'foo'}
    result = client.post('/return_result', data=json.dumps(json_data),
                         content_type='application/json')
    assert result.status_code == 200


def test_return_result_empty_data(client):
    result = client.post('/return_result', data={})
    assert result.status_code == 400
