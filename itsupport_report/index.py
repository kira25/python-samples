import streamlit as st
import pandas as pd
import numpy as np
import time

st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")

# Write a dataframe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0))

# Use magic
st.write("Use magic commands:")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

df

# --FETCH DATA--##

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data[['lat', 'lon']]


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(20)

st.dataframe(data)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

# Draw charts and maps

st.write("Draw charts and maps")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.dataframe(map_data)

st.map(map_data)

##--Widgets--##

st.write("Add interactivity with widgets")

if st.sidebar.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    chart_data

option = st.sidebar.selectbox(
    'Which number do you like best?',
    df['first column'])

'You selected:', option

#Columns
left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

with st.echo():
    st.write("This is a echo")

with st.spinner("Wait for it"):
    time.sleep(5)
    st.success("!Done..")

##--SHOW PROGRESS--##

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'
