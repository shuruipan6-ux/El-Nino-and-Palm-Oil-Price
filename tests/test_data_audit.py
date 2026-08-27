from pathlib import Path

import pandas as pd

from src.data_audit import (
    build_feasibility_matrix,
    load_source_registry,
    missing_required_columns,
)


ROOT = Path(__file__).resolve().parents[1]


def test_source_registry_contains_three_core_modules():
    registry = load_source_registry(ROOT / "config" / "data_sources.json")
    matrix = build_feasibility_matrix(registry, ROOT / "data" / "raw")

    assert set(matrix["module"]) == {
        "weather_expectations",
        "physical_fundamentals",
        "market_pricing",
    }
    assert matrix["publication_lag_status"].eq("to_verify").all()


def test_missing_required_columns_is_explicit():
    candidate = pd.DataFrame({"reference_month": ["2020-01"]})
    assert missing_required_columns(
        candidate,
        ["reference_month", "source_release_date", "value"],
    ) == ["source_release_date", "value"]
