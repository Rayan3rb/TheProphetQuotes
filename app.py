import streamlit as st
import pandas as pd
import certifi
import json
import base64
from io import BytesIO

# Your credentials and API key
api = "8e6f866115cbd7e1427a5c38074aca1b"

# Function to fetch data
def get_jsonparsed_data(url):
    try:
        from urllib.request import urlopen
    except ImportError:
        from urllib2 import urlopen

    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

# Function to make data downloadable
def get_table_download_link(df, filename, text):
    towrite = BytesIO()
    df.to_excel(towrite, index=False, engine='openpyxl')
    b64 = base64.b64encode(towrite.getvalue()).decode() 
    href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{filename}">{text}</a>'
    return href

# Streamlit interface
def main():
    st.title('Financial Statements Viewer')
    
    stock = st.text_input('Enter Company Ticker:', value='2222.SR').upper()

    if st.button("Fetch Data"):
        IS = pd.DataFrame((get_jsonparsed_data(f"https://financialmodelingprep.com/api/v3/income-statement/{stock}?apikey={api}"))).drop(columns=["date","fillingDate","acceptedDate","symbol","cik","link","finalLink"]).T.reset_index().fillna("")
        BS = pd.DataFrame((get_jsonparsed_data(f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{stock}?apikey={api}"))).drop(columns=["date","fillingDate","acceptedDate","symbol","cik","link","finalLink"]).T.reset_index().fillna("")
        CF = pd.DataFrame((get_jsonparsed_data(f"https://financialmodelingprep.com/api/v3/cash-flow-statement/{stock}?apikey={api}"))).drop(columns=["date","fillingDate","acceptedDate","symbol","cik","link","finalLink"]).T.reset_index().fillna("")

        st.subheader("Income Statement")
        st.write(IS)
        st.markdown(get_table_download_link(IS, f"{stock}_Income_Statement.xlsx", "Download Income Statement as Excel"), unsafe_allow_html=True)
        
        # Plotting the revenue chart
        st.subheader("Revenue Trend")
        st.line_chart(IS.set_index('index').loc['revenue'].iloc[1:].astype(float))

        st.subheader("Balance Sheet")
        st.write(BS)
        st.markdown(get_table_download_link(BS, f"{stock}_Balance_Sheet.xlsx", "Download Balance Sheet as Excel"), unsafe_allow_html=True)

        st.subheader("Cash Flow")
        st.write(CF)
        st.markdown(get_table_download_link(CF, f"{stock}_Cash_Flow.xlsx", "Download Cash Flow as Excel"), unsafe_allow_html=True)

if __name__ == '__main__':
    main()
