import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler
import numpy as np

# ---------------------------------------
# Page Configuration
# ---------------------------------------
st.set_page_config(
    page_title="Nassau Candy Shipping Dashboard",
    layout="wide"
)

st.title("🚚 Factory-to-Customer Shipping Route Efficiency Analysis")

# ---------------------------------------
# Load Dataset
# ---------------------------------------
df = pd.read_csv("Nassau Candy Distributor (2).csv")

# ---------------------------------------
# Date Conversion
# ---------------------------------------
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

# ---------------------------------------
# Lead Time
# ---------------------------------------
df['Lead_Time'] = (df['Ship Date'] - df['Order Date']).dt.days

df = df[df['Lead_Time'] >= 0]

# ---------------------------------------
# Product → Factory Mapping
# ---------------------------------------
factory_map = {

"Wonka Bar - Nutty Crunch Surprise":"Lot's O' Nuts",
"Wonka Bar - Fudge Mallows":"Lot's O' Nuts",
"Wonka Bar -Scrumdiddlyumptious":"Lot's O' Nuts",

"Wonka Bar - Milk Chocolate":"Wicked Choccy's",
"Wonka Bar - Triple Dazzle Caramel":"Wicked Choccy's",

"Laffy Taffy":"Sugar Shack",
"SweeTARTS":"Sugar Shack",
"Nerds":"Sugar Shack",
"Fun Dip":"Sugar Shack",
"Fizzy Lifting Drinks":"Sugar Shack",

"Everlasting Gobstopper":"Secret Factory",
"Lickable Wallpaper":"Secret Factory",
"Wonka Gum":"Secret Factory",

"Hair Toffee":"The Other Factory",
"Kazookles":"The Other Factory"
}

# ---------------------------------------
# Factory Column
# ---------------------------------------
df['Factory'] = df['Product Name'].map(factory_map)

# Route
df['Route'] = df['Factory'] + " → " + df['State/Province']

# ---------------------------------------
# Sidebar Filters
# ---------------------------------------
st.sidebar.header("Filters")

start_date, end_date = st.sidebar.date_input(
    "Date Range",
    [df['Order Date'].min(), df['Order Date'].max()]
)

selected_region = st.sidebar.multiselect(
    "Region",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

selected_state = st.sidebar.multiselect(
    "State",
    options=df['State/Province'].unique(),
    default=df['State/Province'].unique()
)

selected_shipmode = st.sidebar.multiselect(
    "Ship Mode",
    options=df['Ship Mode'].unique(),
    default=df['Ship Mode'].unique()
)

threshold = st.sidebar.slider(
    "Delay Threshold (Days)",
    min_value=1,
    max_value=15,
    value=5
)

# ---------------------------------------
# Filter Data
# ---------------------------------------
filtered_df = df[
    (df['Order Date'] >= pd.to_datetime(start_date)) &
    (df['Order Date'] <= pd.to_datetime(end_date)) &
    (df['Region'].isin(selected_region)) &
    (df['State/Province'].isin(selected_state)) &
    (df['Ship Mode'].isin(selected_shipmode))
]

# ---------------------------------------
# Sidebar Menu
# ---------------------------------------
menu = st.sidebar.radio(
    "Dashboard",
    [
        "Route Efficiency Overview",
        "Geographic Shipping Map",
        "Ship Mode Comparison",
        "Route Drill-Down"
    ]
)

# =====================================================
# 1. ROUTE EFFICIENCY OVERVIEW
# =====================================================
if menu == "Route Efficiency Overview":

    st.header("Route Efficiency Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average Lead Time",
            round(filtered_df['Lead_Time'].mean(),2)
        )

    with col2:
        st.metric(
            "Total Orders",
            filtered_df['Order ID'].nunique()
        )

    with col3:
        delay_freq = (filtered_df['Lead_Time'] > threshold).mean()*100

        st.metric(
            "Delay Frequency %",
            round(delay_freq,2)
        )

    # Route Analysis
    route_analysis = filtered_df.groupby('Route').agg(
        Total_Shipments=('Order ID','count'),
        Avg_Lead_Time=('Lead_Time','mean'),
        Lead_Time_STD=('Lead_Time','std')
    ).reset_index()

    st.subheader("Top 10 Efficient Routes")

    top10 = route_analysis.sort_values(
        by='Avg_Lead_Time'
    ).head(10)

    fig = px.bar(
        top10,
        x='Avg_Lead_Time',
        y='Route',
        orientation='h',
        color='Avg_Lead_Time'
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# 2. GEOGRAPHIC SHIPPING MAP
# =====================================================
elif menu == "Geographic Shipping Map":

    st.header("US Shipping Efficiency")

    state_analysis = filtered_df.groupby(
        'State/Province'
    )['Lead_Time'].mean().reset_index()

    fig = px.choropleth(
        state_analysis,
        locations='State/Province',
        locationmode='USA-states',
        color='Lead_Time',
        scope='usa',
        title='Average Lead Time by State'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Regional Bottlenecks")

    region_analysis = filtered_df.groupby(
        'Region'
    )['Lead_Time'].mean().reset_index()

    fig2 = px.bar(
        region_analysis,
        x='Region',
        y='Lead_Time',
        color='Lead_Time'
    )

    st.plotly_chart(fig2, use_container_width=True)

# =====================================================
# 3. SHIP MODE COMPARISON
# =====================================================
elif menu == "Ship Mode Comparison":

    st.header("Ship Mode Performance")

    ship_mode = filtered_df.groupby(
        'Ship Mode'
    ).agg(
        Avg_Lead_Time=('Lead_Time','mean'),
        Orders=('Order ID','count')
    ).reset_index()

    fig = px.bar(
        ship_mode,
        x='Ship Mode',
        y='Avg_Lead_Time',
        color='Ship Mode'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Lead Time Distribution")

    fig2 = px.box(
        filtered_df,
        x='Ship Mode',
        y='Lead_Time',
        color='Ship Mode'
    )

    st.plotly_chart(fig2, use_container_width=True)

# =====================================================
# 4. ROUTE DRILL-DOWN
# =====================================================
elif menu == "Route Drill-Down":

    st.header("Route Drill-Down")

    state = st.selectbox(
        "Select State",
        filtered_df['State/Province'].unique()
    )

    state_df = filtered_df[
        filtered_df['State/Province'] == state
    ]

    st.subheader("State-Level Insights")

    route_summary = state_df.groupby('Route').agg(
        Shipments=('Order ID','count'),
        Avg_Lead_Time=('Lead_Time','mean')
    ).reset_index()

    st.dataframe(route_summary)

    st.subheader("Order-Level Shipment Timeline")

    fig = px.timeline(
        state_df.head(100),
        x_start='Order Date',
        x_end='Ship Date',
        y='Order ID',
        color='Ship Mode'
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Order Details")

    st.dataframe(
        state_df[
            ['Order ID',
             'Order Date',
             'Ship Date',
             'Ship Mode',
             'Lead_Time',
             'Sales']
        ]
    )