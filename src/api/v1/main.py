"""FastAPI application entry point (bootstrap scaffold).

Only infra endpoints exist. Feature endpoints are added by their topics.
"""

from fastapi import FastAPI

app = FastAPI(
    title="AI Investment Opportunity Agent API",
    version="0.1.0",
    description="API for the AI Investment Opportunity Agent. "
    "Feature endpoints are implemented incrementally per SRS topic.",
)


@app.get("/health")
def health() -> dict[str, str]:
    """Readiness/liveness probe for the API service."""
    return {"status": "ok", "service": "inversement-agent"}
