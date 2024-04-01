import streamlit as st
import snowflake.connector
from snowflake.snowpark.functions import col
import pandas as pd

st.title('👕 Zena\'s SweatSuit Catalog 👖')

#let's connect to snowflake

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")

pd_df = my_dataframe.to_pandas()

st.write(pd_df.loc[:,'COLOR_OR_STYLE'])

