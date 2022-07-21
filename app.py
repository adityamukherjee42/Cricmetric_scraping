import pandas as pd
import streamlit as st
import requests
from bs4 import BeautifulSoup
import base64
import os
from zipfile import ZipFile


def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths


def write_excel(name):
    name = name.split("\r")[0]
    URL_Right_arm_Fast = "http://www.cricmetric.com/playerstats.py?player=" + str(name.split(" ")[0]) + '+' + str(
        name.split(" ")[
            1]) + '&role=all&format=all&groupby=year&start_date=2002-01-01&end_date=2022-07-20&opptype=Right-arm+Fast&start_over=0&end_over=9999'
    try:
        page = requests.get(URL_Right_arm_Fast)

        soup = BeautifulSoup(page.content, "html.parser")
        table_html = soup.find("div", {"id": "TWENTY20Content"})
        table = table_html.find_all('table')
        df_1 = pd.read_html(str(table))[0]
    except:
        df_1 = pd.DataFrame({})
    URL_Right_arm_Medium = 'http://www.cricmetric.com/playerstats.py?player=' + str(name.split(" ")[0]) + '+' + str(
        name.split(" ")[
            1]) + '&role=all&format=all&groupby=year&start_date=2002-01-01&end_date=2022-07-20&opptype=Right-arm+Medium&start_over=0&end_over=9999'
    try:
        page = requests.get(URL_Right_arm_Medium)

        soup = BeautifulSoup(page.content, "html.parser")
        table_html = soup.find("div", {"id": "TWENTY20Content"})
        table = table_html.find_all('table')
        df_2 = pd.read_html(str(table))[0]
    except:
        df_2 = pd.DataFrame({})
    URL_Right_arm_Slow = 'http://www.cricmetric.com/playerstats.py?player=' + str(name.split(" ")[0]) + '+' + str(
        name.split(" ")[
            1]) + '&role=all&format=all&groupby=year&start_date=2002-01-01&end_date=2022-07-20&opptype=Right-arm+Slow&start_over=0&end_over=9999'
    try:
        page = requests.get(URL_Right_arm_Slow)

        soup = BeautifulSoup(page.content, "html.parser")
        table_html = soup.find("div", {"id": "TWENTY20Content"})
        table = table_html.find_all('table')
        df_3 = pd.read_html(str(table))[0]
    except:
        df_3 = pd.DataFrame({})
    URL_Right_arm_Legbreak = 'http://www.cricmetric.com/playerstats.py?player=' + str(name.split(" ")[0]) + '+' + str(
        name.split(" ")[
            1]) + '&role=all&format=all&groupby=year&start_date=2002-01-01&end_date=2022-07-20&opptype=Right-arm+Legbreak&start_over=0&end_over=9999'
    try:
        page = requests.get(URL_Right_arm_Legbreak)

        soup = BeautifulSoup(page.content, "html.parser")
        table_html = soup.find("div", {"id": "TWENTY20Content"})
        table = table_html.find_all('table')
        df_4 = pd.read_html(str(table))[0]
    except:
        df_4 = pd.DataFrame({})
    URL_Right_arm_Offbreak = 'http://www.cricmetric.com/playerstats.py?player=' + str(name.split(" ")[0]) + '+' + str(
        name.split(" ")[
            1]) + '&role=all&format=all&groupby=year&start_date=2002-01-01&end_date=2022-07-20&opptype=Right-arm+Offbreak&start_over=0&end_over=9999'
    try:
        page = requests.get(URL_Right_arm_Offbreak)

        soup = BeautifulSoup(page.content, "html.parser")
        table_html = soup.find("div", {"id": "TWENTY20Content"})
        table = table_html.find_all('table')
        df_5 = pd.read_html(str(table))[0]
    except:
        df_5 = pd.DataFrame({})
    URL_Left_arm_Fast = 'http://www.cricmetric.com/playerstats.py?player=' + str(name.split(" ")[0]) + '+' + str(
        name.split(" ")[
            1]) + '&role=all&format=all&groupby=year&start_date=2002-01-01&end_date=2022-07-20&opptype=Left-arm+Fast&start_over=0&end_over=9999'
    try:
        page = requests.get(URL_Left_arm_Fast)

        soup = BeautifulSoup(page.content, "html.parser")
        table_html = soup.find("div", {"id": "TWENTY20Content"})
        table = table_html.find_all('table')
        df_6 = pd.read_html(str(table))[0]
    except:
        df_6 = pd.DataFrame({})
    URL_Left_arm_Medium = 'http://www.cricmetric.com/playerstats.py?player=' + str(name.split(" ")[0]) + '+' + str(
        name.split(" ")[
            1]) + '&role=all&format=all&groupby=year&start_date=2002-01-01&end_date=2022-07-20&opptype=Left-arm+Medium&start_over=0&end_over=9999'
    try:
        page = requests.get(URL_Left_arm_Medium)

        soup = BeautifulSoup(page.content, "html.parser")
        table_html = soup.find("div", {"id": "TWENTY20Content"})
        table = table_html.find_all('table')
        df_7 = pd.read_html(str(table))[0]
    except:
        df_7 = pd.DataFrame({})
    URL_Left_arm_Slow = 'http://www.cricmetric.com/playerstats.py?player=' + str(name.split(" ")[0]) + '+' + str(
        name.split(" ")[
            1]) + '&role=all&format=all&groupby=year&start_date=2002-01-01&end_date=2022-07-20&opptype=Left-arm+Slow&start_over=0&end_over=9999'
    try:
        page = requests.get(URL_Left_arm_Slow)

        soup = BeautifulSoup(page.content, "html.parser")
        table_html = soup.find("div", {"id": "TWENTY20Content"})
        table = table_html.find_all('table')
        df_8 = pd.read_html(str(table))[0]
    except:
        df_8 = pd.DataFrame({})
    URL_Left_arm_Chinaman = 'http://www.cricmetric.com/playerstats.py?player=' + str(name.split(" ")[0]) + '+' + str(
        name.split(" ")[
            1]) + '&role=all&format=all&groupby=year&start_date=2002-01-01&end_date=2022-07-20&opptype=Left-arm+Chinaman&start_over=0&end_over=9999'
    try:
        page = requests.get(URL_Left_arm_Chinaman)

        soup = BeautifulSoup(page.content, "html.parser")
        table_html = soup.find("div", {"id": "TWENTY20Content"})
        table = table_html.find_all('table')
        df_9 = pd.read_html(str(table))[0]
    except:
        df_9 = pd.DataFrame({})
    URL_Left_arm_Orthodox = 'http://www.cricmetric.com/playerstats.py?player=' + str(name.split(" ")[0]) + '+' + str(
        name.split(" ")[
            1]) + '&role=all&format=all&groupby=year&start_date=2002-01-01&end_date=2022-07-20&opptype=Left-arm+Orthodox&start_over=0&end_over=9999'
    try:
        page = requests.get(URL_Left_arm_Orthodox)

        soup = BeautifulSoup(page.content, "html.parser")
        table_html = soup.find("div", {"id": "TWENTY20Content"})
        table = table_html.find_all('table')
        df_10 = pd.read_html(str(table))[0]
    except:
        df_10 = pd.DataFrame({})
    with pd.ExcelWriter('zip_file'+'/'+name + '_batting record.xlsx') as writer:
        df_1.to_excel(writer, 'Right_arm_Fast')
        df_2.to_excel(writer, 'Right_arm_Medium')
        df_3.to_excel(writer, 'Right_arm_Slow')
        df_4.to_excel(writer, 'Right_arm_Legbreak')
        df_5.to_excel(writer, 'Right_arm_Offbreak')
        df_6.to_excel(writer, 'Left_arm_Fast')
        df_7.to_excel(writer, 'Left_arm_Medium')
        df_8.to_excel(writer, 'Left_arm_Slow')
        df_9.to_excel(writer, 'Left_arm_Chinaman')
        df_10.to_excel(writer, 'Left_arm_Orthodox')

def write_excel_bowling(name):
    name = name.split("\r")[0]
    URL_Right = "http://www.cricmetric.com/playerstats.py?player=" + str(name.split(" ")[0]) + '+' + str(
        name.split(" ")[
            1]) + '&role=all&format=all&groupby=year&start_date=2002-01-01&end_date=2022-07-20&opptype=Right&start_over=0&end_over=9999'
    try:
        page = requests.get(URL_Right)

        soup = BeautifulSoup(page.content, "html.parser")
        table_html = soup.find("div", {"id": "TWENTY20Content"})
        table = table_html.find_all('table')
        df_1 = pd.read_html(str(table))[0]
    except:
        df_1 = pd.DataFrame({})
    URL_Left = 'http://www.cricmetric.com/playerstats.py?player=' + str(name.split(" ")[0]) + '+' + str(
        name.split(" ")[
            1]) + '&role=all&format=all&groupby=year&start_date=2002-01-01&end_date=2022-07-20&opptype=Left&start_over=0&end_over=9999'
    try:
        page = requests.get(URL_Left)

        soup = BeautifulSoup(page.content, "html.parser")
        table_html = soup.find("div", {"id": "TWENTY20Content"})
        table = table_html.find_all('table')
        df_2 = pd.read_html(str(table))[0]
    except:
        df_2 = pd.DataFrame({})
    with pd.ExcelWriter('zip_file' + '/' + name + '_bowling record.xlsx') as writer:
        df_1.to_excel(writer, 'Right_hand_batsman')
        df_2.to_excel(writer, 'Left_hand_batsman')


df_p = pd.read_csv("batting_stats.csv")
option = list(set(df_p['PlayerName']))
text_or_name = st.selectbox('Select type of upload', ['Textual Upload', 'Name'])
if text_or_name == 'Name':
    name = st.selectbox('Select Name', option)
    button1 = st.button("Create Excel")
    if button1:
        write_excel(name)
else:

    uploaded_file = st.file_uploader("Add text file !")
    if uploaded_file:
        for line in uploaded_file:
            write_excel(line.decode().split("\n")[0])
            write_excel_bowling(line.decode().split("\n")[0])
            file_paths = get_all_file_paths('zip_file')
            with ZipFile('Archive.zip', 'w') as zip:
                # writing each file one by one
                for file in file_paths:
                    zip.write(file)

with open('Archive.zip', "rb") as f:
    bytes = f.read()
b64 = base64.b64encode(bytes).decode()
href = f'<a href="data:file/zip;base64,{b64}" download=\'Archive.zip\'>\
        Click to download\
    </a>'
st.markdown(href, unsafe_allow_html=True)
