def test_liveness(test_client):
    with test_client as client:
        response = client.get("/v1/health-check/liveness")
        assert response.status_code == 200
        assert response.json() == {"status": "success"}
