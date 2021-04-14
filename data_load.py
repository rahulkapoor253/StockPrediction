import streamlit as st
import yfinance as yf
from datetime import date
from plotly import graph_objs as go

START = '2014-01-01'
TODAY = date.today().isoformat()


@st.cache
def load_data(ticker):
    data_ret = yf.download(ticker, START, TODAY)
    # returned data format: Date as index, Open, High, Low, Close, Adj Close, Volume
    data_ret.reset_index(inplace=True)
    data_ret.Date = data_ret.Date.dt.strftime('%Y-%m-%d')
    return data_ret


def plot_raw_data(data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name="stock open"))
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name="stock close"))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
