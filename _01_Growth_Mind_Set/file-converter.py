import streamlit as st
import pandas as pd
import os
import io as ByteIO

st.set_page_config(
    page_title="🗃File Converter",
    layout="wide"
)
st.title("📂File Converter & Data Sweeper")
st.write("This app is designed to convert CSV or EXCEL files and remove duplicate and format data.")

files = st.file_uploader("Upload CSV or EXCEL Files.", type=['csv', 'xlsx'], accept_multiple_files=True)

if files:
    for file in files:
        ext = file.name.split(".")[-1]
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

        st.header(f"{file.name} - preview")
        st.dataframe(df.head())

        if st.checkbox(f"Remove duplicate data from {file.name}"):
            df = df.drop_duplicates()
            st.success(f"Duplicate data removed from {file.name}")
            st.dataframe(df.head())


            if st.checkbox(f"Fill Missing Values - {file.name}"):
                df = file(df.select_dtypes(include=["number"]).mean(), inplace=True)
                st.success(f"Missing Values filled In - {file.name}")
                st.dataframe(df.head())

            selected_columns = st.multiselect(f"Select columns to format - {file.name}", df.columns , default=df.columns)
            df = df[selected_columns]
            st.dataframe(df.head())

            if st.checkbox(f"Show Cart - {file.name}") and not df.select_dtypes(include='number').empty:
                st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])


            format_choice = st.radio(f"Convert {file.name} to:", ["csv", "Excel"], key=file.name)

            if st.button(f"Download {file.name} as {format_choice}"):
                output = ByteIO.BytesIO()
                if format_choice == "csv":
                    df.to_csv(output, index= False)
                    mine = "text/csv"
                    new_file_name = file.name.replace(ext, "csv")
                
                else:
                    df.to_excel(output, index= False, engine='openpyxl')
                    mine = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    new_file_name = file.name.replace(ext, "xlsx")

                output.seek(0)
                # st.set_download_button(filename=new_file_name, data=output, mine= mine)
                st.download_button(label=f"Download File", data=output, file_name=new_file_name, mime=mine)
                st.success(f"{file.name} converted to {format_choice} successfully!")