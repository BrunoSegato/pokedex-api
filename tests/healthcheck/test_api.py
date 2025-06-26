from fastapi.testclient import TestClient

from pokedex.main import app

client = TestClient(app)


class TestHealthCheckAPI:

    def test_ping(self):
        response = client.get("/ping")
        expected = {"service_name": "pokedex-api", "version": "0.0.1"}
        assert response.status_code == 200
        assert response.json() == expected

    def test_healthcheck(self):
        response = client.get("/healthcheck")
        assert response.status_code == 200
