import streamlit as st
import datetime as dt
import yfinance as yf


today = dt.date.today()
start_date = today - dt.timedelta(days=365)

def user_inputs():

    st.sidebar.header("User Inputs")
    symbols= ['AAPL', 'MSFT', 'XOM', 'C', 'JNJ', 'PFE', 'BAC', 'IBM']
    ticker = st.sidebar.selectbox('Ticker', symbols)

    start = st.sidebar.date_input('Start Date', start_date)
    end = st.sidebar.date_input('End Date', today)

    button = st.sidebar.button('Get Chart')
    return ticker, start, end, button


def get_data(ticker, start, end):
    symbol = yf.Ticker(ticker)
    data = yf.download(ticker, start, end)
    return data


def main():
    #Create Title for Graph
    st.write('# Stock Price Graph')

    #Create variables from user input boxes
    ticker, start, end, button = user_inputs()

    if button:
        #When button is pressed, uses user input to generate data
        data = get_data(ticker, start, end)
        st.line_chart(data.Close)  # can only do simple charts, no titles, customization etc.
        

main()
