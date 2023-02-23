
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

NAVALUES = ['-,']
DATAFILE = "./data/ET_4.2_JAN_23.xlsx"
DATAFILE2 = "./data/ET_4.4_JAN_23.xlsx"
SHEET = "Month (Million m3)"
# data1 = pd.read_excel(DATAFILE, SHEET,index_col=0,header=6)

st.title('Natural Gas Production and Supply')

#@st.cache_data
def load_data(File: str,Sheet: str, head: int):
    data = pd.read_excel(File, Sheet, index_col=0, header=head)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

data = load_data(DATAFILE, SHEET, 6)

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


#st.write(f"value is {graph_columns}")

data2 = load_data(DATAFILE2, SHEET, 5)
col_drop =['Langeled to Easington','Via FLAGS to St Fergus','Frigg / Vesterled to St Fergus ','SAGE to St Fergus','CATS  to Teesside']

data2 = data2.drop(col_drop,axis='columns')

# extract column for slider
graph_range2 = data2.index.to_list()
graph_columns2 = data2.columns.to_list()




# create slider with index as range
slider_filter = st.select_slider("Date", options=graph_range2,value=(graph_range2[0]))
filtered_data2 = data2.loc[slider_filter]
col_drop2 =['Total pipeline','Total LNG','Total Imports']

filtered_data2 = filtered_data2.drop(col_drop2,axis='index')

filt_np = filtered_data2.to_numpy()

lat_lon_data = {"index":filtered_data2.index.to_list(), "lat":[51.331348,52.05109,61.1529386,28.0000272,-11.8775768,-24.7761086,50.6402809,4.6125522,-31.7613365,19.0974031,26.2540493,1.613172,46.603354,52.2434979,9.6000359,61.1529386,61.1529386,-6.8699697,25.3336984,64.6863136,39.3260685,10.7466905,39.7837304,16.3471243],"lon":[3.20684,5.63178,8.7876653,2.9999825,17.5691241,134.755,4.6667145,13.1535811,-71.3187697,-70.3028026,29.2675469,10.5170357,1.8883335,5.6343227,7.9999721,8.7876653,8.7876653,-75.0458515,51.2295295,97.7453061,-4.8379791,-61.0840075,-100.445882,47.8915271]}

df_lat_lon = pd.DataFrame(lat_lon_data)
df_lat_lon.set_index('index')
df_lat_lon["values"]= filt_np
#df_lat_lon.append(filtered_data2.,ignore_index=True)

#test = pd.concat([filtered_data2,df_lat_lon],ignore_index=True)

# test = pd.concat([filtered_data2,df_lat_lon],
# axis=1, sort=False)


x2 = st.checkbox('Show map',key='123k4')
if x2:
    #filtered_data2.loc[-1]= lat_lon_data["lat"]
    st.pydeck_chart(pdk.Deck(
        map_style=None,  #matches streamlit theme
        initial_view_state=pdk.ViewState(
            latitude=56.376,
            longitude=24,
            zoom=2.5,
            #max_zoom=4,        
            pitch=30,
        ),
        layers=[
            pdk.Layer(
                'HeatmapLayer',
                data=df_lat_lon,
                get_position='[lon, lat]',
                get_color='[255,0,0]',
                get_radius=10000,
                aggregation='COUNT',
                get_weight='values',
                pickable=True
            ),
        ],
    ))


x1 = st.checkbox('Show raw data',key='1234')
if x1:
    st.subheader('Raw data')
    st.write(df_lat_lon)
