from backend.__main__ import main


def test_main(mocker):
    mocker.patch("backend.__main__.run")
    ret = main()
    assert ret is None


def test_serve_react_app(test_client):
    with test_client as client:
        response = client.get("/index.html")
        assert response.status_code == 200
        assert "Vite + React + TS".encode() in response.content
