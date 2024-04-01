import streamlit as st
import snowflake.connector
from snowflake.snowpark.functions import col
import pandas as pd

st.title('👕 Zena\'s SweatSuit Catalog 👖')

#let's connect to snowflake

cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE")

#change it to a pandas dataframe
pd_df = my_dataframe.to_pandas()

#now we will put a select box for users to pick a color
color_option = st.selectbox('Pick a sweatsuit color or style:', list(pd_df.loc[:, 'COLOR_OR_STYLE']))

#let's create a image caption and use it for the image of each product
product_caption = 'Our warm, comfortable, ' + color_option + ' sweatsuit!'

st.image(pd_df.loc[pd_df['COLOR_OR_STYLE'] == color_option, 'DIRECT_URL'].iloc[0], caption=product_caption, width = 400)

#now let's write the other details

st.write('Price: ', pd_df.loc[pd_df['COLOR_OR_STYLE'] == color_option, 'PRICE'].iloc[0])
st.write('Sizes Available: ',pd_df.loc[pd_df['COLOR_OR_STYLE'] == color_option, 'SIZE_LIST'].iloc[0])
st.write(pd_df.loc[pd_df['COLOR_OR_STYLE'] == color_option, 'UPSELL_PRODUCT_DESC'].iloc[0])


