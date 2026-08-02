# AI-Powered Oral Disease Detection System
## Milestone 1 — Exploratory Data Analysis (EDA)

Dark theme: `#0F2854` / `#1C4D8D` / `#4988C4` / `#BDE8F5`

---

## Slide 1 — Title

**AI-Powered Oral Disease Detection System Using Transfer Learning and Explainable AI**

*Milestone 1: Exploratory Data Analysis*

**Key bullets:**
- University AI Tools course project
- 12,320 oral cavity images across 6 disease classes
- Pipeline: EDA → Preprocessing → EfficientNetB0 training → Grad-CAM explainability
- Design system: Modern Medical AI (dark theme, `#0F2854`)

**Recommended visual:** dataset banner with class icons, small class distribution preview.

**Speaker notes (≈180 words):**
Good morning/afternoon. Today I present Milestone 1 of our AI-powered oral disease detection system: an exploratory data analysis of the Oral Diseases dataset. Our project goal is a classifier that can flag six common oral conditions — Calculus, Caries, Gingivitis, Ulcers, Tooth Discoloration, and Hypodontia — using transfer learning with EfficientNetB0, and to explain each prediction with Grad-CAM heatmaps so the system remains trustworthy for clinical review. This milestone is the foundation: before we can design a preprocessing pipeline or train a model, we must understand what data we actually have. In this session I will show you how we discovered and validated the dataset structure, measured class balance and image quality, audited data quality, and translated those findings into concrete recommendations for the preprocessing phase. The work was built as a fully reproducible Jupyter notebook with a consistent dark design system, so every chart you see is publication-ready. Let us begin with the dataset structure and loading phase.

---

## Slide 2 — Key Findings

**What the data tells us**

**Key bullets:**
- 12,320 images, 6 classes; imbalance 2.24:1 (Hypodontia smallest at 10.2%)
- Clean quality: 0 corrupted, 0 within-class duplicates, 0 unsupported files
- Resolution varies → resize to 224x224 required
- Mixed YOLO-annotated folder excluded (noisy labels)

**Recommended visual:** class distribution bar chart + pie chart (from `reports/class_distribution.png`, `reports/class_pie.png`).

**Speaker notes (≈190 words):**
The dataset is clean and well structured. We found 12,320 usable images across six folders, with the largest class, Ulcers, holding about 22.8 percent and the smallest, Hypodontia, only about 10.2 percent — an imbalance ratio of roughly 2.24 to 1. This is moderate, not extreme, but it will shape our training strategy. Our quality audit found zero corrupted images, zero duplicate filenames within any class, and zero unsupported files; the only flagged items were a few empty label folders inside the mixed YOLO-annotated directory, which we exclude anyway because its labels are noisy and inconsistent. On the imaging side, resolution and aspect ratio vary noticeably across samples, which means Milestone 2 must standardize everything to the EfficientNetB0 input size of 224 by 224 pixels, and normalization must follow the EfficientNet preprocessing contract rather than generic scaling. Overall, the data is strong enough for transfer learning, provided we handle the imbalance with class weights and a stratified split. Next, I will summarize our recommendations and the transition to preprocessing.

---

## Slide 3 — Recommendations & Next Steps

**From EDA to Preprocessing**

**Key bullets:**
- Stratified 70/15/15 split preserves class proportions
- Class weights (inverse frequency) counter Hypodontia/Calculus under-representation
- Mild augmentation: rotation ±15°, flip, zoom, brightness — training only
- RGB + per-channel EfficientNet normalization

**Recommended visual:** class weights chart (`reports/class_weights.png`).

**Speaker notes (≈180 words):**
Based on these findings we have defined the preprocessing and training strategy for Milestone 2 and 3. First, the data will be split stratified at 70, 15, and 15 percent for training, validation, and test, so that every split keeps the same class proportions as the full dataset. Second, we will compute inverse-frequency class weights from the counts you saw earlier, giving Hypodontia and Calculus a stronger contribution to the loss and preventing the model from being biased toward the majority classes. Third, augmentation will stay mild — rotation, horizontal flip, small zoom, and brightness jitter — applied to the training split only, because aggressive transforms could distort clinically meaningful features. Fourth, all images will be resized to 224 by 224 and normalized with the EfficientNetB0 preprocessing function, which expects RGB input in the model's native range. These decisions are fully documented in the notebook and its reports folder, making the project reproducible end to end. That completes the EDA milestone; the next milestone will build the data pipeline, and I look forward to your questions.
