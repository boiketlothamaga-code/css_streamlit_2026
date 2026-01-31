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
st.title("🧪 Gas Sensors & MXene Research Profile")

st.markdown("""
**Research Focus:**  
MXene-based gas sensors, metal oxide heterostructures, defect engineering, and surface/interface physics.
""")

st.divider()

# -------------------------------
# Profile section
# -------------------------------
col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/3/3a/Graphene_structure.svg",
        caption="2D Materials Concept",
        use_container_width=True
    )

with col2:
    st.subheader("👩🏽‍🔬 About Me")
    st.write("""
I am a researcher working in the field of **gas sensing and low-dimensional materials**, 
with a strong emphasis on **MXenes (Ti₃C₂Tₓ)** and **metal oxide–MXene heterostructures** 
for room-temperature gas sensing.

My research explores **charge transport mechanisms**, **Schottky barriers**, 
**defect engineering**, and **surface chemistry** to enhance sensitivity, selectivity, 
and stability of gas sensors.
    """)
