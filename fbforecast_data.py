import streamlit as st
from fbprophet import Prophet
from fbprophet.plot import plot_plotly


def forecast_data(data, period):
    df_train = data[["Date", "Close"]]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    forecast_data_load_state = st.text("Predicting Data...")

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)
    # forecast.ds = forecast.ds.dt.strftime('%Y-%m-%d')

    forecast_data_load_state.text("Done Predicting!")
    st.subheader("Forecast Data")
    # st.write(forecast.tail())

    fig = plot_plotly(m, forecast)
    st.plotly_chart(fig)

    st.subheader("Forecast Components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)
