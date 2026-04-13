# Smart Irrigation & Fertilizer Dashboard

**Data Analytics & Visualisation Project**  
**Gautami Thakur | University of Galway, 2025**

An interactive Streamlit dashboard for exploring how fertilizer, soil nutrients, and temperature affect crop yield — built as a virtual what-if simulator for data-driven agronomy decisions.

🔗 **Live App:** [crop-yield-analytics-9.streamlit.app](https://crop-yield-analytics-9.streamlit.app/)

---

## Overview

This dashboard lets users simulate different agricultural input conditions and immediately see how crop yield responds. Using real-world agronomy data, it combines dynamic filtering, KPI cards, a correlation heatmap, and scatter plots into a single responsive interface — no field experiments needed.

---

## Repository Structure

```
├── streamlitapp.py       # Full Streamlit application
├── Crop_yield.csv        # Dataset: soil nutrients, fertilizer, temperature, yield
├── requirements.txt      # Python dependencies
└── README.md
```

---

## Features

### Sidebar Sliders — Real-Time Input Control
Five sliders let users set upper-bound thresholds for each input variable:

| Slider | Variable |
|---|---|
| Fertilizer | Total fertilizer applied |
| Temperature (°C) | Ambient temperature |
| Nitrogen (N) | Soil nitrogen level |
| Phosphorus (P) | Soil phosphorus level |
| Potassium (K) | Soil potassium level |

The entire dashboard — KPIs, heatmap, and all scatter plots — updates live as sliders are adjusted.

### KPI Cards
Three headline metrics computed on the filtered dataset:
- **Avg Yield** — mean crop yield under current input conditions
- **Avg Temp (°C)** — average temperature in the filtered subset
- **Max Fertilizer** — maximum fertilizer value in the filtered range

### Correlation Heatmap
A filtered heatmap showing pairwise correlations between all input variables and yield — helps identify which inputs have the strongest relationship with output at the selected conditions.

### Yield vs Inputs — Scatter Plots
Five scatter plots (one per input variable) displayed two per row, each showing how yield varies across the filtered data range. Fixed axis limits ensure visual consistency as filters change, making trends easy to compare.

### Raw Data Explorer
A collapsible expander shows the first rows of the filtered dataset for quick inspection.

### What-If Simulation
The slider interface acts as a virtual agronomic lab. Example queries:
- *"What happens to yield if I reduce nitrogen to 60?"*
- *"How does high temperature affect productivity?"*
- *"Is there a sweet spot for fertilizer that maximises yield?"*

---

## Dataset

`Crop_yield.csv` contains real-world agronomy records with the following columns:

| Column | Description |
|---|---|
| `Fertilizer` | Total fertilizer applied |
| `N` | Nitrogen level in soil |
| `P` | Phosphorus level in soil |
| `K` | Potassium level in soil |
| `temp` | Temperature in °C |
| `yeild` | Crop yield (target variable) |

---

## Tech Stack

- **Python** — Pandas for data handling
- **Streamlit** — Interactive web app framework
- **Seaborn / Matplotlib** — Correlation heatmap and scatter plots

---

## How to Run Locally

```bash
git clone https://github.com/gautami9t/crop-yield-analytics-streamlit.git
cd crop-yield-analytics-streamlit
pip install -r requirements.txt
streamlit run streamlitapp.py
```

Or visit the live deployment directly: [crop-yield-analytics-9.streamlit.app](https://crop-yield-analytics-9.streamlit.app/)

