# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 15:47:01 2026

@author: THAMAGA
"""

import streamlit as st

# --------------------------------
# Page configuration
# --------------------------------
st.set_page_config(
    page_title="Gas Sensing Devices Store",
    page_icon="🧪",
    layout="wide"
)

# Background color
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f4f7fb;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------
# Header
# --------------------------------
st.title("🧪 Thamaga's Smart Gas Sensing Devices")
st.markdown(
    "### Advanced Gas Sensors for Industrial, Environmental, and Wearable Applications"
)

st.divider()

# --------------------------------
# Navigation
# --------------------------------
page = st.sidebar.radio(
    "Navigate",
    ["Home", "Products", "Wearable Sensors", "Technology", "Contact & Orders"]
)

# --------------------------------
# Home Page
# --------------------------------
if page == "Home":
    st.subheader("🚀 Why Our Gas Sensors?")
    st.markdown("""
- **High sensitivity & selectivity**
- **Room-temperature operation**
- **MXene & metal oxide heterostructures**
- **Low power consumption**
- **Portable & wearable-ready**
    """)

    st.info(
        "Our sensors are designed for real-time gas monitoring in healthcare, "
        "industrial safety, environmental sensing, and smart wearables."
    )

# --------------------------------
# Products Page
# --------------------------------
elif page == "Products":
    st.subheader("📦 Our Gas Sensing Devices")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🏭 Industrial Gas Sensor")
        st.image(
            "https://www.renkeer.com/wp-content/uploads/2021/06/fixed-gas-detector.jpg",
            use_container_width=True
        )
        st.markdown("""
- Detects VOCs, CO, NO₂, NH₃  
- High stability & long lifetime  
- Suitable for factories & labs  
**Price:** R7000
        """)
        st.button("Add to Cart – Industrial")

    with col2:
        st.markdown("### 🎒 Portable Gas Sensor")
        st.image(
            "https://tlmcorporation.co.za/wp-content/uploads/2015/11/GasAlertMicroClipXT.jpg",
            use_container_width=True
        )
        st.markdown("""
- Compact & battery-powered  
- Bluetooth & mobile app support  
- Ideal for field measurements  
**Price:** R3500
        """)
        st.button("Add to Cart – Portable")

    with col3:
        st.markdown("### ⌚ Wearable Gas Sensor")
        st.image(
            "https://ars.els-cdn.com/content/image/1-s2.0-S1385894724093902-gr1.jpg",
            use_container_width=True
        )
        st.markdown("""
- Lightweight & skin-compatible  
- Ultra-low power consumption  
- Continuous personal exposure monitoring  
**Price:** R500
        """)
        st.button("Add to Cart – Wearable")

# --------------------------------
# Wearable Sensors Page
# --------------------------------
elif page == "Wearable Sensors":
    st.subheader("⌚ Wearable & Portable Gas Sensors")

    st.markdown("""
Our wearable gas sensors integrate **MXene-based sensing layers**
with **flexible substrates** to enable real-time personal exposure monitoring.
    """)

    col4, col5 = st.columns(2)

    with col4:
        st.markdown("### Key Features")
        st.markdown("""
- Flexible & lightweight design  
- MXene thin-film sensing layer  
- Wireless data transmission  
- Compatible with smartwatches & badges  
        """)

    with col5:
        st.markdown("### Applications")
        st.markdown("""
- Occupational safety  
- Healthcare & breath analysis  
- Environmental exposure tracking  
- Smart clothing & IoT  
        """)


# --------------------------------
# Technology Page
# --------------------------------
elif page == "Technology":
    st.subheader("🔬 Our Sensing Technology")

    st.markdown("""
**Core Technologies**
- MXene-based chemiresistive sensing  
- Metal oxide/MXene heterojunctions  
- Schottky barrier modulation  
- Defect engineering for enhanced sensitivity  
    """)


    st.markdown("""
**Operating Principle**
Gas adsorption alters carrier concentration and interfacial barriers,
leading to measurable resistance changes even at room temperature.
    """)

    st.success("Our technology is scalable, low-cost, and industry-ready.")
    

# --------------------------------
# Contact & Orders Page
# --------------------------------
elif page == "Contact & Orders":
    st.subheader("📫 Contact & Orders")

    st.markdown("""
📧 **Email:** boiketlothamaga@gmail.com  
📞 **Phone:** +27 67 793 9766  
🌍 **Location:** Thamaga Research & Innovation Lab  
    """)

    st.markdown("### 📝 Request a Quote")

    with st.form("order_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        product = st.selectbox(
            "Select Product",
            ["Industrial Sensor", "Portable Sensor", "Wearable Sensor"]
        )
        quantity = st.number_input("Quantity", min_value=1, value=1)
        submit = st.form_submit_button("Submit Request")

        if submit:
            st.success(
                f"Thank you {name}! Your request for {quantity} "
                f"{product}(s) has been received."
            )

# --------------------------------
# Footer
# --------------------------------
st.divider()
st.caption("© 2026 Smart Gas Sensing Technologies | MXene-Based Sensors")

st.write("Protect yourself and loved ones.")
st.write("Get a sensing device NOW!")

st.divider()
st.caption("© 2026 Thamaga's Smart Gas Sensing Technologies | Wearable Sensors")