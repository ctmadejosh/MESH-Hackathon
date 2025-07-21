import requests
import streamlit as st

# Define your API key here
API_KEY = 'fba8e286495646148f8bc67700283455'

def get_investment_news():
    # Define the endpoint URL
    url = 'https://newsapi.org/v2/everything'
    # Specify the query and number of returns
    parameters = {
        'q': 'stocks',  # or 'investment', 'finance', 'market', etc.
        'pageSize': 10,  # number of articles to return
        'apiKey': API_KEY,
        'language': 'en',  # retrieve English news
        'sortBy': 'publishedAt',  # sort by the latest articles
    }
    # Make the request
    response = requests.get(url, params=parameters)
    articles = response.json().get('articles', [])
    # Return the articles list
    return articles

def display_news():
    st.title('Latest Investment News')
    # Get news articles from the API
    news_items = get_investment_news()
    # Display each news item
    for item in news_items:
        st.subheader(item.get('title', 'No Title'))
        st.write('Published at: ' + item.get('publishedAt', ''))
        st.write(item.get('description', ''))
        st.write('[Read More](' + item.get('url', '') + ')', unsafe_allow_html=True)
        if item.get('urlToImage'):
            st.image(item['urlToImage'])
        st.write('---')

display_news()
