"""Clean retail sales data and build lag features."""

import pandas as pd


def load_sales(path: str = "data/store_item_demand.csv") -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    df = df.sort_values(["store", "item", "date"])
    df["lag_7"] = df.groupby(["store", "item"])["sales"].shift(7)
    df["lag_28"] = df.groupby(["store", "item"])["sales"].shift(28)
    return df.dropna()
