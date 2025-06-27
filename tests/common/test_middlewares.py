import re

from fastapi.testclient import TestClient

from pokedex.main import app

client = TestClient(app)


class TestMiddlewares:

    def test_process_time_reader(self):
        response = client.get("/ping")
        assert response.status_code == 200
        assert "X-Process-Time" in response.headers

        value = response.headers["X-Process-Time"]
        assert re.match(r"^\d+\.\d{4}s$", value)
