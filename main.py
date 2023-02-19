


import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


st.title('Watcha')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data        

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')

hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)


chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,  #matches streamlit theme
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))




data1 = pd.DataFrame([
    {
        'site': 'Big Ben',
        'attraction_type': 'Clock Tower',
        'lat': 51.5006958,
        'lng': -0.1266639
    }, 
    {
        'site': 'Kensington Palace',
        'attraction_type': 'Palace',
        'lat': 51.5046188,
        'lng': -0.1839472
    },
    {
        'attraction_type': 'Palace',
        'site': 'Buckingham Palace',
        'lat': 51.501364,
        'lng': -0.14189
    }])

color_lookup = pdk.data_utils.assign_random_colors(data1['attraction_type'])
# Assign a color based on attraction_type
data1['color'] = data1.apply(lambda row: color_lookup.get(row['attraction_type']), axis=1)



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
            'ScatterplotLayer',
            data=data1,
            get_position='[lng, lat]',
            get_color='[255,0,0]',
            get_radius=1000,
        ),
    ],
))


