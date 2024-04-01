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

pd_df = pd.DataFrame(my_catalog)

#st.write(pd_df)

color_list = pd_df[0].values.tolist()

# Let's put a pick list here so the user can pick the color

color_option = st.selectbox('Pick a sweatsuit color or style:', list(color_list))

# We'll build the image caption now, since we can

product_caption = 'Our warm, comfortable, ' + color_option + ' sweatsuit!'

st.write(product_caption)

