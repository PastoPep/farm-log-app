import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Farm Logs").worksheet("Logs")  # change this to your sheet + tab name

st.title("Farm Log Entry")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
batch_id = st.text_input("Batch ID")
species = st.text_input("Species")
action = st.selectbox("Action", ["Fed", "Harvested", "Sampled", "Treated", "Moved"])
weight = st.text_input("Weight")
notes = st.text_area("Notes")

if st.button("Submit"):
    sheet.append_row([timestamp, batch_id, species, action, weight, notes])
    st.success("Submitted!")