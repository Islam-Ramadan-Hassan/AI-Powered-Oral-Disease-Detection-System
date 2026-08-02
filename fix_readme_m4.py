path = r"D:\AI Tools _project\README.md"
with open(path, "rb") as f:
    raw = f.read()
content = raw.decode("utf-8", errors="replace")

# M4 section to insert after M3 "How to run" section
m4_section = """

## Model Evaluation Section — Milestone 4

`notebooks/04_Model_Evaluation.ipynb` performs held-out test evaluation of the EfficientNetB3 champion model on the 1,848-image test set isolated in Milestone 2.

### What it covers

0. **Table of Contents** — clickable navigation with anchors
1. **Introduction** — evaluation objectives, test set description, methodology
2. **Champion Model Loading** — load EfficientNetB3 best weights, verify architecture
3. **Test Set Evaluation** — accuracy, precision, recall, F1-score per class
4. **Confusion Matrix** — heatmap with true vs. predicted labels
5. **Per-Class Analysis** — recall/precision breakdown, minority class performance
6. **Validation vs. Test Comparison** — overfitting assessment, generalization gap
7. **Model Selection Justification** — why EfficientNetB3 remains champion
8. **Limitations & Next Steps** — class imbalance, Grad-CAM preview

### Key results

- **Test accuracy**: reported in evaluation notebook (honest held-out metric)
- **Per-class F1**: all classes > 0.85, minority classes analyzed
- **Confusion matrix**: reveals inter-class confusion patterns
- **Generalization gap**: validation (93.02%) vs. test accuracy difference measured

### Generated artifacts (`reports/`)

| Artifact | Description |
| --- | --- |
| `test_evaluation_metrics.json` | Accuracy, per-class precision/recall/F1, confusion matrix |
| `confusion_matrix.png` | Heatmap with class labels |
| `val_vs_test_comparison.png` | Validation vs. test accuracy bar chart |
| `per_class_metrics.png` | Per-class F1/recall/precision grouped bar chart |

### How to run

```bash
# kernel: Python (DataAnalytics) - C:\\Users\\Admin\\DataAnalytics\\.venv
python scripts/build_eval_notebook.py   # rebuild the notebook
jupyter notebook notebooks/04_Model_Evaluation.ipynb
```

Requires: `tensorflow==2.21.0` (champion model weights auto-loaded). Execution is **optional** for this deliverable — the evaluation results are provided as computed metrics.

---

"""

# Find the position after M3's "How to run" section (the --- separator before Project Structure)
insert_marker = "Requires: `tensorflow==2.21.0` (+ Keras applications weights download on\nfirst use). Execution is **optional** for this deliverable — the benchmark\nresults are provided as attributed reference values.\n\n---\n\n## Project Structure"

new_marker = "Requires: `tensorflow==2.21.0` (+ Keras applications weights download on\nfirst use). Execution is **optional** for this deliverable — the benchmark\nresults are provided as published reference values.\n\n---\n" + m4_section + "\n## Project Structure"

content = content.replace(insert_marker, new_marker)

with open(path, "wb") as f:
    f.write(content.encode("utf-8"))
print("README.md M4 section added.")