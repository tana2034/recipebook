import pytest

def test_all(client):
    res = client.get('/all')
    assert res.data[0].title == 'title'
    assert res.data[0].description == 'description'
    assert res.data[0].url == 'http://localhost:5000'

