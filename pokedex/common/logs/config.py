import logging
import logging.config

from pokedex.common.logs.filters import RequestIdFilter


def config_logging(settings):
    fmt = "[%(asctime)s] %(levelname)s [%(request_id)s] in %(name)s: %(message)s"
    config: dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": fmt,
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "filters": {
            "request_id": {
                "()": RequestIdFilter,
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": settings.log_formatter,
                "filters": ["request_id"],
                "level": settings.log_level,
            },
        },
        "loggers": {
            "pokedex": {
                "handlers": ["console"],
                "level": settings.log_level,
                "propagate": False,
            },
            "uvicorn": {
                "handlers": ["console"],
                "level": settings.log_level,
                "propagate": False,
            },
        },
        "root": {
            "handlers": ["console"],
            "level": settings.log_level,
        },
    }
    logging.config.dictConfig(config)


def get_logger(name):
    return logging.getLogger(name)
