"""Compare MAPE / RMSE across Prophet, LSTM, TFT."""


def mape(y_true, y_pred) -> float:
    import numpy as np

    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return float(np.mean(np.abs((y_true - y_pred) / np.maximum(y_true, 1))) * 100)
