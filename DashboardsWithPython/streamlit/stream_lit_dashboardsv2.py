import pandas as pd
import streamlit as st
import plotly.express as px

# PD Config
path = "/Users/ivanildo_barauna/bitbucket_mycodes/python_learning/__databases/netflix_titles.csv"
df = pd.read_csv(path)


## ST Config
st.set_page_config(layout='wide'
                   ,page_title='NetFlix Analysis'
                   )
st.header('NetFlix Titles Dashboard')
st.divider()
selected_country =  st.sidebar.selectbox('Country Filter'
                    ,df["country"].unique()
                    )

df_filtered = df[
    df["country"] == selected_country
]


df_filtered
st.write(len(df_filtered))

## Metrics Start
col1, col2 = st.columns(2)
cht1 = px.bar(df, x='type', y='show_id')
col1.plotly_chart(cht1)

## Metrics Start
cht2 = px.bar(df, x='type', y='show_id')
col1.plotly_chart(cht1)





