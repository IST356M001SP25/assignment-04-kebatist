'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
file = st.file_uploader("Upload a file:", type=["csv", "xlsx", "json"])

if file:
    file_type = pl.get_file_extension(file.name)
    df = pl.load_file(file, file_type)
    cols = pl.get_column_names(df)
    selected_cols = st.multiselect("Select columns to display", cols, default=cols)
    if st.checkbox("Filter data"):
        stcols = st.columns(3)
        text_cols = pl.get_columns_of_type(df, 'object')
        filter_col = stcols[0].selectbox("Select column to filter", text_cols)
        if filter_col:
            vals = pl.get_unique_values(df, filter_col)
            val = stcols[1].selectbox("Select value to filter On", vals)
            df_show = df[df[filter_col] == val][selected_cols]
    else:
        df_show = df[selected_cols]
    
    st.dataframe(df_show)
    st.dataframe(df_show.describe())
    
st.caption("The Universal data browser")
'''
# TODO Write code here to complete the unibrow.py
url = car_owner.csv # URL of the data
df = pd.read_csv(url) # Load the data into a DataFrame

cols = df.columns # Get the columns of the DataFrame
selected_cols = st.multiselect("Select columns", cols) # Select the columns to display

df = pl.select_columns(df, selected_cols) # Select the columns to display
fiter = st.selectbox("Select a column to filter", cols) # Select the column to filter
name = st.text_input("Enter a value to filter", "") # Enter the value to filter
df = pl.filter_data(df, fiter, name) # Filter the data

df = df[df[fiter] == name] # Filter the data
df = pl.describe_data(df) # Describe the data




df = pl.filter_data(df) # Filter the data
df = pl.sort_data(df) # Sort the data
df = pl.rename_columns(df) # Rename the columns
df = pl.reset_index(df) # Reset the index'

# Display the DataFrame
st.write(df)


The **UniBrow** application is a streamlit application which displays a data from a file. 

It consists of 3 inputs:

- upload a file in Excel (XLSX), Comma-Separared, with Header (CSV), or Row-Oriented Json (JSON) into a dataframe
- select which columns to display from the dataframe
- build a fiter on the dataframe based on a text column and one of the values in the column.

And 2 outputs:

- the dataframe with column / row filters applied.
- the describe of the dataframe (to see statistics for the numerical columns)

'''