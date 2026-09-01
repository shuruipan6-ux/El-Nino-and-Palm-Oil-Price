# Data

This directory contains the monthly datasets used in the project.

## Structure

- `interim/`: a folder containing cleaned monthly datasets from public sources
- `palm_oil_monthly_panel/`: the merged monthly research panel
- `sources/`: source links and data coverage information

## Reproduction

Run `notebooks/01_build_monthly_data.ipynb` to download, clean, and export the datasets.

## Sources

The project uses public data from the Malaysian Palm Oil Board, World Bank, FRED, NOAA, CHIRPS, and ERA5-Land.

Detailed source links are recorded in `metadata/sources.csv`.
