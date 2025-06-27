import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from pokedex.common.context.manager import set_context


class ResponseHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.perf_counter()
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        set_context("request_id", request_id)

        response = await call_next(request)

        process_time = time.perf_counter() - start_time
        response.headers["X-Process-Time"] = f"{process_time:.4f}s"
        response.headers["X-Request-ID"] = request_id
        return response
