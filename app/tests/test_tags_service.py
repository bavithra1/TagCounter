"""
This file consists of test cases for tags module
"""
def test_index(client):
    tag = {"name": "test", "value" : 1}
    response = client.get("/")
    assert (response.status_code == 200)

def test_tags_get(client, monkeypatch):
    tag = {"name": "test", "value" : 1}
    def mock_async_return(*args, **kwargs):
        future = asyncio.Future()
        future.set_result(tag)
        return future
    monkeypatch.setattr("services.tags_service.get_all_tags", mock_async_return)
    
    response = client.get("/tags")
    assert (response.status_code == 200)

@pytest.mark.asyncio   
def test_tags_post(client, monkeypatch):
    
    def mock_async_return(*args, **kwargs):
        future = asyncio.Future()
        future.set_result(None)
        return future
    monkeypatch.setattr("services.tags_service.create_tag", mock_async_return)
    monkeypatch.setattr("services.tags_service.get_tag", mock_async_return)
    tag = {"name": "test_", "value" : 1}
    response = client.post("/tags", json.dumps(tag))
    assert (response.status_code == 200  or response.status_code == 201)