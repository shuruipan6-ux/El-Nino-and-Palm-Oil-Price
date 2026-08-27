# Palm Oil Weather Premium Forecast

Forecasting whether weather-driven palm oil price moves are more likely to continue or reverse when market expectations diverge from physical supply data.

> **Status:** Research design and data feasibility audit. No model results are claimed yet.

## Business question

Markets may price an expected El Niño supply shock before it appears in production and inventory data. When palm oil prices rise while physical supply remains loose, investors face a practical question:

**Will later fundamentals validate the weather premium, or will the premium unwind?**

This project turns that question into a historical forecasting exercise using information that would actually have been available at each forecast date.

## Project objective

Build and evaluate a transparent weather–fundamental divergence indicator for Malaysian palm oil, then test whether it improves one- to three-month price forecasts beyond a price-only baseline.

The project will forecast:

- next-month palm oil price direction or return;
- continuation versus material reversal over the next one to three months;
- whether predictive information comes from weather expectations, physical confirmation, or their divergence.

## Research design

The analysis has three information layers:

1. **Weather expectations:** ONI level, change, event strength, duration, and lag structure.
2. **Physical fundamentals:** seasonally adjusted MPOB production, inventory, and exports.
3. **Market pricing:** palm oil returns, trend deviation, and volatility.

A preliminary divergence signal will compare weather and price pressure with the degree of physical tightening. Its final formula will be selected using only training data and will remain interpretable.

## Validation standard

The main evidence will come from expanding-window or rolling-window historical forecasts. Every forecast must use only data published by that date.

The weather–fundamental model will be compared with:

- a naive or historical-mean benchmark;
- a price-only time-series model;
- a price plus weather model;
- a price, weather, fundamentals, and divergence model.

Evaluation will include forecast error, directional accuracy, performance by climate regime, and sensitivity to publication lags. A complex model will only be retained if it improves out-of-sample results consistently.

## Current data plan

| Data module | Candidate source | Initial variables | Current task |
|---|---|---|---|
| Climate | NOAA Physical Sciences Laboratory | ONI and related ENSO indices | Confirm downloadable history and publication timing |
| Physical supply | Malaysian Palm Oil Board (MPOB) | Production, stocks, exports | Build a continuous monthly table and verify release dates |
| Market price | World Bank Commodity Price Data | Monthly palm oil price | Confirm definition, currency, and timing |

See [`data/README.md`](data/README.md) and [`docs/data_dictionary.md`](docs/data_dictionary.md) for the audit fields.

## Repository structure

```text
.
├── config/              # Data-source registry and project settings
├── data/                # Documentation plus untracked raw/processed data
├── docs/                # Research design and data dictionary
├── notebooks/           # Ordered analysis notebooks
├── reports/figures/     # Final charts for the README and report
├── src/                 # Reusable data-audit and modeling code
├── tests/               # Lightweight automated checks
├── .gitignore
├── requirements.txt
└── README.md
```

## Reproduce the current scaffold

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
jupyter lab
```

Start with [`notebooks/00_data_feasibility.ipynb`](notebooks/00_data_feasibility.ipynb). It records what is required, what is currently available, and what must be verified before modeling begins.

## Research boundaries

- The project focuses on Malaysian palm oil, not a broad basket of agricultural assets.
- It does not directly forecast individual company share prices.
- It does not assume that El Niño always raises palm oil prices.
- Reported percentage moves or lag claims from secondary research are hypotheses until traced to primary sources and independently tested.
- Correlation will not be presented as certain causality.

## Origin and ownership

The research question was inspired by an internship discussion about divergence between market expectations and physical commodity data. The data engineering, indicator construction, forecasting design, code, and validation in this repository are intended to be independently completed and clearly documented.

