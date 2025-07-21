import streamlit as st

st.title('User Profile')

if 'profile' in st.session_state:
    st.write(st.session_state['profile'])
else:
    st.info('No profile data found. Please use the main page to generate your profile.')
