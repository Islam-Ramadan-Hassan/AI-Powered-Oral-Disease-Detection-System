# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), semantic versions per
milestone.

## [Milestone 3] — 2026-08-01

### Model training benchmark (reference implementation integrated, not retrained)

- `notebooks/03_Model_Training.ipynb` — rebuilt (30 cells: 14 code + 16
  markdown), four-architecture benchmark delivered **unexecuted**; benchmark
  metrics are **attributed** as Reference Implementation Results.
- Models preserved from the reference: Custom CNN (83.97%), MobileNetV2
  (89.57%), EfficientNetB3 (93.02% champion), DenseNet121 (92.57%) — training
  logic, callbacks (EarlyStopping, ModelCheckpoint, ReduceLROnPlateau) and
  comparison workflow kept.
- Integration only: M2 partition files (`split_partition.npz`,
  `split_metadata.json`) replace dataset paths; deprecated APIs removed
  (`InputLayer(shape=)`, no `verbose`); hardcoded fallback accuracies removed;
  outputs to `models/` + `reports/`; seed 42 reproducibility.
- Test split (1,848) reserved for Milestone 4 — never touched by training.
- `reports/reference_model_comparison.png`, `reports/training_workflow.png`
  (project theme).
- `scripts/build_train_notebook.py` — rebuilt (4-model benchmark builder with
  embedded base64 charts).

### Deliverables

- `presentation/AI_Powered_Oral_Disease_Detection_System.pptx` — extended to
  **15 slides** (M3: motivation, transfer learning, 4 model slides, reference
  benchmark table + chart, champion analysis, transition). Attribution chips
  (Reference Benchmark Results vs. Our Contribution) on every M3 slide, speaker
  notes on all.
- `deliverables/report_Model_Training.md` — architecture comparison, technical
  analysis, per-model strengths/limitations, reference benchmark discussion.
- `deliverables/viva_preparation_Model_Training.md` — 10 Q&A, common mistakes
  table, one-sentence pitch (reference attribution, transfer learning,
  callbacks, M4 handoff).
- README updated (M3 status, attribution statement, structure).

## [Milestone 2] — 2026-08-01

### Preprocessing pipeline (complete, verified)

- `notebooks/02_Preprocessing.ipynb` — 19 cells (9 code + 10 markdown), executed
  with the `dataanalytics` kernel, **0 errors**, 6 embedded charts.
- Exhaustive cleaning: all 12,320 files PIL-verified + fully decoded → **0 corrupted**
  (`reports/cleaning_report.json`).
- Preprocessing: RGB → 224×224 → float32 **in [0,255]** (Keras EfficientNetB0 contract).
- Augmentation (Keras layers, train-only): flip, rotation ±15°, zoom 0.9–1.1×,
  translation ±10%, brightness ±0.2, contrast ±0.2.
- Stratified 70/15/15 split (8,624/1,848/1,848, seed 42) — verified overlap-free,
  reproducible; persisted to `reports/split_partition.npz` + `split_metadata.json`.
- tf.data pipeline: map → cache → shuffle → augment(train) → batch(32) → prefetch(AUTOTUNE).
- Inverse-frequency class weights 0.7318–1.6427 (`reports/class_weights_final.json`).
- `reports/preprocessing_summary.json` — machine-readable pipeline contract.

### Deliverables

- `presentation/AI_Powered_Oral_Disease_Detection_System.pptx` — live 5-slide deck,
  dark Modern Medical AI theme, speaker notes on all slides.
- `deliverables/report_Preprocessing.md`, `deliverables/viva_preparation_Preprocessing.md`,
  `deliverables/M2_Verification_Report.md` (9.5/10 → READY FOR MODEL TRAINING).
- README updated (M2 status, structure, artifacts).

### Engineering

- `scripts/build_preprocess_notebook.py` (builder), `scripts/execute_notebook.py`
  (nbclient executor), `scripts/build_pptx.py` (deck builder),
  `scripts/verify_dataset.py`, `scripts/verify_split.py`, `scripts/verify_consistency.py`,
  `scripts/bench_cpu.py` (verification + benchmark suite).
- Fixed during final verification:
  - Normalization contract: pipeline kept float32 in [0,255] (EffNetB0 rescales internally;
    [0,1] would double-normalize — verified via feature-correlation test).
  - `RandomBrightness` range: operates in 0–255 space (delta ±51); was saturating [0,1]
    images — verified empirically (76.7–177.9 on mid-gray, expected 76.5–178.5).

## [Milestone 1] — 2026-07-31

### EDA (complete, approved)

- `notebooks/01_EDA.ipynb` — 13 cells (5 code + 8 markdown), executed, 0 errors,
  7 embedded charts, clickable table of contents.
- Findings: 12,320 clean images in 6 classes; imbalance 2.24:1; variable geometry;
  mixed YOLO-annotated folder excluded.
- `reports/`: class distribution, pie, samples, resolution, aspect ratio, formats,
  class weights PNGs + `quality_report.json`, `analysis_summary.json`,
  `class_statistics.csv`.
- Design system established: `src/project_style.py` (Modern Medical AI dark theme).
- Deliverables: `presentation_EDA.md`, `report_EDA.md`, `viva_preparation_EDA.md`,
  `M1_Final_Review.md`.

### Foundation

- Project scaffold: README, `.gitignore`, directory structure, DataAnalytics kernel
  (`C:\Users\Admin\DataAnalytics\.venv`) selected as execution environment,
  TensorFlow 2.21.0 + python-pptx 1.0.2 installed.
