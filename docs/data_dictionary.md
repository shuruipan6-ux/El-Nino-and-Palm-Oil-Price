# Preliminary data dictionary

This dictionary records required variables before collection begins. Availability and exact definitions must be confirmed in the feasibility notebook.

| Field | Module | Frequency | Definition | Availability timing | Status |
|---|---|---:|---|---|---|
| `reference_month` | key | monthly | Economic month represented by the observation | n/a | required |
| `forecast_origin_date` | key | monthly | Date on which a historical forecast is made | n/a | required |
| `oni` | weather | monthly | Oceanic Niño Index or selected official ENSO measure | to verify | candidate |
| `oni_change_3m` | weather | monthly | Three-month change in the selected ENSO measure | derived after release | candidate |
| `strong_enso_flag` | weather | monthly | Indicator based on a pre-declared strong-event threshold | derived after release | candidate |
| `mpob_production` | fundamentals | monthly | Malaysian palm oil production | release date required | candidate |
| `mpob_stocks` | fundamentals | monthly | Malaysian palm oil stocks | release date required | candidate |
| `mpob_exports` | fundamentals | monthly | Malaysian palm oil exports | release date required | candidate |
| `production_seasonal_z` | fundamentals | monthly | Production deviation from normal seasonal pattern | derived after release | candidate |
| `stocks_seasonal_z` | fundamentals | monthly | Stock deviation from normal seasonal pattern | derived after release | candidate |
| `palm_oil_price` | pricing | monthly | Consistent monthly palm oil price series | release convention required | candidate |
| `return_1m` | target | monthly | One-month log return | known after target month | required |
| `return_3m` | target | monthly | Three-month log return | known after target horizon | secondary |
| `continuation_label_3m` | target | monthly | Pre-declared continuation/reversal outcome | known after target horizon | secondary |

## Audit fields required for every source

- source URL and provider;
- download date;
- license or redistribution rule;
- native frequency and unit;
- first and last observation;
- missing values and revisions;
- publication schedule and usable lag;
- transformation applied by this project.

