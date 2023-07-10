import pandas as pd
import streamlit as st
import plotly.express as px
import builtins
import types




st.set_page_config(
    page_title = 'Analytics Dashboard',
    page_icon = '✅',
    layout = 'wide'
)

def function_hasher(func):
    return func.__name__

@st.cache_data(hash_funcs={types.FunctionType: function_hasher})

def load_data():
    df = pd.read_excel(
        io="Freddie_Mac.xlsx",
        engine="openpyxl",
        sheet_name="Full History",
        skiprows=2000,
        usecols="A:I",
        nrows=700,
    )
    return df

data = load_data()

data.columns = ['Week', 'US 30 YR FRM', '30yr fees and pts','US 15 yr ARM','15 yr fees and pts','US 5/1 ARM','5/1 ARM fees and pts','US 5/1 ARM margin','spread']


# Set the first column as the DataFrame index
data.set_index(data.columns[0], inplace=True)

st.write("Preview of Dataset")
#st.write(data.head())

#st.write("Description of Dataset")
#st.write(data.describe())


selected_columns = st.sidebar.multiselect("Select the columns to display", data.columns)
num_rows = st.sidebar.slider("Select the number of rows to display", 1, len(data), 1000)

st.dataframe(data[selected_columns].head(num_rows))

st.write("Distribution of columns")

st.line_chart(data[selected_columns])

df = pd.read_csv(
    "mortgage_rates.csv")
df.columns=['Mortgage news daily','Rate', 'Points', 'Change']
df = df.iloc[:6].drop(df.columns[2], axis=1)


# Custom CSS for the table
css = """
<style type=\"text/css\">
table {
color: #d8d8e0;
font-family: monospace;
border-width: 0px;
border-color: #d8d8e0;
border-collapse: collapse;
background-color: #121111;
}
table th {
border-width: 0px;
padding: 8px;
border-style: solid;
border-color: #d8d8e0;
background-color: #47484a;
}
table td {
border-width: 0px;
padding: 8px;
border-style: solid;
border-color: #d8d8e0;
background-color: #121111;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

st.title('Mortgage Rates Daily')

st.write("Preview of Dataset")
st.table(df)

