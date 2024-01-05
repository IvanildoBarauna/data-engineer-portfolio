import pandas as pd
import streamlit as st
import plotly.express as px

## Streamlit configuration
st.set_page_config(page_title="Students Performance",layout='wide')
st.sidebar.title('Filters')


## DF manipulation
path = '/Users/ivanildo_barauna/bitbucket_mycodes/python_learning/__databases/StudentsPerformance.csv'
df = pd.read_csv(path)
gender = st.sidebar.selectbox("Gender", df['gender'].unique())
df_filtered = df[df['gender'] == gender]

## Math Score Analysis
metric_name = "math score"
st.header(metric_name.capitalize() + ' Analysis')
st.divider()
col1, col2, col3 =st.columns(3)
chart1 = px.bar(df_filtered
                , x="race/ethnicity"
                , y=metric_name
                , title=metric_name.capitalize() + ' by race'
                , color='lunch'
                )
col1.plotly_chart(chart1)

chart2 = px.bar(df_filtered
                , x=metric_name
                , y="parental level of education"
                , title=metric_name.capitalize() + ' by race'
                , color="lunch"
                , orientation='h'
                )
col2.plotly_chart(chart2)

chart3 = px.pie(df_filtered,
                values=metric_name,
                names='lunch',
                title=metric_name.capitalize() + ' by lunch'
                )
col3.plotly_chart(chart3)

## Reading Analysis
metric_name = "reading score"
st.header(metric_name.capitalize() + ' Analysis')
st.divider()
col4, col5, col6 =st.columns(3)

chart4 = px.bar(df_filtered
                , x="race/ethnicity"
                , y=metric_name
                , title=metric_name.capitalize() + ' by race'
                , color='lunch'
                )
col4.plotly_chart(chart4)

chart5 = px.pie(df_filtered
                ,values=metric_name
                ,names='lunch'
                ,title=metric_name.capitalize() + ' lunch'
                )
col5.plotly_chart(chart5)

chart6 = px.bar(df_filtered
                , x=metric_name
                , y="parental level of education"
                , title=metric_name.capitalize() + ' level and lunch'
                , color="lunch"
                , orientation='h'
                )
col6.plotly_chart(chart6)

## writing Analysis
metric_name = "writing score"
st.header(metric_name.capitalize() + ' Analysis')
st.divider()
col7, col8, col9 =st.columns(3)

chart7 = px.bar(df_filtered
                , x="race/ethnicity"
                , y=metric_name
                , title=metric_name.capitalize() + 'by race and lunch'
                , color='lunch'
                )
col7.plotly_chart(chart7)

chart8 = px.pie(df_filtered
                ,values=metric_name
                ,names='lunch'
                ,title=metric_name.capitalize() + ' by Lunch'
                )
col8.plotly_chart(chart8)

chart9 = px.bar(df_filtered
                , x=metric_name
                , y="parental level of education"
                , title=metric_name.capitalize() + ' by parental level and lunch'
                , color="lunch"
                , orientation='h'
                )
col9.plotly_chart(chart9)

st.header('Raw Data by Kaggle')
st.divider()
df