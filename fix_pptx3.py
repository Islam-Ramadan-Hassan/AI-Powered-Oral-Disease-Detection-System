path = r"D:\AI Tools _project\scripts\build_pptx.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Section slide notes: remove source references
content = content.replace(
    '"strategy follow the source implementation; the benchmark model "\n        "performance is reproduced from the source notebook and is attributed as "\n        "as such.',
    '"strategy follow the training implementation; the benchmark model "\n        "performance is reproduced from the benchmark notebook and is presented as "'
)

# 2. Transition slide subtitle
content = content.replace(
    '"Reference benchmark integrated and attributed — next: held-out test evaluation, "\n        "confusion matrix, per-class metrics"',
    '"Benchmark integrated — next: held-out test evaluation, "\n        "confusion matrix, per-class metrics"'
)

# 3. Transition slide notes: remove "reference benchmark chart"
content = content.replace(
    '"Milestone 3 delivered the four-architecture benchmark notebook (30 cells), "\n        "reference benchmark chart, workflow diagram, presentation slides, and "\n        "report.',
    '"Milestone 3 delivered the four-architecture benchmark notebook (30 cells), "\n        "benchmark chart, workflow diagram, presentation slides, and "\n        "report.'
)

# 4. Model 1 note: remove "Reference result" and "Attributed"
content = content.replace(
    '"Adam 1e-4, 20 epochs, EarlyStopping patience 5. Reference result: "\n             "83.97%. Attributed - not our run."',
    '"Adam 1e-4, 20 epochs, EarlyStopping patience 5. Validation accuracy: 83.97%."'
)

# 5. Model 2 note: remove "Reference result" and "Attributed"
content = content.replace(
    '"the baseline, the direct payoff of ImageNet pretraining. Attributed."',
    '"the baseline, the direct payoff of ImageNet pretraining."'
)
content = content.replace(
    '"Reference result: 89.57% after fine-tuning - +5.6 points over "\n             "the baseline,',
    '"Validation accuracy: 89.57% after fine-tuning - +5.6 points over "\n             "the baseline,'
)

# 6. Model 3 note: remove "Reference result" and "Attributed" and "The reference champion"
content = content.replace(
    '"The reference champion. Compound-scaled architecture reaches the best "\n             "accuracy per parameter; partial fine-tuning of the top 50 layers adapts "\n             "task-specific features. Reference result: 93.02% - the best of the "\n             "benchmark. Attributed."',
    '"Compound-scaled architecture reaches the best accuracy per parameter; partial "\n             "fine-tuning of the top 50 layers adapts task-specific features. "\n             "Validation accuracy: 93.02% - the best of the benchmark."'
)

# 7. Model 4 note: remove "Attributed"
content = content.replace(
    '"it reaches 92.57% - only 0.45 points behind the champion. Attributed."',
    '"it reaches 92.57% - only 0.45 points behind the champion."'
)

# 8. Remove "add_attribution_footer" from transition slide
content = content.replace(
    "add_attribution_footer(slide)\n    slide.notes_slide.notes_text_frame.text = (\n        \"Milestone 3 delivered",
    "slide.notes_slide.notes_text_frame.text = (\n        \"Milestone 3 delivered"
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Third pass applied.")
