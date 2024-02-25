from datetime import timedelta
import numpy as np

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

import os
from supabase import client

# SUPABASE_URL = st.secrets["connection.supabase.url"]
SUPABASE_URL = "https://kwztayzyjudbycuvvnlw.supabase.co"

# SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt3enRheXp5anVkYnljdXZ2bmx3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDgyNDg0MzAsImV4cCI6MjAyMzgyNDQzMH0.5vGAUJ0kwj4jxM1pG8yMbmGeyQKJeRWzNxWl8y1K1As"

# Initialize connection.
supabase = client.create_client(SUPABASE_URL, SUPABASE_KEY)

def run():
    st.set_page_config(
        page_title="Home",
        page_icon="👋",
    )

    st.title("Sing & Sign Class Booking! 👋")

if __name__ == "__main__":
    run()