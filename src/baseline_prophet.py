"""Prophet baseline for MAPE comparison."""

from prophet import Prophet


def fit_prophet(df) -> Prophet:
    m = Prophet(yearly_seasonality=True, weekly_seasonality=True)
    m.fit(df.rename(columns={"date": "ds", "sales": "y"}))
    return m
