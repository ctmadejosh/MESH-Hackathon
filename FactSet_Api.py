import requests
import json
import streamlit as st

st.title("FactSet Company Profile Lookup")

# User input for ticker
ticker = st.text_input("Enter Ticker Symbol", value="AAPL")

if ticker:
    url = f'https://api.factset.com/report/overview/v1/profile?id={ticker}'

    headers = {
        "X-Lima-Created": "1716472735",
        "X-Lima-Expiration": "1716501535",
        "X-Lima-Original-Serial": "FDS",
        "X-Lima-Original-Username": "TARTURI",
        "X-Lima-Serial": "FDS",
        "X-Lima-Username": "TARTURI",
        "X-Lima-Userstate": "INTERNAL",
        "X-Lima-Usertype": "EMPLOYEE",
        "X-Limasig-Dsa1024": "MC0CFENfQWmjCwmk6eCRFVbEV/j+YulpAhUAjBq3VAIQObBVn6Km4X+FuzC1pO4=",
        "X-Datadirect-Auth-Token": "tdchc80CzV2OtGONQKwF6lrdu3g7FJT0IzLHCGvCImYWrDwtnLaO9KxxVaGDOfaq"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        st.subheader(f"Profile Data for {ticker.upper()}")
        st.json(data)
    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP error: {e}")
    except Exception as e:
        st.error(f"Error: {e}")
