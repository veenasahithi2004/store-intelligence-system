import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dashboard.app import run_dashboard

st.set_page_config(page_title="Store Intelligence System", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose Module", ["dashboard"])

if page == "dashboard":
    run_dashboard()
