import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
st.subheader("AI Insights")
st.set_page_config(
    page_title="AI Store Intelligence",
    layout="wide"
)

st.title("🛍️ AI Store Intelligence Dashboard")

st.subheader("Store Performance Overview")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Revenue", "₹34,331")
col2.metric("Orders", "24")
col3.metric("Visitors", "301")
col4.metric("Conversion Rate", "35%")

st.divider()

st.divider()

left, right = st.columns([1, 2])

with left:

    st.markdown("## 💡 Business Insights")

    insights = [
        ("📍", "Makeup Zone recorded the highest visitor traffic (124 visitors)"),
        ("🏆", "Faces Canada generated the highest revenue (₹15,697)"),
        ("📈", "Conversion Rate is approximately 35%"),
        ("🕒", "Average customer dwell time in Makeup Zone is 15.36 sec"),
        ("🛍️", "Checkout traffic indicates strong purchase intent")
    ]

    for icon, text in insights:
        st.markdown(
            f"""
            <div style="
                padding:15px;
                margin-bottom:12px;
                border-radius:12px;
                border:1px solid #e5e7eb;
                background-color:#fafafa;
                box-shadow:0px 1px 3px rgba(0,0,0,0.05);
            ">
                <span style="font-size:20px;">{icon}</span>
                <span style="padding-left:10px;">{text}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

with right:

    st.markdown("## 🏬 Store Layout")

    st.image(
        "dashboard/current_layout.png",
        use_container_width=True
    )

st.divider()

st.subheader("Camera-Zone Mapping")

camera_mapping = pd.DataFrame({
    "Camera": ["CAM 1", "CAM 2", "CAM 3", "CAM 4", "CAM 5"],
    "Zone": [
        "Skincare",
        "Makeup",
        "Entrance",
        "Storage / Staff Area",
        "Checkout"
    ],
    "Visitors": [69, 124, 62, 3, 43]
})

styled = camera_mapping.style.hide(axis="index")\
    .set_properties(**{
        "text-align": "center"
    })

st.dataframe(styled, use_container_width=True)

# Top Brands
st.divider()

st.subheader("Top Brands")

brands = pd.DataFrame({
    "Brand": [
        "Faces Canada",
        "NY Bae",
        "COSRX",
        "Maybelline",
        "DERMDOC"
    ],
    "Revenue": [
        15697,
        2342,
        2070,
        1834,
        1620
    ]
})

fig = px.bar(
    brands,
    x="Brand",
    y="Revenue",
    color="Revenue",
    color_continuous_scale="Blues",
    text="Revenue"
)

fig.update_layout(height=450)

st.plotly_chart(fig, use_container_width=True)

# Top Categories + Zone Traffic
st.divider()

left, right = st.columns(2)

#Top Categories
with left:

    st.subheader("Top Categories")

    categories = pd.DataFrame({
        "Category": [
            "Lipstick",
            "Foundation",
            "Concealer",
            "Sheet Mask",
            "Toner"
        ],
        "Revenue": [
            5118,
            3685,
            2128,
            1485,
            1448
        ]
    })

    fig_cat = px.pie(
        categories,
        names="Category",
        values="Revenue",
        hole=0.55,
        color_discrete_sequence=px.colors.sequential.Blues_r
    )

    fig_cat.update_layout(height=450)

    st.plotly_chart(fig_cat, use_container_width=True)

#Zone Traffic
with right:

    st.subheader("Zone Traffic Analysis")

    zones = pd.DataFrame({
        "Zone": [
            "Makeup",
            "Skincare",
            "Entrance",
            "Checkout",
            "Storage"
        ],
        "Visitors": [
            124,
            69,
            62,
            43,
            3
        ]
    })

    fig_zone = px.pie(
        zones,
        names="Zone",
        values="Visitors",
        color="Visitors",
        color_discrete_sequence=px.colors.sequential.Reds_r
    )

    fig_zone.update_layout(height=450)

    st.plotly_chart(fig_zone, use_container_width=True)

# Customer Engagement
st.divider()

st.subheader("Customer Engagement")

c1, c2, c3 = st.columns(3)

c1.metric(
    "Average Dwell Time",
    "15.36 sec"
)

c2.metric(
    "Longest Stay",
    "125.89 sec"
)

c3.metric(
    "Valid Visitors",
    "40"
)