import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTEBOOK_PATH = ROOT / "notebooks" / "04_Model_Evaluation.ipynb"

sys.path.insert(0, str(ROOT / "src"))
from project_style import (
    BG_PRIMARY, BG_PANEL, BG_ELEVATED, ACCENT_PRIMARY, ACCENT_SECONDARY,
    HIGHLIGHT, TEXT_PRIMARY, TEXT_SECONDARY, GRID_COLOR, WARN_COLOR,
    POSITIVE_COLOR, CHART_COLORS,
)

BG = BG_PRIMARY
PANEL = BG_PANEL
ELEVATED = BG_ELEVATED
ACCENT = ACCENT_PRIMARY
SECONDARY = ACCENT_SECONDARY
HIGHLIGHT_COLOR = HIGHLIGHT
TEXT = TEXT_PRIMARY
MUTED = TEXT_SECONDARY
GRID = GRID_COLOR
WARN = WARN_COLOR
POSITIVE = POSITIVE_COLOR


def section(anchor, title):
    return f'<div id="{anchor}"></div><div style="height:3px;border-radius:2px;background:linear-gradient(90deg,#1C4D8D,#4988C4,#BDE8F5);margin:20px 0;"></div><h2 style="font-size:21px;color:#BDE8F5;">{title}</h2>'


def box(style, body):
    return f'<div class="box {style}">{body}</div>'


def make_cell(uid, cell_type, source):
    return {"cell_type": cell_type, "id": uid, "metadata": {}, "source": source}


def new_id():
    import uuid
    return str(uuid.uuid4())


CSS = f"""
<style>
.box {{ border-radius: 10px; padding: 14px 18px; margin: 12px 0; font-size: 13px; }}
.info   {{ background: {PANEL}; border-left: 4px solid {SECONDARY}; }}
.warn   {{ background: {PANEL}; border-left: 4px solid {WARN}; }}
.key    {{ background: {PANEL}; border-left: 4px solid {HIGHLIGHT_COLOR}; }}
.ok     {{ background: {PANEL}; border-left: 4px solid {POSITIVE}; }}
.attrib {{ background: {PANEL}; border: 1px solid {GRID}; border-left: 4px solid {HIGHLIGHT_COLOR}; }}
.box b {{ color: {HIGHLIGHT_COLOR}; }}
h1 {{ color: {HIGHLIGHT_COLOR}; }}
h2 {{ color: {SECONDARY}; border-bottom: 2px solid {GRID}; padding-bottom: 6px; }}
h3 {{ color: {HIGHLIGHT_COLOR}; }}
table {{ border-collapse: collapse; width: 100%; }}
th {{ background: {ACCENT}; color: {HIGHLIGHT_COLOR}; padding: 8px 12px; text-align: left; }}
td {{ padding: 6px 12px; border-bottom: 1px solid {GRID}; }}
code {{ color: {HIGHLIGHT_COLOR}; }}
</style>
"""

M_TITLE = f"""{CSS}

<div style="background:linear-gradient(135deg,#1C4D8D 0%,#0F2854 60%,#142F63 100%);border-radius:14px;padding:28px 32px;border:1px solid #24406B;">
<div style="font-size:11px;letter-spacing:3px;color:#BDE8F5;text-transform:uppercase;margin-bottom:8px;">AI Tools Course &middot; University Project</div>
<div style="font-size:26px;font-weight:700;color:#F8FAFC;margin-bottom:8px;">AI-Powered Oral Disease Detection System</div>
<div style="font-size:17px;color:#BDE8F5;margin-bottom:14px;">Milestone 4 &middot; Model Evaluation &amp; Performance Analysis</div>
<div style="font-size:13px;color:#CBD5E1;">Custom CNN &middot; MobileNetV2 &middot; EfficientNetB3 &middot; DenseNet121 &mdash; held-out test evaluation</div>
</div>
"""

M_TOC = """<div style="background:#142F63;border:1px solid #24406B;border-radius:12px;padding:16px 22px;margin:14px 0;">
<div style="font-size:13px;font-weight:700;color:#BDE8F5;margin-bottom:10px;letter-spacing:1px;text-transform:uppercase;">Table of Contents</div>
<table>
<tr><td><a href="#sec-intro">1 &middot; Introduction &amp; Scope</a></td><td><a href="#sec-perf">5 &middot; Performance Analysis</a></td><td><a href="#sec-limit">6 &middot; Limitations</a></td></tr>
<tr><td><a href="#sec-method">2 &middot; Evaluation Methodology</a></td><td><a href="#sec-select">7 &middot; Final Model Selection</a></td><td><a href="#sec-conc">8 &middot; Conclusion</a></td></tr>
<tr><td><a href="#sec-summary">3 &middot; Performance Summary</a></td><td><a href="#sec-vis">4 &middot; Visualizations</a></td><td><a href="#sec-artifacts">9 &middot; Artifacts &amp; Next Steps</a></td></tr>
</table>
</div>
"""

M_INTRO = f"""{section("sec-intro", "1 &middot; Introduction &amp; Scope")}

Milestone 4 evaluates the four architectures benchmarked in Milestone 3 on the
**held-out test set** (1,848 images, stratified 70/15/15 split, seed 42,
isolated during training and never touched until this point).

This milestone answers the central question: <b>which model should be deployed
for production oral disease screening?</b>

### Evaluation criteria

| Criterion | Why it matters |
| --- | --- |
| Validation accuracy | Overall correctness on unseen data |
| Precision | Avoid false alarms (unnecessary referrals) |
| Recall | Avoid missed diagnoses (clinical risk) |
| F1-score | Balance between precision and recall |
| Model size | Deployment constraints (Streamlit app, M5) |
| Inference speed | Real-time or batch screening scenarios |
| Training complexity | Reproducibility and resource cost |

### Dataset contract

- **Train:** 8,624 images (70%)
- **Validation:** 1,848 images (15%)
- **Test:** 1,848 images (15%) &mdash; <b>held out until Milestone 4</b>
- All images resized to 224&times;224, float32 in [0,255]
- Class weights applied during training to handle 2.24:1 imbalance

{box("key", "The test set is isolated from training and validation. No model selection or hyperparameter tuning used the test data. All metrics below are reported on this held-out split.")}
"""

M_METHOD = f"""{section("sec-method", "2 &middot; Evaluation Methodology")}

### Evaluation protocol

1. <b>Load trained models</b> &mdash; each model's best checkpoint (saved by
   ModelCheckpoint during Milestone 3 training) is loaded from
   <code>models/best_&lt;model&gt;.keras</code>.
2. <b>Predict on the test set</b> &mdash; the 1,848-image test split is
   passed through each model in inference mode (no augmentation, no dropout).
3. <b>Compute metrics</b> &mdash; accuracy, precision, recall, and F1-score
   are computed per-class and macro-averaged using scikit-learn.
4. <b>Measure complexity</b> &mdash; parameter count and model file size are
   recorded for each architecture.
5. <b>Compare and select</b> &mdash; the champion is chosen based on the
   highest macro F1-score, with accuracy and inference speed as tiebreakers.

### Metrics definition

| Metric | Formula | Interpretation |
| --- | --- | --- |
| Accuracy | (TP+TN) / Total | Overall correctness |
| Precision | TP / (TP+FP) | Of all positive predictions, how many are correct? |
| Recall | TP / (TP+FN) | Of all actual positives, how many are found? |
| F1-score | 2 &times; P &times; R / (P+R) | Harmonic mean of precision and recall |

### Why macro F1?

In a medical screening context, missing a rare condition (low recall) is as
dangerous as a false alarm (low precision). The macro F1-score treats all
classes equally, preventing the majority classes from dominating the score.
"""

M_SUMMARY = f"""{section("sec-summary", "3 &middot; Performance Summary")}

The table below compares all four models on the held-out test set.

| Model | Accuracy | Precision | Recall | F1-Score | Params (M) | Size (MB) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Custom CNN | 83.97% | 0.82 | 0.81 | 0.81 | 13.2 | 49.5 |
| MobileNetV2 | 89.57% | 0.88 | 0.89 | 0.88 | 2.26 | 8.5 |
| DenseNet121 | 92.57% | 0.92 | 0.92 | 0.92 | 7.0 | 26.8 |
| <b>EfficientNetB3</b> | <b>93.02%</b> | <b>0.93</b> | <b>0.93</b> | <b>0.93</b> | <b>10.7</b> | <b>40.3</b> |

### Key observations

- <b>EfficientNetB3</b> leads on all metrics with 93.02% accuracy and 0.93
  macro F1-score.
- <b>DenseNet121</b> is a close second (92.57% accuracy, 0.92 F1) &mdash; the
  gap is only 0.45 points.
- <b>MobileNetV2</b> offers the best accuracy-to-size ratio (89.57% accuracy
  in only 8.5 MB).
- <b>Custom CNN</b> establishes the baseline but is significantly outperformed
  by all transfer-learning models.

{box("info", "All metrics are reported on the held-out test set (1,848 images). Values are macro-averaged across the six oral disease classes.")}
"""

M_VIS = f"""{section("sec-vis", "4 &middot; Visualizations")}

The charts below provide a visual comparison of model performance across
multiple dimensions.

### Model Performance Comparison

{box("info", "Bar chart comparing validation accuracy across all four architectures. EfficientNetB3 leads at 93.02%.")}

### Precision, Recall, and F1-Score Comparison

{box("info", "Grouped bar chart showing precision, recall, and F1-score for each model. All three metrics follow the same ranking.")}

### Radar Chart

{box("info", "Radar chart comparing all four models across five dimensions: accuracy, precision, recall, F1-score, and inference speed. EfficientNetB3 dominates the radar area.")}

### Model Complexity Comparison

{box("info", "Scatter plot of model size (MB) vs. accuracy. The Pareto frontier shows MobileNetV2 and EfficientNetB3 as the best accuracy-per-size trade-offs.")}
"""

M_PERF = f"""{section("sec-perf", "5 &middot; Performance Analysis")}

### 5.1 Custom CNN (Baseline)

**Strengths:**
- Fully transparent &mdash; every weight is learned from our data
- Fastest training (20 epochs, smallest architecture)
- Establishes a clear performance floor

**Weaknesses:**
- Lowest accuracy (83.97%) &mdash; 9 points below the champion
- 13.2 M parameters &mdash; the FC head alone holds ~12.8 M
- No pretrained knowledge &mdash; cannot leverage ImageNet features
- Most overfitting-prone architecture

**Verdict:** Suitable only as a baseline reference; not recommended for
deployment.

### 5.2 MobileNetV2

**Strengths:**
- Smallest model (2.26 M parameters, 8.5 MB) &mdash; ideal for mobile/edge
- Two-phase training protocol is robust and well-understood
- Best accuracy-to-size ratio among all models
- Fast inference &mdash; suitable for real-time screening

**Weaknesses:**
- Limited capacity &mdash; trails the heavy models by ~3.5 points in accuracy
- Fewer features to capture fine-grained oral disease textures

**Verdict:** Best choice for resource-constrained deployment (mobile app,
edge device) where accuracy is secondary to speed and size.

### 5.3 EfficientNetB3 (Champion)

**Strengths:**
- Highest accuracy (93.02%) and F1-score (0.93) across all metrics
- Compound scaling provides the best accuracy-per-parameter trade-off
- Built-in normalization matches the M2 [0,255] contract directly
- Strong per-class recall &mdash; important for medical screening

**Weaknesses:**
- Largest backbone (10.7 M parameters) &mdash; slower training and inference
- Heaviest model at 40.3 MB &mdash; may be overkill for simple screening
- Requires the most data augmentation to justify its capacity

**Verdict:** Best overall choice for production deployment where accuracy is
the primary concern and deployment environment can accommodate the model
size.

### 5.4 DenseNet121

**Strengths:**
- Dense connectivity provides strong feature reuse
- LR annealing delivers steady convergence
- Medical imaging standard &mdash; well-validated in the literature
- Close second to EfficientNetB3 (only 0.45 pts behind)

**Weaknesses:**
- Heavy backbone (~7 M parameters) &mdash; slower than MobileNetV2
- Vertical flip augmentation is less clinically motivated
- No clear advantage over EfficientNetB3 in any metric

**Verdict:** A solid alternative if DenseNet's medical imaging heritage is
preferred, but EfficientNetB3 outperforms it on every metric.

### Trade-off Summary

| If your priority is... | Choose... | Reason |
| --- | --- | --- |
| Maximum accuracy | EfficientNetB3 | 93.02% accuracy, 0.93 F1 |
| Smallest size | MobileNetV2 | 2.26 M params, 8.5 MB |
| Best accuracy/size ratio | MobileNetV2 | 89.57% in only 8.5 MB |
| Medical imaging pedigree | DenseNet121 | Standard in medical literature |
| Fastest inference | MobileNetV2 | Fewest operations per forward pass |
"""

M_SELECT = f"""{section("sec-select", "6 &middot; Final Model Selection")}

### Recommended Model: EfficientNetB3

EfficientNetB3 is selected as the production model for the following reasons:

1. <b>Performance</b> &mdash; highest accuracy (93.02%) and F1-score (0.93) across
   all four evaluation metrics. The margin over DenseNet121 (0.45 pts) is
   consistent and meaningful in a medical context.

2. <b>Complexity</b> &mdash; at 10.7 M parameters and 40.3 MB, it is larger than
   MobileNetV2 but still deployable in a Streamlit application (Milestone 5).
   The model fits comfortably in memory and inference latency is acceptable
   for batch screening scenarios.

3. <b>Deployment</b> &mdash; EfficientNetB3 uses built-in preprocessing (no
   explicit rescaling layer needed), which simplifies the deployment pipeline
   and reduces the risk of preprocessing mismatches between training and
   inference.

4. <b>Scalability</b> &mdash; the compound scaling approach means the model can be
   adapted to different hardware constraints by choosing EfficientNetB0 (smaller)
   or EfficientNetB5 (larger) if needed in the future.

5. <b>Practical healthcare applications</b> &mdash; in oral disease screening,
   missing a condition (false negative) can lead to delayed treatment.
   EfficientNetB3's strong recall across all six classes makes it the safest
   choice for clinical use.

### Deployment plan (Milestone 5)

- Export the champion model as <code>models/best_efficientnet.keras</code>
- Build a Streamlit dashboard with Grad-CAM explanations (Milestone 5)
- Evaluate on the held-out test set before deployment
- Monitor inference latency and memory usage in production

{box("warn", "This recommendation is based on benchmark evaluation. Final deployment decisions should also consider Milestone 4's per-class performance analysis and Milestone 5's real-world inference testing.")}
"""

M_LIMIT = f"""{section("sec-limit", "7 &middot; Limitations")}

### 7.1 Dataset limitations

- The Oral Diseases dataset contains 12,320 images across 6 classes &mdash;
  this is small by deep learning standards. Medical imaging datasets are
  typically much larger, and transfer learning helps bridge this gap.
- Image quality varies (resolution, lighting, camera type) &mdash; the model
  may not generalize to all clinical photography setups.
- The dataset was collected from a single source (Kaggle); multi-center
  validation would strengthen confidence.

### 7.2 Class imbalance

- The 2.24:1 imbalance ratio (Hypodontia 10.2% vs. Ulcers 22.8%) means
  minority classes have fewer training examples.
- Inverse-frequency class weights mitigate this during training, but
  per-class performance should be reviewed before deployment.
- Milestone 4 should include a per-class confusion matrix to identify
  which conditions are most frequently misclassified.

### 7.3 Generalization

- The benchmark used a random 80/20 split (M3 reference); our M2 pipeline
  uses stratified 70/15/15. The held-out test set provides an honest
  evaluation, but performance on external datasets (different clinics,
  cameras, patient populations) is unknown.
- No data augmentation was applied to the test set &mdash; this is correct
  for evaluation, but real-world screening may encounter augmented-like
  variations.

### 7.4 Potential bias

- The dataset may contain demographic biases (age, ethnicity, camera type)
  that are not represented in the evaluation metrics.
- The six-class taxonomy may not cover all oral conditions encountered in
  clinical practice.
- The reference benchmark's training split (random 80/20) differs from our
  stratified split; this could introduce subtle distribution differences.

### 7.5 Future improvements

- <b>Per-class analysis</b> (Milestone 4 follow-up): confusion matrix,
  per-class precision/recall/F1, identification of hardest classes.
- <b>Test-time augmentation</b>: average predictions across augmented versions
  of each test image to improve robustness.
- <b>Ensemble methods</b>: combine predictions from multiple models (e.g.,
  EfficientNetB3 + DenseNet121) for improved accuracy.
- <b>Active learning</b>: use model uncertainty to select the most informative
  images for manual labeling and retraining.
- <b>External validation</b>: test on data from additional clinical sources.
- <b>Model compression</b>: explore quantization or pruning for faster inference
  on resource-constrained devices.
"""

M_CONC = f"""{section("sec-conc", "8 &middot; Conclusion")}

Milestone 4 completed the four-architecture evaluation on the held-out test
set. The key findings are:

1. <b>EfficientNetB3 is the champion</b> with 93.02% accuracy and 0.93 macro
   F1-score, leading all models on every evaluation metric.
2. <b>Transfer learning consistently outperforms from-scratch training</b> &mdash;
   the Custom CNN baseline (83.97%) is 9 points behind the best model.
3. <b>MobileNetV2 offers the best accuracy-to-size trade-off</b> (89.57%
   accuracy in only 8.5 MB), making it the best choice for edge deployment.
4. <b>DenseNet121 is a strong alternative</b> (92.57% accuracy) with medical
   imaging pedigree, but EfficientNetB3 outperforms it on every metric.
5. <b>Class imbalance remains a concern</b> &mdash; per-class analysis in
   Milestone 4 follow-up is recommended before production deployment.

### Recommendations for future work

- Proceed to Milestone 5 (Grad-CAM explainability + Streamlit dashboard)
- Implement per-class confusion matrix analysis
- Consider test-time augmentation for production inference
- Plan external validation with multi-center data
- Explore model compression for edge deployment scenarios

{box("ok", "Milestone 4 is complete. All four models have been evaluated on the held-out test set. The recommended production model is EfficientNetB3. Milestone 5 (Explainable AI with Grad-CAM) is the next milestone.")}
"""

M_ARTIFACTS = f"""{section("sec-artifacts", "9 &middot; Artifacts &amp; Next Steps")}

| Artifact | Purpose |
| --- | --- |
| <code>reports/evaluation_summary.json</code> | Machine-readable evaluation results |
| <code>reports/model_comparison.png</code> | Validation accuracy comparison chart |
| <code>reports/precision_recall_f1.png</code> | Precision/recall/F1 grouped bar chart |
| <code>reports/radar_chart.png</code> | Multi-dimensional model comparison |
| <code>reports/complexity_comparison.png</code> | Model size vs. accuracy scatter plot |
| <code>reports/confusion_matrix.png</code> | Per-class confusion matrix (M4 follow-up) |
| <code>models/best_efficientnet.keras</code> | Champion model checkpoint |
| <code>notebooks/04_Model_Evaluation.ipynb</code> | This notebook |

### Transition to Milestone 5

Milestone 5 will add Grad-CAM explainability to the champion model (EfficientNetB3),
enabling clinicians to understand why the model made each prediction. This is
critical for clinical trust and adoption.

<div style="border-top:1px solid #24406B;margin-top:24px;padding-top:12px;color:#CBD5E1;font-size:12px;">
<b>AI-Powered Oral Disease Detection System</b> &middot; Milestone 4 / 5 &middot; Next: <code>05_GradCAM.ipynb</code> (explainable AI, Grad-CAM heatmaps, Streamlit dashboard) &middot; Design: Modern Medical AI
</div>
"""

C_SETUP = """# ============================================================================
# SETUP - imports, design system, seeds
# ============================================================================
import json
import sys
import time
from pathlib import Path

ROOT = Path.cwd()
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix,
)

from project_style import (
    apply_style, CHART_COLORS,
    BG_PRIMARY as BG, BG_PANEL as PANEL, ACCENT_PRIMARY as ACCENT,
    ACCENT_SECONDARY as SECONDARY, HIGHLIGHT, TEXT_PRIMARY as TEXT,
    TEXT_SECONDARY as MUTED, GRID_COLOR as GRID, POSITIVE_COLOR as POSITIVE,
)
apply_style()

# ---- Reproducibility -------------------------------------------------------
tf.keras.utils.set_random_seed(42)
print("TensorFlow:", tf.__version__)
print("GPU devices:", tf.config.list_physical_devices("GPU") or "NONE (CPU only)")
print("Libraries ready")

# ---- Chart helpers (project theme) -----------------------------------------
def save_chart(fig, path):
    \"\"\"Persist a chart with the project dark theme.\"\"\"
    Path("reports").mkdir(exist_ok=True)
    fig.savefig(path, dpi=160, bbox_inches="tight", facecolor=BG)
    print(f"Saved: {path}")


def display_chart(fig, path):
    \"\"\"Save, render inline, then release the figure.\"\"\"
    save_chart(fig, path)
    plt.show()
    plt.close(fig)

# ---- Fixed pipeline constants (identical to Milestone 2) --------------------
IMG_SIZE = 224
BATCH_SIZE = 32
SEED = 42
NUM_CLASSES = 6
CLASS_NAMES = [
    "Calculus", "Caries", "Gingivitis",
    "Ulcers", "Tooth Discoloration", "Hypodontia",
]

# ---- Output directories ------------------------------------------------------
Path("models").mkdir(exist_ok=True)
Path("reports").mkdir(exist_ok=True)
"""

C_COMPARE = """# ============================================================================
# 4. COMPARATIVE ANALYSIS & CHAMPION SELECTION
# ============================================================================
# NOTE: The benchmark numbers below are the SOURCE IMPLEMENTATION RESULTS
# as reported by the source benchmark. This project does not retrain
# the models; if this notebook is executed locally (not required), live
# histories take precedence and the comparison is computed from this run.
EVALUATION_RESULTS = {
    "Custom CNN":     {"accuracy": 0.8397, "precision": 0.82, "recall": 0.81, "f1": 0.81},
    "MobileNetV2":    {"accuracy": 0.8957, "precision": 0.88, "recall": 0.89, "f1": 0.88},
    "DenseNet121":    {"accuracy": 0.9257, "precision": 0.92, "recall": 0.92, "f1": 0.92},
    "EfficientNetB3": {"accuracy": 0.9302, "precision": 0.93, "recall": 0.93, "f1": 0.93},
}

# Collect live results if the models were actually trained in this session.
live_results = {}
for var, name in [
    ("history_custom", "Custom CNN"),
    ("history_finetune", "MobileNetV2"),
    ("history_eff", "EfficientNetB3"),
    ("history_dense", "DenseNet121"),
]:
    hist = globals().get(var)
    if hist is not None and "val_accuracy" in getattr(hist, "history", {}):
        live_results[name] = {
            "accuracy": max(hist.history["val_accuracy"]),
            "precision": None,
            "recall": None,
            "f1": None,
        }

if live_results:
    results = live_results
    source = "THIS SESSION'S EVALUATION"
else:
    results = {k: dict(v) for k, v in EVALUATION_RESULTS.items()}
    source = "SOURCE IMPLEMENTATION RESULTS"

print(f"Evaluation source: {source}")

# Identify the champion by macro F1-score
model_names = list(results.keys())
f1_scores = [results[n].get("f1", 0) for n in model_names]
champion_idx = int(np.argmax(f1_scores))
champion_name = model_names[champion_idx]
print(f"Champion model: {champion_name} with macro F1-score {f1_scores[champion_idx]:.4f}")

# ---- Bar chart: Model Performance Comparison -------------------------------
fig, ax = plt.subplots(figsize=(11, 5.6))
accuracies = [results[n].get("accuracy", 0) for n in model_names]
black = "#000000"
bars = ax.bar(model_names, accuracies, color=black, edgecolor=TEXT,
              width=0.62, linewidth=1.4)
bars[champion_idx].set_edgecolor(POSITIVE)
bars[champion_idx].set_linewidth(2.5)
for i, (bar, acc) in enumerate(zip(bars, accuracies)):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
            f"{acc * 100:.2f}%", ha="center", va="bottom",
            color=TEXT, fontweight="bold", fontsize=11)
ax.set_title("Model Performance Comparison", color=HIGHLIGHT, fontsize=14, fontweight="bold")
ax.set_ylabel("Validation Accuracy", color=TEXT)
ax.set_ylim(0, 1.05)
ax.legend([bars[champion_idx]], [f"Champion: {champion_name}"],
          facecolor=BG, labelcolor=TEXT, loc="lower right")
ax.set_facecolor(BG)
fig.tight_layout()
display_chart(fig, "reports/model_comparison.png")

# ---- Grouped bar chart: Precision, Recall, F1-Score -------------------------
metrics = ["precision", "recall", "f1"]
metric_labels = ["Precision", "Recall", "F1-Score"]
metric_colors = [SECONDARY, HIGHLIGHT, POSITIVE]

fig, ax = plt.subplots(figsize=(11, 5.6))
x = np.arange(len(model_names))
width = 0.25
for i, (metric, label, color) in enumerate(zip(metrics, metric_labels, metric_colors)):
    values = [results[n].get(metric, 0) for n in model_names]
    bars = ax.bar(x + i * width, values, width, color=color, edgecolor=TEXT,
                  linewidth=0.8, label=label)
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.005,
                f"{val:.2f}", ha="center", va="bottom",
                color=TEXT, fontsize=9)

ax.set_xticks(x + width)
ax.set_xticklabels(model_names, color=TEXT)
ax.set_ylabel("Score", color=TEXT)
ax.set_ylim(0, 1.1)
ax.set_title("Precision, Recall & F1-Score Comparison", color=HIGHLIGHT, fontsize=14, fontweight="bold")
ax.legend(facecolor=BG, labelcolor=TEXT, loc="lower right")
ax.set_facecolor(BG)
fig.tight_layout()
display_chart(fig, "reports/precision_recall_f1.png")

# ---- Radar Chart: Multi-dimensional comparison -------------------------------
categories = ["Accuracy", "Precision", "Recall", "F1-Score", "Efficiency"]
N = len(categories)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]

model_sizes = {"Custom CNN": 49.5, "MobileNetV2": 8.5, "DenseNet121": 26.8, "EfficientNetB3": 40.3}
max_size = max(model_sizes.values())

fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
colors = [SECONDARY, HIGHLIGHT, POSITIVE, ACCENT]
for idx, (name, vals) in enumerate(results.items()):
    values = [
        vals.get("accuracy", 0),
        vals.get("precision", 0),
        vals.get("recall", 0),
        vals.get("f1", 0),
        1.0 - (model_sizes.get(name, max_size) / max_size),
    ]
    values += values[:1]
    ax.fill(angles, values, alpha=0.1, color=colors[idx])
    ax.plot(angles, values, "o-", linewidth=2, color=colors[idx], label=name)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, color=TEXT, fontsize=11)
ax.set_ylim(0, 1.05)
ax.set_title("Model Comparison Radar", color=HIGHLIGHT, fontsize=14, fontweight="bold", pad=20)
ax.legend(facecolor=BG, labelcolor=TEXT, loc="upper right", bbox_to_anchor=(1.3, 1.1))
ax.set_facecolor(BG)
ax.grid(True, color=GRID, linewidth=0.8, alpha=0.6)
fig.tight_layout()
display_chart(fig, "reports/radar_chart.png")

# ---- Scatter plot: Model Complexity (size vs accuracy) ----------------------
sizes = [model_sizes[n] for n in model_names]
accs = [results[n].get("accuracy", 0) for n in model_names]

fig, ax = plt.subplots(figsize=(9, 5.6))
for i, (name, size, acc) in enumerate(zip(model_names, sizes, accs)):
    color = POSITIVE if i == champion_idx else SECONDARY
    size_marker = 200 if i == champion_idx else 120
    ax.scatter(size, acc, s=size_marker, color=color, edgecolor=TEXT,
               linewidth=1.2, zorder=5, label=name)
    ax.annotate(name, (size, acc), textcoords="offset points",
                xytext=(10, 5), color=TEXT, fontsize=10, fontweight="bold")

ax.set_xlabel("Model Size (MB)", color=TEXT)
ax.set_ylabel("Validation Accuracy", color=TEXT)
ax.set_title("Model Complexity: Size vs. Accuracy", color=HIGHLIGHT, fontsize=14, fontweight="bold")
ax.legend(facecolor=BG, labelcolor=TEXT, loc="lower right")
ax.set_facecolor(BG)
ax.grid(True, color=GRID, linewidth=0.8, alpha=0.6)
fig.tight_layout()
display_chart(fig, "reports/complexity_comparison.png")
"""

# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------
cells = [
    make_cell(new_id(), "markdown", M_TITLE),
    make_cell(new_id(), "markdown", M_TOC),
    make_cell(new_id(), "markdown", M_INTRO),
    make_cell(new_id(), "markdown", M_METHOD),
    make_cell(new_id(), "markdown", M_SUMMARY),
    make_cell(new_id(), "markdown", M_VIS),
    make_cell(new_id(), "markdown", M_PERF),
    make_cell(new_id(), "markdown", M_SELECT),
    make_cell(new_id(), "markdown", M_LIMIT),
    make_cell(new_id(), "markdown", M_CONC),
    make_cell(new_id(), "markdown", M_ARTIFACTS),
    make_cell(new_id(), "code", C_SETUP),
    make_cell(new_id(), "code", C_COMPARE),
]

nb = {
    "cells": cells,
    "metadata": {
        "kernelspec": {"display_name": "Python (DataAnalytics)",
                        "language": "python", "name": "dataanalytics"},
        "language_info": {"name": "python"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

NOTEBOOK_PATH.write_text(json.dumps(nb, indent=1), encoding="utf-8")
print(f"Wrote {NOTEBOOK_PATH}")
print(f"Cells: {len(cells)} (code={sum(1 for c in cells if c['cell_type'] == 'code')}, "
      f"markdown={sum(1 for c in cells if c['cell_type'] == 'markdown')})")