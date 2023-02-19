
import streamlit as st
import pandas as pd
# import numpy as np
# import pydeck as pdk

NAVALUES = ['-,']
DATAFILE = ".\\data\\ET_4.2_JAN_23.xlsx"
SHEET = "Month (Million m3)"
# data1 = pd.read_excel(DATAFILE, SHEET,index_col=0,header=6)

st.title('Natural Gas Production and supply')

@st.cache_data
def load_data():
    data = pd.read_excel(DATAFILE, SHEET,index_col=0,header=6)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

data = load_data()
raw_data=data
# extract column for slider
graph_range = data.index.to_list()
graph_columns = data.columns.to_list()

# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")


# create slider with index as range
slider_range1, slider_range2 = st.select_slider("Date Range", options=graph_range,value=(graph_range[0],graph_range[-1]))

# not used - but this how to get the index values from the names
filter_range = data.index.get_indexer([slider_range1, slider_range2])

# create data subset of filtered range
filtered_data = data.loc[slider_range1:slider_range2]

st.bar_chart(filtered_data)

x = st.checkbox('Show raw data')
if x:
    st.subheader('Raw data')
    st.write(filtered_data)


st.write(f"value is {graph_columns}")
