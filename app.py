import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly .express as px 
st.set_page_config(
    page_title="Wind Turbine CO2 Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.markdown("""
# 🌍 Wind Turbine CO2 Optimization Dashboard
### Data-driven turbine comparison for clean energy and emissions reduction
""")

st.write("""
This dashboard analyzes wind speed data to compare turbine designs, estimate energy production,
calculate avoided CO2 emissions, and support engineering decision-making for renewable energy systems.
""")

st.markdown("---")

# Load data
df = pd.read_csv("processed_wind_turbine_results.csv")

# Clean columns
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(" ", "_")

# Convert timestamp
if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.set_index("timestamp")

# Sidebar filters
st.sidebar.header("Filters")

start_date = st.sidebar.date_input("Start Date", df.index.min().date())
end_date = st.sidebar.date_input("End Date", df.index.max().date())

filtered_df = df.loc[pd.to_datetime(start_date):pd.to_datetime(end_date)]

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📄 Dataset",
    "🌬️ Wind Analysis",
    "⚙️ Turbine Performance",
    "🌱 Sustainability & Decision"
])

with tab1:
    st.header("Dataset Preview")
    st.dataframe(filtered_df.head())
    st.write("Dataset shape:", filtered_df.shape)

with tab2:
    st.header("Wind Speed Over Time")

    fig = px.line(
    filtered_df,
    x=filtered_df.index,
    y="wind_speed_m_s",
    title="Wind Speed Over Time"
)

st.plotly_chart(fig, use_container_width=True)

# Turbine model
def turbine_power(v, cut_in, rated_speed, cut_out, rated_power):
    if v < cut_in:
        return 0
    elif v < rated_speed:
        return (v - cut_in) / (rated_speed - cut_in) * rated_power
    elif v <= cut_out:
        return rated_power
    else:
        return 0

# Create turbine power columns
filtered_df["power_A_kw"] = filtered_df["wind_speed_m_s"].apply(
    lambda v: turbine_power(v, cut_in=3, rated_speed=12, cut_out=25, rated_power=1000)
)

filtered_df["power_B_kw"] = filtered_df["wind_speed_m_s"].apply(
    lambda v: turbine_power(v, cut_in=2.5, rated_speed=10, cut_out=25, rated_power=1200)
)

filtered_df["power_C_kw"] = filtered_df["wind_speed_m_s"].apply(
    lambda v: turbine_power(v, cut_in=3.5, rated_speed=11, cut_out=25, rated_power=900)
)

# Energy calculations
total_A = filtered_df["power_A_kw"].sum()
total_B = filtered_df["power_B_kw"].sum()
total_C = filtered_df["power_C_kw"].sum()

co2_factor = 0.4
co2_A = total_A * co2_factor
co2_B = total_B * co2_factor
co2_C = total_C * co2_factor

energy_data = pd.DataFrame({
    "Turbine": ["A", "B", "C"],
    "Total Energy (kWh)": [total_A, total_B, total_C],
    "CO2 Saved (kg)": [co2_A, co2_B, co2_C]
})

st.sidebar.markdown("---")
st.sidebar.header("Decision Weights")

energy_weight = st.sidebar.slider(
    "Energy Production Weight",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)

co2_weight = 1 - energy_weight

st.sidebar.write(f"CO2 Reduction Weight: {co2_weight:.1f}")

energy_data["Score"] = (
    energy_data["Total Energy (kWh)"] * energy_weight +
    energy_data["CO2 Saved (kg)"] * co2_weight
)

best_turbine = energy_data.loc[
    energy_data["Score"].idxmax(),
    "Turbine"
]

with tab3:
    st.markdown("## ⚙️ Turbine Performance Analysis")

    st.markdown("### 🔋 Energy Production")

    col1, col2, col3 = st.columns(3)
    col1.metric("Turbine A", f"{total_A:,.0f} kWh")
    col2.metric("Turbine B", f"{total_B:,.0f} kWh")
    col3.metric("Turbine C", f"{total_C:,.0f} kWh")

    st.markdown("---")

    st.markdown("### 📊 Energy Comparison")

    st.dataframe(energy_data)
fig = px.bar(
    energy_data,
    x="Turbine",
    y="Total Energy (kWh)",
    color="Turbine",
    title="Energy Comparison Between Turbines"
)

st.plotly_chart(fig, use_container_width=True)
    

with tab4:
    st.header("Sustainability & Decision")

    st.subheader("CO2 Reduction")

    col4, col5, col6 = st.columns(3)
    col4.metric("CO2 Saved A", f"{co2_A:,.0f} kg")
    col5.metric("CO2 Saved B", f"{co2_B:,.0f} kg")
    col6.metric("CO2 Saved C", f"{co2_C:,.0f} kg")

    st.markdown("---")

    st.markdown("## 🧠 Engineering Decision")

    st.markdown("### ⚖️ Multi-Criteria Optimization")

    c1, c2 = st.columns(2)
    c1.metric("Total Energy (kWh)", f"{energy_data['Total Energy (kWh)'].sum():,.0f}")
    c2.metric("Total CO2 Saved (kg)", f"{energy_data['CO2 Saved (kg)'].sum():,.0f}")

    st.markdown("---")

    st.markdown("### 🏆 Optimal Turbine Selection")

    st.success(f"""
The recommended turbine is **{best_turbine}**.

This decision is based on a weighted optimization approach combining:
- Energy production (70%)
- CO2 emissions reduction (30%)

This turbine provides the best balance between performance and environmental impact.
""")

    st.markdown("---")

    st.markdown("### 📌 Engineering Insight")

    st.info("""
The selected turbine demonstrates superior performance under the given wind conditions.
This indicates strong alignment between turbine design and wind speed distribution,
leading to higher efficiency and sustainability impact.
""")

    st.markdown("---")

    st.markdown("## ⚠️ Model Limitations")

    st.warning("""
This model is based on simplified assumptions and may not fully represent real-world wind turbine performance.

Key limitations include:
- Use of a simplified turbine power curve
- Assumption of constant turbine availability
- No consideration of wake effects between turbines
- No inclusion of maintenance downtime
- Fixed air density without temperature or altitude variation

These factors may influence actual energy production and should be considered in real engineering applications.
""")

    st.markdown("## 🚀 Future Improvements")

    st.write("""
Future versions could include wind forecasting, real turbine specifications,
economic analysis, battery storage integration, site-specific optimization,
and interactive geographic visualization.
""")

    st.markdown("## 📌 Project Value")

    st.write("""
This project demonstrates how data analysis and engineering modeling can support decision-making
in renewable energy systems. It highlights the importance of turbine selection based on real wind
conditions to maximize energy production and reduce CO2 emissions.
""")

    st.markdown("## 👤 Author")

    st.write("Developed as a data-driven renewable energy optimization project.")

