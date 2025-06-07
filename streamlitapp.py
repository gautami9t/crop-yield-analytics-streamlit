# app.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Smart Irrigation Dashboard", layout="wide")

# Load dataset
file_path = "Crop_yield.csv"
df = pd.read_csv(file_path)

# 🌾 Title and Sidebar Description
st.title("🌾 Smart Irrigation & Fertilizer Dashboard")
st.sidebar.markdown("""
### 🧠 About this App
This tool lets you simulate different irrigation and nutrient inputs
to see how they affect crop yield. Use the sliders below to adjust inputs.
""")

# 🔍 Sidebar Filters
st.sidebar.header("🎚️ Filter Inputs")

fertilizer = st.sidebar.slider("Fertilizer", float(df.Fertilizer.min()), float(df.Fertilizer.max()), float(df.Fertilizer.max()))
temp = st.sidebar.slider("Temperature (°C)", float(df.temp.min()), float(df.temp.max()), float(df.temp.max()))
n = st.sidebar.slider("Nitrogen (N)", float(df.N.min()), float(df.N.max()), float(df.N.max()))
p = st.sidebar.slider("Phosphorus (P)", float(df.P.min()), float(df.P.max()), float(df.P.max()))
k = st.sidebar.slider("Potassium (K)", float(df.K.min()), float(df.K.max()), float(df.K.max()))

filtered_df = df[
    (df["Fertilizer"] <= fertilizer) &
    (df["temp"] <= temp) &
    (df["N"] <= n) &
    (df["P"] <= p) &
    (df["K"] <= k)
]

# 📂 Collapsible Raw Data Section
with st.expander("📂 View Raw Data"):
    st.write(filtered_df.head())

# 📈 KPI Cards
st.markdown("### 📈 Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Avg Yield", f"{filtered_df['yeild'].mean():.2f}")
col2.metric("Avg Temp (°C)", f"{filtered_df['temp'].mean():.1f}")
col3.metric("Max Fertilizer", f"{filtered_df['Fertilizer'].max():.1f}")

# 🔗 Correlation Heatmap
st.subheader("🔗 Correlation Heatmap (Filtered)")
fig = plt.figure(figsize=(4, 3))  # smaller size
ax = fig.add_subplot(1, 1, 1)
sns.heatmap(filtered_df.corr(), annot=True, cmap="YlGnBu", fmt=".2f", ax=ax,
            annot_kws={"size": 6}, cbar_kws={"shrink": 0.6})
ax.set_title("Correlation Heatmap", fontsize=9)
ax.tick_params(axis='x', labelsize=6)
ax.tick_params(axis='y', labelsize=6)
st.pyplot(fig)

# ⚖️ Yield vs Inputs (Filtered)
st.subheader("⚖️ Yield vs Inputs (Filtered)")

# Define full axis limits
x_limits = {
    'Fertilizer': (df['Fertilizer'].min() - 1, df['Fertilizer'].max() + 10),
    'N': (df['N'].min() - 1, df['N'].max() + 1),
    'P': (df['P'].min() - 1, df['P'].max() + 1),
    'K': (df['K'].min() - 1, df['K'].max() + 1),
    'temp': (df['temp'].min() - 1, df['temp'].max() + 1)
}
y_limit = (df['yeild'].min() - 5, df['yeild'].max() + 2.5)

# Two charts per row using columns
features = ['Fertilizer', 'N', 'P', 'K', 'temp']
for i in range(0, len(features), 2):
    cols = st.columns(2)
    for j, feature in enumerate(features[i:i+2]):
        with cols[j]:
            fig, ax = plt.subplots(figsize=(4, 3))  # compact size
            sns.scatterplot(
                x=filtered_df[feature], y=filtered_df['yeild'],
                ax=ax, s=15, alpha=0.4, color='seagreen', edgecolor='black'
            )

            ax.set_title(f'Yield vs {feature}', fontsize=9)
            ax.set_xlabel(feature, fontsize=8)
            ax.set_ylabel("Yield", fontsize=8)
            ax.set_xlim(x_limits[feature])
            ax.set_ylim(y_limit)
            ax.grid(True, linestyle='--', linewidth=0.5)
            st.pyplot(fig)

# 📜 Footer
st.markdown("---")
st.markdown("👩‍💻 Created by Gautami Thakur · University of Galway · June 2025")
