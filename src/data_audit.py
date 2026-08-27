"""Small, dependency-light helpers for the data feasibility stage."""

from __future__ import annotations

from dataclasses import dataclass, asdict
import json
from pathlib import Path
from typing import Iterable

import pandas as pd


@dataclass(frozen=True)
class SourceAudit:
    """One row in the data feasibility matrix."""

    source_id: str
    module: str
    provider: str
    url: str
    publication_lag_status: str
    redistribution_status: str
    local_file_found: bool


def load_source_registry(config_path: str | Path) -> dict:
    """Load the human-reviewed JSON source registry."""

    path = Path(config_path)
    with path.open("r", encoding="utf-8") as handle:
        registry = json.load(handle)
    if not isinstance(registry, dict) or "sources" not in registry:
        raise ValueError("Source registry must contain a top-level 'sources' list.")
    return registry


def build_feasibility_matrix(
    registry: dict,
    raw_directory: str | Path,
) -> pd.DataFrame:
    """Create a transparent availability matrix without downloading data."""

    raw_path = Path(raw_directory)
    local_names = {path.stem.lower() for path in raw_path.glob("*") if path.is_file()}
    rows: list[SourceAudit] = []

    for source in registry["sources"]:
        source_id = str(source["id"])
        rows.append(
            SourceAudit(
                source_id=source_id,
                module=str(source["module"]),
                provider=str(source["provider"]),
                url=str(source["url"]),
                publication_lag_status=str(source["publication_lag_status"]),
                redistribution_status=str(source["redistribution_status"]),
                local_file_found=source_id.lower() in local_names,
            )
        )

    return pd.DataFrame(asdict(row) for row in rows)


def missing_required_columns(frame: pd.DataFrame, required: Iterable[str]) -> list[str]:
    """Return required columns absent from a candidate dataset."""

    return sorted(set(required) - set(frame.columns))
