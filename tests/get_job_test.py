import pytest
from c20_server.get_job import APP


@pytest.fixture(name='client')
def client_fixture():
    APP.config['TESTING'] = True
    return APP.test_client()


def test_get_job(client):
    response = client.get('/get_job')
    assert response.status_code == 200
    assert response.data == b'{"docketId":"CMS-2014-0115"}\n'
