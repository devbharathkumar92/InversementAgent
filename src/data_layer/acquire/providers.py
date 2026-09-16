"""Topic 10 — provider boundary and the deterministic provider.

A provider is the only thing that *obtains* data. It is isolated behind
`ProviderAdapter` so that the acquisition service never depends on a
vendor, and so that Discovery/Analysis can never call a source directly.

`DeterministicProvider` is the only implementation registered today. It
derives its payload from the request alone: no network, no clock, no
randomness, no credentials. It exists so the boundary can be exercised
deterministically and so the paper runtime stays offline.
"""

from __future__ import annotations

import hashlib
from typing import Any, Protocol, runtime_checkable

from src.data_layer.acquire.contracts import AcquisitionRequest


class ProviderError(RuntimeError):
    """Raised when a provider cannot supply data (REQ 10.18)."""


@runtime_checkable
class ProviderAdapter(Protocol):
    """The contract every data provider must satisfy (REQ 10.12)."""

    name: str

    def fetch(self, request: AcquisitionRequest) -> dict[str, Any]:
        """Return a raw payload for `request`, or raise `ProviderError`."""
        ...


def _derive(seed: str, low: float, span: float) -> float:
    """Return a deterministic float in `[low, low + span)` from a seed."""
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    fraction = int(digest[:12], 16) / float(16**12)
    return round(low + fraction * span, 4)


class DeterministicProvider:
    """An offline provider producing reproducible synthetic payloads.

    It is **synthetic by construction** and is never presented as an
    approved production source (see `production_provider_status`).
    """

    name = "deterministic-synthetic"

    def __init__(
        self,
        *,
        error: str | None = None,
        timestamp: str | None = None,
        payload_override: dict[str, Any] | None = None,
    ) -> None:
        self.error = error
        self.timestamp = timestamp
        self.payload_override = payload_override or {}

    def fetch(self, request: AcquisitionRequest) -> dict[str, Any]:
        if self.error is not None:
            raise ProviderError(self.error)

        payload: dict[str, Any] = {
            "price": _derive(f"{request.asset}|price", 100.0, 400.0),
            "volume": _derive(f"{request.asset}|volume", 100_000.0, 900_000.0),
            "timestamp": self.timestamp if self.timestamp is not None else request.timestamp,
            "provenance": {"source_id": request.source_id, "fetched_at": request.timestamp},
        }
        payload.update(self.payload_override)
        return payload
