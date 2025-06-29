from unittest.mock import AsyncMock

import pytest

from pokedex.healthcheck.service import HealthCheckService


@pytest.fixture
def healthcheck_service(settings, mock_uow):
    yield HealthCheckService(db=mock_uow, settings=settings)


def fn_check_1():
    return True


def fn_check_2():
    return True


def fn_check_3():
    return False


class TestHealthCheckService:

    @pytest.mark.parametrize(
        "name,fn,expected_count",
        [
            ("service_1", fn_check_1, 3),
            ("service_1", fn_check_2, 3),
            ("service_2", fn_check_3, 3),
        ],
    )
    def test_check_idempotence_checks(
        self, healthcheck_service, name, fn, expected_count
    ):
        print(len(healthcheck_service._checks))
        healthcheck_service.add_checks(name, fn)
        assert len(healthcheck_service._checks) == expected_count

    def test_uptime_method_error(self, healthcheck_service, mocker):
        mocker.patch("builtins.open", side_effect=FileNotFoundError)
        result = healthcheck_service._uptime()
        assert result is None

    def test_uptime_method_success(self, healthcheck_service, mocker):
        mock_open = mocker.mock_open(read_data="3600.00 12345.67\n")
        mocker.patch("builtins.open", mock_open)
        result = healthcheck_service._uptime()
        assert result == "1h 0m 0s"

    async def test_is_health_success(self, healthcheck_service):
        result, status_code = await healthcheck_service.is_healthy()
        assert status_code == 200

    async def test_is_health_error(self, healthcheck_service):
        healthcheck_service._checks.clear()
        healthcheck_service.add_checks("service", fn_check_3)
        result, status_code = await healthcheck_service.is_healthy()
        assert status_code == 503

    @pytest.mark.asyncio
    async def test_check_db_should_return_false_on_exception(
        self, mocker, healthcheck_service
    ):
        healthcheck_service._repository = mocker.Mock()
        healthcheck_service._repository.check_connection = AsyncMock(
            side_effect=Exception("DB error")
        )

        result = await healthcheck_service.check_db()

        assert result is False
