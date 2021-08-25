import streamlit as st


# Accessing a secret
st.write(st.secrets["tableau"]["token_name"])

if st.checkbox('Show exception'):
    st.session_state.username
