import logging
import logging.config


def config_logging(settings):
    config: dict = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "standard": {
                "format": "[%(asctime)s] %(levelname)s in %(name)s: %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": settings.log_formatter,
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
