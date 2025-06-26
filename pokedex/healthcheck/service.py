from pokedex.healthcheck.schemas import PingModel


class HealthCheckService:

    CHECK_STATUS = True

    def ping(self):
        return PingModel(service_name="pokedex-api", version="0.0.1")

    def check_service(self):
        return self.CHECK_STATUS
