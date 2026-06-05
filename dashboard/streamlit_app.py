"""Forecast visualization dashboard."""

import streamlit as st

st.title("Demand Forecasting")
st.line_chart({"actual": [], "forecast": []})
