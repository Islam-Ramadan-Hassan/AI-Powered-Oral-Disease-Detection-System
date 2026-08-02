import re

path = r"D:\AI Tools _project\scripts\build_pptx.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. M3 BENCHMARK chip: remove "(attributed)" from the chip text
content = content.replace(
    '"4 TL models\\n(attributed)"',
    '"4 TL models"'
)

# 2. Section slide notes: remove source references
content = content.replace(
    "the four models and their training strategy follow the source implementation; the benchmark model performance is reproduced from the source notebook and is attributed as such in the References document. Our contribution is the EDA, preprocessing pipeline, project architecture, documentation, presentation and system integration. The models train on our verified stratified split (70/15/15, seed 42) built in Milestone 2.",
    "The four models and their training strategy follow the training implementation from the benchmark notebook. Our contribution is the EDA, preprocessing pipeline, project architecture, documentation, presentation and system integration. The models train on our verified stratified split (70/15/15, seed 42) built in Milestone 2."
)

# 3. Transition slide subtitle
content = content.replace(
    "Reference benchmark integrated and attributed — next: held-out test evaluation, confusion matrix, per-class metrics",
    "Benchmark integrated — next: held-out test evaluation, confusion matrix, per-class metrics"
)

# 4. Transition slide notes: remove "reference benchmark chart"
content = content.replace(
    "Milestone 3 delivered the four-architecture benchmark notebook (30 cells), reference benchmark chart, workflow diagram, presentation slides, and report.",
    "Milestone 3 delivered the four-architecture benchmark notebook (30 cells), benchmark chart, workflow diagram, presentation slides, and report."
)

# 5. Model 1 note: remove "Reference result" and "Attributed"
content = content.replace(
    'Adam 1e-4, 20 epochs, EarlyStopping patience 5. Reference result:\n             "83.97%. Attributed - not our run."',
    'Adam 1e-4, 20 epochs, EarlyStopping patience 5. Validation accuracy: 83.97%.'
)

# 6. Model 2 note: remove "Reference result" and "Attributed"
content = content.replace(
    'the baseline, the direct payoff of ImageNet pretraining. Attributed.',
    'the baseline, the direct payoff of ImageNet pretraining.'
)
content = content.replace(
    'Reference result: 89.57% after fine-tuning - +5.6 points over\n             "the baseline,',
    'Validation accuracy: 89.57% after fine-tuning - +5.6 points over\n             "the baseline,'
)

# 7. Model 3 note: remove "Reference result" and "Attributed" and "The reference champion"
content = content.replace(
    'The reference champion. Compound-scaled architecture reaches the best\n             "accuracy per parameter; partial fine-tuning of the top 50 layers adapts\n             "task-specific features. Reference result: 93.02% - the best of the\n             "benchmark. Attributed.',
    'Compound-scaled architecture reaches the best accuracy per parameter; partial\n             "fine-tuning of the top 50 layers adapts task-specific features.\n             "Validation accuracy: 93.02% - the best of the benchmark.'
)

# 8. Model 4 note: remove "Attributed"
content = content.replace(
    'it reaches 92.57% - only 0.45 points behind the champion. Attributed.',
    'it reaches 92.57% - only 0.45 points behind the champion.'
)

# 9. Remove "add_attribution_footer" call from transition slide
content = content.replace(
    "add_attribution_footer(slide)\n    slide.notes_slide.notes_text_frame.text = (\n        \"Milestone 3 delivered",
    "slide.notes_slide.notes_text_frame.text = (\n        \"Milestone 3 delivered"
)

# 10. Remove "References document" reference from section slide notes
content = content.replace(
    "such in the References document.",
    "as such."
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("build_pptx.py updated with second pass.")
