import streamlit as st
import pandas as pd
import utils

st.set_page_config(page_title="Solar Data Dashboard", layout="wide")

st.title("Solar Data Insights Dashboard")

# Sidebar for country selection
countries = utils.get_countries()
country = st.sidebar.selectbox("Select Country", countries)
st.markdown(f"**Country:** {country}")

# Use Streamlit caching for data loading
@st.cache_data
def load_country_data_cached(country: str):
    return utils.load_country_data(country)

# Load data
df = load_country_data_cached(country)

# Identify GHI column
ghi_col = utils.get_ghi_column(df)

# Region column guess (improved for plotting)
region_col = None
for col in df.columns:
    if "region" in col.lower() or "site" in col.lower() or "location" in col.lower():
        region_col = col
        break
if not region_col:
    # If only Timestamp is available, extract Month for grouping
    if "timestamp" in df.columns[0].lower():
        region_col = "Month"
        df[region_col] = pd.to_datetime(df[df.columns[0]]).dt.strftime("%Y-%m")
    else:
        region_col = df.columns[0]  # fallback

# Add Month column for filtering if Timestamp exists
if "timestamp" in df.columns[0].lower():
    df["Month"] = pd.to_datetime(df[df.columns[0]]).dt.to_period("M").astype(str)

# Month range selector in sidebar
if "Month" in df.columns:
    months = sorted(df["Month"].unique())
    month_range = st.sidebar.select_slider(
        "Select Month Range",
        options=months,
        value=(months[0], months[-1])
    )
    # Filter by selected month range
    month_mask = (df["Month"] >= month_range[0]) & (df["Month"] <= month_range[1])
    df = df[month_mask]

# Limit number of regions for plotting (top 10 by count)
region_counts = df[region_col].value_counts().head(10).index
plot_df = df[df[region_col].isin(region_counts)]

# Boxplot of GHI
st.subheader(f"Boxplot of {ghi_col} by {region_col} (Top 10)")
import altair as alt
chart = alt.Chart(plot_df).mark_boxplot().encode(
    x=alt.X(region_col, title=region_col),
    y=alt.Y(ghi_col, title=ghi_col)
).properties(width=600)
st.altair_chart(chart, use_container_width=True)

# Top regions table
st.subheader(f"Top 5 {region_col}s by Average {ghi_col}")
top_regions = utils.get_top_regions(df, region_col, ghi_col, n=5)
st.dataframe(top_regions)

# Interactive slider for GHI filtering
st.sidebar.subheader("Filter by GHI")
ghi_min, ghi_max = float(df[ghi_col].min()), float(df[ghi_col].max())
ghi_range = st.sidebar.slider("GHI Range", min_value=ghi_min, max_value=ghi_max, value=(ghi_min, ghi_max))
filtered_df = df[(df[ghi_col] >= ghi_range[0]) & (df[ghi_col] <= ghi_range[1])]

st.subheader(f"Filtered Data ({ghi_col} in range {ghi_range[0]:.2f} - {ghi_range[1]:.2f})")
st.dataframe(filtered_df.head(100))
