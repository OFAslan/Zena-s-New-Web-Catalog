import streamlit as st
import snowflake.connector
import pandas as pd

st.title('👕 Zena\'s SweatSuit Catalog 👖')

#let's connect to snowflake

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a snowflake query and put it all in a var called my_catalog

my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

# put the data into a dataframe
df = my_catalog.to_pandas()

st.write(df)
