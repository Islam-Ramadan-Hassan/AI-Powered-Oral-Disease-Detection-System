from __future__ import annotations

import io
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[2]


def render_dataset_plots() -> None:
    """Render a few dataset insight charts from the generated reports."""
    import streamlit as st

    summary = pd.read_csv(ROOT / "reports" / "class_statistics.csv")
    summary = summary.rename(columns={"total_images": "count"})
    fig, ax = plt.subplots(figsize=(8, 4.6))
    sns.barplot(data=summary, x="class", y="count", color="#2196F3", ax=ax)
    ax.set_title("Class Distribution")
    ax.set_ylabel("Image Count")
    ax.set_xlabel("Class")
    ax.tick_params(axis="x", rotation=20)
    fig.tight_layout()
    st.pyplot(fig)


def render_resolution_chart() -> None:
    """Render a resolution histogram from the EDA outputs."""
    import streamlit as st

    from PIL import Image

    image_path = ROOT / "reports" / "resolution_distribution.png"
    if image_path.exists():
        image = Image.open(image_path)
        st.image(image, caption="Resolution analysis", width="stretch")


def render_quality_chart() -> None:
    """Render the quality report image from the EDA outputs."""
    import streamlit as st

    from PIL import Image

    image_path = ROOT / "reports" / "quality_report.png"
    if image_path.exists():
        image = Image.open(image_path)
        st.image(image, caption="Data quality", width="stretch")
