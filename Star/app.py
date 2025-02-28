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
if st.button("Starbucks Overview",icon="☕️"):
    st.switch_page("pages/Starbucks.py")


'''# Welcome to Coffee Insights! ☕ '''
st.divider()

"""
Discover the stories behind your favorite Starbucks locations and menu trends with our intuitive app. Dive into rich data that brings the world of Starbucks to life:
- 🌎 Explore store performance and customer favorites across locations worldwide. 
- 📊 Analyze sales trends, seasonal drinks, and customer preferences. 
- 📝 Learn how Starbucks embraces sustainability and community impact.""" 
'''Start your journey with beautiful visualizations, interactive tools, and seamless navigation! 
Let’s brew something amazing together. Scroll below to explore! 🚀'''

coffee = pd.read_csv('data/cleaned_starbucks.csv')

''' ### Key Features: '''

col1, col2, col3 = st.columns(3, gap = 'large')

with col1:
    st.subheader('''Beverage Details''')
    st.markdown(''' 
    - Attributes: Beverage category, name, and preparation method (e.g., Short, Tall, Grande, Venti).
    - Purpose: Helps identify product categories and customization options.''')

with col2: 
    st.subheader('''Nutritional Information''')
    st.markdown('''
    - Attributes: Calories, total fat, sugars, protein, caffeine content, and other nutrients (e.g., vitamins, minerals).
    - Purpose: Enables analysis of health-related aspects of beverages.''')

with col3:
    st.subheader('''Caffeine Content''')
    st.markdown('''
    - Attributes: Caffeine in milligrams per serving.
    - Purpose: Tracks variations in caffeine levels across products and sizes.''')

left, right = st.columns(2)

left.subheader('''Missing Data''')
left.markdown('''
    - Attribute: Some missing values in the "Caffeine (mg)" column.
    - Purpose: Highlight gaps in data for analysis or cleaning needs.''')

right.subheader('''Data Types''')
right.markdown('''
    - Categorical: Beverage category, beverage name, preparation method.
    - Numerical: Calories, fats, sugars, protein, sodium, vitamins, caffeine content.''')


st.divider()

'''### Notable Aspects:
- Diversity of Products: Includes multiple beverage categories like Coffee, Espresso Drinks, and more.
- Customization Options: Tracks variations in preparation methods (e.g., size and milk choice).
- Health Focus: Nutritional breakdown allows for health-conscious analyses, like identifying high-calorie or high-caffeine drinks.
- Completeness: Most data fields are complete, except for some missing values in the caffeine content.'''

st.divider()

'''### Starbucks EDA'''
st.markdown('''Click the Starbucks Icon for more EDA Starbucks Overview''')






tab1, tab2, tab3, tab4 = st.tabs(["Bar Chart1", "Bar Chart2", "Scatter Plot","Pie Chart" ])

with tab1:
    st.header("Beverage prep vs Calories")
    st.bar_chart(coffee, x="Beverage_prep", y="Calories", stack=False)
with tab2:
    st.header("Beverage and it's Nutritional Value")
    st.bar_chart(
    coffee,
    x="Beverage",
    y=["Calories", "Caffeine (mg)"])
with tab3:
    st.header("Beverage vs Caffeine")
    st.scatter_chart(
    coffee,
    x="Beverage",
    y="Caffeine (mg)",
    color="Beverage_prep",
    size="Calories")
with tab4:
    st.subheader("Starbucks Beverage")
    fig = px.pie(
    coffee,
    names="Beverage",
    values="Calories",
    title="Beverage Calories Selection",
    color_discrete_sequence=px.colors.sequential.RdBu,
    )
    st.plotly_chart(fig)





#pr = coffee.profile_report()
#pr.to_file(Path("data/cleaned_starbucks.csv"))



