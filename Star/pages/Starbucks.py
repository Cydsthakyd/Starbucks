
import streamlit as st
import streamlit_jupyter as stj
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from ydata_profiling import ProfileReport
from ydata_profiling.utils.cache import cache_file
from ydata_profiling.visualisation.plot import timeseries_heatmap
from pathlib import Path
import streamlit.components.v1 as components

if st.button("Home", icon="🏠"):
    st.switch_page("app.py")

coffee = pd.read_csv('data/cleaned_starbucks.csv')
path_to_html = "data/cleaned_starbucks.html" 

##with open(path_to_html,'r') as f: 
  ##  html_data = f.read()

## Show in webpage
st.header("Starbucks EDA Overview")

profile = ProfileReport(coffee, title="Starbucks EDA Overview", explorative=True)

# Generate the report HTML
report_html = profile.to_html()
st.components.v1.html(report_html, width=1000, height=750, scrolling=True)
