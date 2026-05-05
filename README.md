# Wind Turbine CO2 Optimization Dashboard

## Project Overview

This project presents a data-driven wind energy analysis and decision-support dashboard.  
It uses real wind speed data to evaluate different wind turbine configurations, estimate energy production, calculate avoided CO2 emissions, and recommend the most suitable turbine design for the selected wind conditions.

The project combines energy engineering, data analysis, sustainability evaluation, and interactive visualization using Python and Streamlit.

---

## Project Goal

The main goal of this project is to answer the following engineering question:

**Which wind turbine configuration performs best under real wind conditions while maximizing clean energy production and CO2 emissions reduction?**

To answer this question, the project:
- analyzes real wind speed data,
- models turbine power output,
- compares multiple turbine designs,
- estimates environmental impact,
- and provides an automated recommendation.

---

## Problem Statement

Wind turbine performance strongly depends on local wind conditions.  
A turbine that performs well in one location may not be optimal in another.

Selecting an unsuitable turbine design can lead to:
- lower energy production,
- reduced capacity utilization,
- lower CO2 emissions savings,
- and weaker clean energy impact.

Therefore, a data-driven approach is needed to compare turbine configurations and support engineering decision-making.

---

## Proposed Solution

The solution is an interactive dashboard that allows users to:

- filter wind data by date range,
- visualize wind speed behavior over time,
- compare three turbine configurations,
- calculate total energy production,
- estimate avoided CO2 emissions,
- and receive an engineering recommendation based on performance.

The dashboard acts as a simplified decision-support tool for clean energy applications.

---

## Methodology

The project follows a structured workflow:

1. **Data Loading**  
   Real wind speed data is loaded into Python using Pandas.

2. **Data Cleaning**  
   The dataset is cleaned by:
   - selecting relevant columns,
   - renaming variables,
   - converting timestamps,
   - removing invalid wind speed values.

3. **Wind Data Analysis**  
   Wind speed trends are analyzed over time to understand variability and site behavior.

4. **Turbine Modeling**  
   A simplified turbine power curve is used to convert wind speed into power output.

5. **Turbine Comparison**  
   Three turbine designs are simulated and compared under the same wind conditions.

6. **Energy Production Calculation**  
   Total energy output is calculated for each turbine.

7. **CO2 Emissions Reduction**  
   Avoided CO2 emissions are estimated using a standard emissions factor.

8. **Engineering Recommendation**  
   A weighted decision score is used to recommend the best turbine.

---

## Turbine Modeling Concept

The turbine model is based on four main parameters:

- **Cut-in speed**: minimum wind speed required for the turbine to start producing power.
- **Rated speed**: wind speed at which the turbine reaches its rated power.
- **Cut-out speed**: wind speed at which the turbine stops for safety reasons.
- **Rated power**: maximum power output of the turbine.

The simplified logic is:

- If wind speed is below cut-in speed → power output is zero.
- If wind speed is between cut-in and rated speed → power increases gradually.
- If wind speed is between rated and cut-out speed → rated power is produced.
- If wind speed is above cut-out speed → turbine stops for protection.

---

## Turbine Configurations

Three turbine designs are compared:

### Turbine A
A standard turbine configuration with moderate cut-in speed and rated power.

### Turbine B
A turbine optimized for low-to-medium wind speeds.  
It has a lower cut-in speed and reaches useful power output earlier.

### Turbine C
A turbine with higher rated power but less favorable behavior at lower wind speeds.

---

## Decision Logic

The dashboard uses a weighted score to recommend the best turbine.

The score considers:

- **70% Total Energy Production**
- **30% CO2 Emissions Reduction**

This approach ensures that the recommendation is not based only on energy output, but also includes sustainability impact.

---

## Results

The analysis showed that **Turbine B** achieved the best overall performance.

It produced the highest total energy and achieved the highest CO2 emissions reduction among the three turbine configurations.

### Key Findings

- Turbine B performed best under the analyzed wind profile.
- Lower cut-in speed improved energy capture during low and moderate wind periods.
- Higher energy production directly increased avoided CO2 emissions.
- Turbine design has a significant influence on clean energy performance.

---

## Environmental Impact

The project estimates avoided CO2 emissions by comparing wind energy generation with fossil-fuel-based electricity generation.

This demonstrates how wind energy can contribute to:
- reducing greenhouse gas emissions,
- supporting clean energy transition,
- improving sustainability performance,
- and reducing dependence on fossil fuels.

---

## Engineering Insights

The results show that turbine selection should not be based only on rated power.  
A turbine with higher rated power is not always the best choice if the local wind profile does not allow it to operate efficiently.

For this dataset, Turbine B performed best because it was better suited to low-to-medium wind speeds.

This highlights the importance of matching turbine design to site-specific wind conditions.

---

## Model Limitations

This project uses a simplified engineering model.  
The following factors are not included:

- manufacturer-specific turbine power curves,
- wind direction,
- turbulence intensity,
- wake effects,
- air density variation,
- mechanical and electrical losses,
- maintenance downtime,
- grid constraints,
- real curtailment events,
- electricity prices,
- and hourly carbon intensity data.

These limitations should be considered when interpreting the results.

---

## Future Improvements

Future versions of this project could include:

- real turbine power curves from manufacturers,
- hourly carbon intensity data,
- electricity market prices,
- demand/load data,
- curtailment modeling,
- battery storage integration,
- wind forecasting,
- geographic site comparison,
- and optimization algorithms for turbine operation.

These improvements would make the project closer to a real industrial decision-support system.

---

## Dashboard Features

The Streamlit dashboard includes:

- interactive date filtering,
- wind speed visualization,
- turbine energy comparison,
- CO2 emissions reduction KPIs,
- bar chart comparison of turbine designs,
- automated engineering recommendation,
- model limitations,
- and future improvement suggestions.

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Streamlit
- Jupyter Notebook

---

## How to Run the Project


Install the required libraries:

```bash
pip install pandas matplotlib streamlit
````


##🚀 Live Demo

[Open the Dashboard] (https://wind-turbine-co2-dashboard.streamlit.app/)
