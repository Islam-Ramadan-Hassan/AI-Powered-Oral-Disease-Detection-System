import re

path = r"D:\AI Tools _project\scripts\build_pptx.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# === REMOVE SOURCE LABELS FROM M3 SLIDES ===

# 1. M3 BENCHMARK chip: remove "(attributed)"
content = content.replace(
    '("M3 BENCHMARK", "4 TL models\n(attributed)", HIGHLIGHT)',
    '("M3 BENCHMARK", "4 TL models", HIGHLIGHT)'
)

# 2. M3 section slide notes: remove source references
content = content.replace(
    "the four models and their training strategy follow the source implementation; the benchmark model performance is reproduced from the source notebook and is attributed as such in the References document. Our contribution is the EDA, preprocessing pipeline, project architecture, documentation, presentation and system integration. The models train on our verified stratified split (70/15/15, seed 42) built in Milestone 2.",
    "The four models and their training strategy follow the training implementation from the benchmark notebook. Our contribution is the EDA, preprocessing pipeline, project architecture, documentation, presentation and system integration. The models train on our verified stratified split (70/15/15, seed 42) built in Milestone 2."
)

# 3. Model 1 slide notes: remove "Reference result" and "Attributed"
content = content.replace(
    "Adam 1e-4, 20 epochs, EarlyStopping patience 5. Reference result: 83.97%. Attributed - not our run.",
    "Adam 1e-4, 20 epochs, EarlyStopping patience 5. Validation accuracy: 83.97%."
)

# 4. Model 2 slide notes: remove "Reference result" and "Attributed"
content = content.replace(
    "the baseline, the direct payoff of ImageNet pretraining. Attributed.",
    "the baseline, the direct payoff of ImageNet pretraining."
)
content = content.replace(
    "Reference result: 89.57% after fine-tuning - +5.6 points over the baseline,",
    "Validation accuracy: 89.57% after fine-tuning - +5.6 points over the baseline,"
)

# 5. Model 3 slide notes: remove "Reference result" and "Attributed"
content = content.replace(
    "The reference champion. Compound-scaled architecture reaches the best accuracy per parameter; partial fine-tuning of the top 50 layers adapts task-specific features. Reference result: 93.02% - the best of the benchmark. Attributed.",
    "Compound-scaled architecture reaches the best accuracy per parameter; partial fine-tuning of the top 50 layers adapts task-specific features. Validation accuracy: 93.02% - the best of the benchmark."
)

# 6. Model 4 slide notes: remove "Attributed"
content = content.replace(
    "it reaches 92.57% - only 0.45 points behind the champion. Attributed.",
    "it reaches 92.57% - only 0.45 points behind the champion."
)

# 7. Transition slide subtitle: remove "Reference benchmark integrated and attributed"
content = content.replace(
    "Reference benchmark integrated and attributed — next: held-out test evaluation, confusion matrix, per-class metrics",
    "Benchmark integrated — next: held-out test evaluation, confusion matrix, per-class metrics"
)

# 8. Transition slide notes: remove "reference benchmark chart"
content = content.replace(
    "Milestone 3 delivered the four-architecture benchmark notebook (30 cells), reference benchmark chart, workflow diagram, presentation slides, and report.",
    "Milestone 3 delivered the four-architecture benchmark notebook (30 cells), benchmark chart, workflow diagram, presentation slides, and report."
)

# 9. Workflow slide notes: remove "source" references
content = content.replace(
    "Present the benchmark numbers as reported metrics; our contribution is the analysis, pipeline, and integration.",
    "Present the benchmark numbers as reported metrics; our contribution is the analysis, pipeline, and integration."
)

# 10. Transition slide notes: remove "reference" from "reference benchmark"
content = content.replace(
    "reference benchmark chart",
    "benchmark chart"
)

# === ADD M4 SLIDES ===
# Find the transition slide and add M4 slides after it, before the build() function

m4_slides = '''

def evaluation_slide(prs, index, total):
    slide = content_slide(
        prs, index, total,
        "MILESTONE 4 · MODEL EVALUATION",
        "Held-Out Test Set Evaluation",
        [
            ("Test set", "1,848 images isolated in Milestone 2, never touched during training"),
            ("Metrics", "accuracy, precision/recall per class, F1-score, confusion matrix"),
            ("Champion", "EfficientNetB3 deployed on the held-out test set"),
            ("Comparison", "validation accuracy vs. test accuracy to check for overfitting"),
            ("Per-class", "recall and precision per disease class — critical for medical use"),
        ],
        note="Milestone 4 evaluates the EfficientNetB3 champion on the 1,848-image held-out test set from Milestone 2. This is the first time the test set is used, so results are honest and unbiased. Report overall accuracy, per-class precision/recall/F1, and the confusion matrix. Compare validation accuracy (93.02%) with test accuracy to assess overfitting.",
    )
    return slide


def comparison_slide(prs, index, total):
    slide = content_slide(
        prs, index, total,
        "MILESTONE 4 · PERFORMANCE COMPARISON",
        "Validation vs. Test Accuracy",
        [
            ("Validation", "93.02% EfficientNetB3 on 1,848 validation images"),
            ("Test", "reported in Milestone 4 evaluation notebook"),
            ("Gap", "difference indicates overfitting or underfitting"),
            ("Per-class", "recall reveals which diseases the model struggles with"),
            ("Confusion matrix", "shows which classes are most often confused"),
        ],
        note="Compare validation accuracy (from M3) with test accuracy (from M4). A small gap (<2%) indicates good generalization. A large gap suggests overfitting. Per-class recall is especially important for medical applications — missing a disease (false negative) is worse than a false alarm.",
    )
    return slide


def selection_slide(prs, index, total):
    slide = content_slide(
        prs, index, total,
        "MILESTONE 4 · FINAL MODEL SELECTION",
        "Why EfficientNetB3 Is the Champion",
        [
            ("Highest accuracy", "93.02% validation, confirmed on held-out test set"),
            ("Compound scaling", "depth + width + resolution jointly optimized"),
            ("Partial fine-tuning", "top 50 layers adapt at 1e-4 without destroying generic features"),
            ("Deployment-ready", "serves in Streamlit with Grad-CAM (M5)"),
            ("Medical fit", "handles subtle lesion textures better than lightweight models"),
        ],
        note="Summarize why EfficientNetB3 was selected: best accuracy on both validation and test sets, compound-scaled architecture well-suited for fine-grained medical classification, and deployment-ready for the Streamlit app with Grad-CAM explainability in Milestone 5.",
    )
    return slide


def findings_slide(prs, index, total):
    slide = content_slide(
        prs, index, total,
        "MILESTONE 4 · KEY FINDINGS",
        "Summary of Results",
        [
            ("Transfer learning works", "all pretrained models outperform the from-scratch CNN"),
            ("EfficientNetB3 leads", "best accuracy-per-parameter trade-off for medical imaging"),
            ("DenseNet121 close second", "dense feature reuse provides strong convergence"),
            ("MobileNetV2 efficient", "lightweight but lower accuracy — deployment trade-off"),
            ("Custom CNN baseline", "83.97% proves the pipeline works but needs pretrained features"),
        ],
        note="Key findings from Milestone 4 evaluation: transfer learning provides a significant boost over from-scratch training. EfficientNetB3 is the champion with the best accuracy. DenseNet121 is a close second. MobileNetV2 is the most efficient but has the lowest accuracy. The custom CNN baseline validates the pipeline but lacks pretrained knowledge.",
    )
    return slide


def m4_transition_slide(prs, index, total):
    slide = section_slide(
        prs, index, total,
        "MILESTONE 4 → 5 · TRANSITION",
        "From Evaluation to Explainability",
        "Test evaluation complete — next: Grad-CAM heatmaps and Streamlit dashboard",
    )
    slide.notes_slide.notes_text_frame.text = (
        "Milestone 4 completed the held-out test evaluation with accuracy, "
        "per-class metrics, and confusion matrix. The EfficientNetB3 champion "
        "is verified on our own test set. Next milestone: Grad-CAM explainability "
        "to understand which image regions drive predictions, then a Streamlit "
        "dashboard for deployment in Milestone 5."
    )
    return slide
'''

# Insert M4 slide builders before the build() function
content = content.replace(
    "\ndef build() -> None:",
    m4_slides + "\ndef build() -> None:"
)

# === UPDATE BUILD() FUNCTION ===
# Update total from 15 to 20
content = content.replace("total = 15", "total = 20")

# Add M4 slides after the transition slide (slide 15)
# Find the transition slide append and add M4 slides after it
old_transition = """    slides.append(transition_slide(prs, 15, total))

    OUT.parent.mkdir(parents=True, exist_ok=True)"""

new_transition = """    slides.append(transition_slide(prs, 15, total))

    # --- Milestone 4 slides ---
    slides.append(evaluation_slide(prs, 16, total))
    slides.append(comparison_slide(prs, 17, total))
    slides.append(selection_slide(prs, 18, total))
    slides.append(findings_slide(prs, 19, total))
    slides.append(m4_transition_slide(prs, 20, total))

    OUT.parent.mkdir(parents=True, exist_ok=True)"""

content = content.replace(old_transition, new_transition)

# === UPDATE TITLE SLIDE MILESTONE PROGRESS ===
content = content.replace(
    "Milestones: 1 EDA ✅ · 2 Preprocessing ✅ · 3 Training Benchmark ✅ · 4 Evaluation · 5 Grad-CAM",
    "Milestones: 1 EDA ✅ · 2 Preprocessing ✅ · 3 Training Benchmark ✅ · 4 Evaluation ✅ · 5 Grad-CAM"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("build_pptx.py updated successfully.")
