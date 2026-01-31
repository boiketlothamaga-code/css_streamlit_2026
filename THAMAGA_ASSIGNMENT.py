# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 14:47:07 2026

@author: THAMAGA
"""

import streamlit as st

# -------------------------------
# Page configuration
# -------------------------------
st.set_page_config(
    page_title="Gas Sensors Research Profile",
    page_icon="🧪",
    layout="wide"
)

# -------------------------------
# Header section
# -------------------------------
st.title("🧪  Thamaga's Portable Gas Sensor Devices")

st.markdown("""
**Research Focus:**  

Gas sensors are a category of electronic devices that detect and measure the presence of various gases.
Gas sensor device detects and monitors hazardous gases—including toxic, flammable, and combustible""")

st.divider()

# -------------------------------
# Profile section
# -------------------------------
col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "https://www.istockphoto.com/illustrations/gas-detector",
        caption="Gas sensor device",
        use_container_width=True
    )

with col2:
    st.subheader("Wearable Gas Sensors")
    st.write("""
Get yourself a wearable gas sensor device for personal safety and health monitoring
    """)

st.write ("The wearable devices come as a patches, badges, and smart accessories, offer real-time, on-person monitoring of hazardous gases (e.g., \(CO\), \(H_{2}S\), \(NH_{3}\)) and volatile organic compounds (VOCs)")
st.image("https://www.researchgate.net/figure/Types-of-wearable-gas-sensors-Wearable-gas-sensors-Adapted-with-permission56_fig11_349088989")


st.write("Protect yourseld and loved ones.")
st.write("Get a sensing device NOW!")





