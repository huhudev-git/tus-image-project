
def test_index(client, app):
    # test that viewing the page renders without template errors
    assert client.get("/").status_code == 200
    assert client.post("/").status_code == 405
