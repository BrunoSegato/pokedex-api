import logging

from pokedex.common.context.manager import get_context


class RequestIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        request_id = get_context("request_id")
        record.request_id = request_id if request_id else "-"
        return True
