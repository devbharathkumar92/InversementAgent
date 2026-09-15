"""FastAPI application entry point (bootstrap scaffold).

Infra endpoints plus the bounded synthetic/paper runtime endpoint.
Feature endpoints are added by their topics.
"""

from fastapi import FastAPI

from src.api.v1.runtime import router as runtime_router

app = FastAPI(
    title="AI Investment Opportunity Agent API",
    version="0.1.0",
    description="API for the AI Investment Opportunity Agent. "
    "Feature endpoints are implemented incrementally per SRS topic.",
)

app.include_router(runtime_router)


@app.get("/health")
def health() -> dict[str, str]:
    """Readiness/liveness probe for the API service."""
    return {"status": "ok", "service": "inversement-agent"}
