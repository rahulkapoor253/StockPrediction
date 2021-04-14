# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import data_load
import fbforecast_data


st.title("Stock Prediction App")
stocks = ("GOOG", "AAPL", "FB", "AMZN", "TSLA", "NFLX")

selected_stocks = st.selectbox("Pick a stock to analyze", stocks)

n_years = st.slider("Years of prediction", 1, 4)
period = n_years * 365  # as periods should in prophet should be in num. of days

data_load_state = st.text("Loading data...")
data = data_load.load_data(selected_stocks)
data_load_state.text("Loading done!")

st.subheader("Raw Stock Data")
st.write(data.tail())

data_load.plot_raw_data(data)

# Stock Forecasting
fbforecast_data.forecast_data(data, period)
