import streamlit as st
from dashboard.app import run_dashboard

st.set_page_config(page_title="Store Intelligence System", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose Module", ["Dashboard"])

if page == "Dashboard":
    run_dashboard()
