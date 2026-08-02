from __future__ import annotations

import pandas as pd
import streamlit as st
from PIL import Image

from app.components.footer import render_footer
from app.components.header import render_page_header
from app.components.metrics import render_metric_row
from app.utils.image_utils import resize_for_display
from app.utils.preprocessing import preprocess_and_time, load_image_to_array
from app.utils.prediction import build_model_from_catalog, predict_with_model

render_page_header(
    title="Disease detection",
    subtitle="Upload an oral image and run the same preprocessing and prediction workflow used in training.",
    icon="biotech",
)

st.markdown("**:material/upload: 1 · Upload an image**")
with st.container(border=True):
    uploaded_file = st.file_uploader(
        "Oral image",
        type=["png", "jpg", "jpeg", "webp"],
        help="Accepted formats: PNG, JPG, JPEG, WEBP.",
    )
    if uploaded_file is not None:
        st.success("Image received", icon=":material/check_circle:")
    else:
        st.caption("No file selected yet.")

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.space("small")
    st.markdown("**:material/query_stats: 2 · Inference results**")

    left, right = st.columns([1.1, 1], vertical_alignment="center")
    with left:
        st.image(resize_for_display(image), caption="Uploaded image", width="stretch")

    with right:
        selected_model_id = st.session_state.get("selected_model_id", "efficientnetb3")
        with st.spinner("Running inference..."):
            model, model_path, loaded = build_model_from_catalog(selected_model_id)
            array = load_image_to_array(image)
            tensor, preprocess_ms = preprocess_and_time(array, selected_model_id)
            result = predict_with_model(model, tensor, selected_model_id)

        confidence = result["confidence"]
        if confidence >= 0.8:
            badge = "green"
            tag = "Confident"
        elif confidence >= 0.6:
            badge = "orange"
            tag = "Moderate"
        else:
            badge = "red"
            tag = "Uncertain"

        render_metric_row([
            ("Predicted disease", result["predicted_label"]),
            ("Confidence", f"{confidence * 100:.2f}%"),
            ("Inference", f"{result['inference_ms']} ms"),
        ])
        st.markdown(f":{badge}-badge[{tag} prediction] :gray-badge[{result['model_name']}]")

    st.space("small")

    st.markdown("**:material/bar_chart: Class probabilities**")
    probs_df = pd.DataFrame({"class": result["class_names"], "probability": result["probabilities"]})
    probs_df = probs_df.sort_values("probability", ascending=False)
    st.bar_chart(probs_df, x="class", y="probability", horizontal=True)

    st.space("small")
    st.markdown("**:material/podium: Top-3 predictions**")
    with st.container(border=True):
        for label, score in result["top_predictions"]:
            st.progress(float(score), text=f"{label}: {score:.2%}")

    st.caption(f"Model source: {model_path} · Preprocessing: {preprocess_ms} ms")
else:
    st.space("medium")
    st.info("Upload an image to begin inference.", icon=":material/upload:")

render_footer()
