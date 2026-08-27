# Research design

## Core question

When palm oil prices have already moved on stronger El Niño expectations but Malaysian production and stocks have not tightened, can a weather–fundamental divergence indicator forecast whether the move will continue or reverse over the next one to three months?

## Unit of analysis

Monthly Malaysian palm oil market observations. The exact start date will be set after the data feasibility audit.

## Primary target

Next-month palm oil log return:

```text
target_return_1m[t] = log(price[t+1] / price[t])
```

## Secondary target

A continuation/reversal label over a three-month horizon. The threshold and reference trend must be fixed using training data only. The label definition will be documented before model comparison.

## Predictor blocks

### Weather expectations

- ONI level and change;
- strong-event threshold indicators;
- event duration;
- lagged climate values available at the forecast date.

### Physical fundamentals

- seasonally adjusted MPOB production;
- seasonally adjusted inventory;
- exports and inventory draw/accumulation;
- release-date-aware changes and surprises.

### Market pricing

- lagged returns;
- trend deviation;
- realized volatility;
- optional momentum features defined without future data.

## Preliminary divergence concept

```text
divergence = weather_expectation_score
           + market_pricing_score
           - physical_tightening_score
```

This is a research concept, not a finalized formula. Feature scaling, sign conventions, and weights must be estimated or fixed using training data only.

## Baseline ladder

1. Naive historical mean or no-change benchmark.
2. Price-only linear/time-series benchmark.
3. Price plus weather model.
4. Price plus weather plus physical fundamentals.
5. Full model including the interpretable divergence measure.

## Validation

- expanding-window or rolling-window forecasts;
- explicit publication lags;
- no random train/test split for the main result;
- MAE/RMSE for return forecasts;
- directional accuracy for sign forecasts;
- regime analysis for strong/weak ENSO periods;
- ablation tests by predictor block;
- sensitivity to horizon, lag assumptions, and outlier treatment.

## Falsifiable outcomes

The project will be considered informative even if climate variables do not improve forecasts. Plausible conclusions include:

- ONI alone has little incremental forecasting value;
- physical confirmation matters more than the global climate index;
- divergence is only informative during strong climate regimes;
- public climate information is already reflected in price;
- the proposed signal is unstable and should not be used as a standalone investment rule.

## Non-goals

- predicting individual listed-company returns;
- covering sugar, rubber, grains, and A-share sectors in the same model;
- claiming causal effects from correlation alone;
- reporting live investment performance before a locked historical test is complete.

