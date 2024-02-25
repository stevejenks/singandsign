from typing import Any


import streamlit as st

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

import os
from supabase import client

# SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_URL = "https://kwztayzyjudbycuvvnlw.supabase.co"

# SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt3enRheXp5anVkYnljdXZ2bmx3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDgyNDg0MzAsImV4cCI6MjAyMzgyNDQzMH0.5vGAUJ0kwj4jxM1pG8yMbmGeyQKJeRWzNxWl8y1K1As"

# Initialize connection.
supabase = client.create_client(SUPABASE_URL, SUPABASE_KEY)



def animation_demo() -> None:

    st.title("People Maintenance")

    option = st.sidebar.selectbox("Maintain People", ("Create", "Read", "Update", "Delete"),
                                   index=None, placeholder="Select operation...")
    
    if option=="Create":
        st.subheader("Create a Record")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email_address = st.text_input("Email Address")
        role = ("Customer")
        if st.button("Create"):     
            params=dict(first_name = first_name, last_name = last_name, role = role, email_address = email_address)
            supabase.table("PEOPLE").insert(params).execute()
            st.success("New record created sucessfully")
    elif option=="Read":
        st.subheader("Read Records")
        rows = supabase.table("PEOPLE").select("id, first_name, last_name, email_address, role").execute()
        st.dataframe(rows.data)
    elif option=="Update":
        st.subheader("Update a Record")
        id = st.number_input("ID",min_value=1, step=1)
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email_address = st.text_input("Email Address")
        role = "Student"

        if st.button("Update"):     
            params1=dict(id = id)
            params2=dict(first_name = first_name, last_name = last_name, role = role, email_address = email_address)
            supabase.table("PEOPLE").update(params2).eq("id", id).execute()
            st.success("Record sucessfully updated")

    elif option=="Delete":
        st.subheader("Delete a Record")
        id = st.number_input("ID",min_value=1, step=1)
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email_address = st.text_input("Email Address")
        role = "Student"

        if st.button("Delete Record"):     
            params1=dict(id = id)
            params2=dict(id = id, first_name = first_name, last_name = last_name, role = role, email_address = email_address)
            data, count = supabase.table('PEOPLE').delete().eq("id", id).execute()
            st.success("Record sucessfully updated")

animation_demo()