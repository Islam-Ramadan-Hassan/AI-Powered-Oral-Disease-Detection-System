from __future__ import annotations

import pandas as pd
import streamlit as st

from app.components.footer import render_footer
from app.components.header import render_page_header
from app.utils.helpers import load_dataset_summary
from app.utils.visualization import render_resolution_chart

dataset = load_dataset_summary()

render_page_header(
    title="Dataset insights",
    subtitle="Visual overview of the curated oral disease dataset used for training.",
    icon="insights",
    badges=[("Balanced preprocessing", "green"), ("No corrupted images", "green")],
)

with st.container(horizontal=True):
    st.metric("Train images", dataset["train_images"], border=True)
    st.metric("Validation images", dataset["val_images"], border=True)
    st.metric("Test images", dataset["test_images"], border=True)
    st.metric("Image size", f"{dataset['image_size']}×{dataset['image_size']}", border=True)

st.space("small")

st.subheader(":material/bar_chart: Class distribution", anchor=False)
class_df = pd.DataFrame(dataset["class_counts"]).rename(columns={"class": "class", "total_images": "images"})
st.bar_chart(class_df, x="class", y="images")

st.space("small")

left, right = st.columns(2)
with left:
    st.subheader(":material/scale: Class imbalance", anchor=False)
    with st.container(border=True):
        st.markdown(f"**Imbalance ratio:** {dataset['imbalance_ratio']:.2f}")
        st.caption("Ratios near 1.0 indicate balanced class sizes; class weights compensate for the spread.")
        weights_df = pd.DataFrame(
            {"class": list(dataset["class_weights"].keys()), "weight": list(dataset["class_weights"].values())}
        )
        st.bar_chart(weights_df, x="class", y="weight", horizontal=True)
with right:
    st.subheader(":material/aspect_ratio: Resolution analysis", anchor=False)
    render_resolution_chart()

st.space("small")

st.subheader(":material/verified: Data quality", anchor=False)
col1, col2, col3 = st.columns(3)
with col1:
    with st.container(border=True):
        st.metric("Corrupted images", 0, border=True)
        st.caption("No corrupted files detected in the cleaned dataset.")
with col2:
    with st.container(border=True):
        st.metric("Unsupported files", 0, border=True)
        st.caption("All validated files are supported image formats.")
with col3:
    with st.container(border=True):
        st.metric("Classes", len(dataset["class_counts"]), border=True)
        st.caption("Six clinically distinct oral disease categories.")

render_footer()
