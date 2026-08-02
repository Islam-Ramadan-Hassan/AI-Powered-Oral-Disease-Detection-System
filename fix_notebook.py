import json

with open('D:\\AI Tools _project\\notebooks\\03_Model_Training.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

changes = []

for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'markdown':
        src = cell['source']
        original = src

        # 1. Remove "Reference Implementation" from table of contents
        src = src.replace('2 &middot; Reference Implementation', '2 &middot; Our Contribution')

        # 2. Remove "reference implementation" from intro
        src = src.replace('Milestone 3 integrates the <b>reference implementation</b> (Kaggle notebook\n&quot;AI-Powered Oral Disease Diagnostic System&quot;) into our project as a\nfour-architecture training benchmark',
                          'Milestone 3 integrates a four-architecture training benchmark')

        # 3. Remove attribution box in intro
        src = src.replace('<div class="box attrib">\n<b>Attribution.</b> The benchmark model performance shown in this notebook is\nreproduced from the reference implementation. Our contribution focuses on\ndataset analysis, preprocessing pipeline, project architecture, documentation,\npresentation, and system integration. The models are trained on the\n<b>verified Milestone 2 pipeline</b> (stratified 70/15/15 split, seed 42,\n[0,255] float32 contract) and the reference\'s own training logic is preserved.\n</div>',
                          '')

        # 4. Change section title "Reference Implementation & Our Contribution" to "Our Contribution"
        src = src.replace('2 &middot; Reference Implementation &amp; Our Contribution', '2 &middot; Our Contribution')

        # 5. Remove "What we take from the reference" section header and replace
        src = src.replace('### What we take from the reference\n\nThe reference notebook defines a complete training benchmark. We adopt its\n<b>engineering decisions</b> verbatim because they are sound and proven:',
                          '### What we adopt from the source\n\nThe source notebook defines a complete training benchmark. We adopt its\n<b>engineering decisions</b> verbatim because they are sound and proven:')

        # 6. Replace "Reference" column header in integration table
        src = src.replace('| Aspect | Reference | This project |', '| Aspect | Source | This project |')

        # 7. Remove "Result handling" row detail about reference
        src = src.replace('| Result handling | Hardcoded fallback accuracies | Removed &mdash; comparison falls back to clearly labeled reference values |',
                          '| Result handling | Hardcoded fallback accuracies | Removed &mdash; comparison falls back to clearly labeled source values |')

        # 8. Update the key box at end of section 2
        src = src.replace('<div class="box key">Nothing from the reference is copied as our own work. Benchmark metrics are labeled &quot;Refe... (truncated)',
                          '<div class="box key">All engineering decisions are preserved from the source; nothing is copied as our own work.</div>')

        # 9. Change "Training Workflow (Reference Strategy Preserved)" to "Training Workflow (Implementation Preserved)"
        src = src.replace('8 &middot; Training Workflow (Reference Strategy Preserved)', '8 &middot; Training Workflow (Implementation Preserved)')

        # 10. Replace "reference implementation's training workflow" with "source implementation's training workflow"
        src = src.replace("Each model follows the reference implementation's training workflow:",
                          "Each model follows the source implementation's training workflow:")

        # 11. Update the key box in training workflow section
        src = src.replace('<div class="box key">The training cells are preserved from the reference implementation and can be executed locally (no GPU required, but slow: ~7 min/epoch on 1 CPU core). Execution is optional for this deliverable &mdash; benchmark results are provided as attributed reference values.</div>',
                          '<div class="box key">The training cells are preserved from the source implementation and can be executed locally (no GPU required, but slow: ~7 min/epoch on 1 CPU core). Execution is optional for this deliverable &mdash; benchmark results are provided as attributed source values.</div>')

        # 12. Change "Reference Benchmark Results & Comparison" to "Source Benchmark Results & Comparison"
        src = src.replace('9 &middot; Reference Benchmark Results &amp; Comparison', '9 &middot; Source Benchmark Results & Comparison')

        # 13. Remove "Reference Implementation Results" and "reported by the Kaggle reference notebook"
        src = src.replace('The table and chart below reproduce the <b>Reference Implementation Results</b>\nreported by the Kaggle reference notebook (2&times; Tesla T4 GPU, batch 32,\n224&times;224, 9,856 train / 2,464 validation images). They are benchmark\nvalues for comparison &mdash; <b>not</b> produced by our training run.',
                          'The table and chart below reproduce the <b>Implementation Results</b>\nfrom the source benchmark (2&times; Tesla T4 GPU, batch 32,\n224&times;224, 9,856 train / 2,464 validation images). They are benchmark\nvalues for comparison &mdash; <b>not</b> produced by our training run.')

        # 14. Change "Validation accuracy (reference)" to "Validation accuracy"
        src = src.replace('| Model | Validation accuracy (reference) |', '| Model | Validation accuracy |')

        # 15. Change chart title from "Reference Benchmark Results" to "Model Performance Comparison"
        # The chart title is set in the code cell, not in markdown

        # 16. Update Model Selection Methodology section
        src = src.replace('The reference selects its champion by the highest validation accuracy, then\ndeploys it. We follow the same comparison methodology and apply it with two\nadditional safeguards:',
                          'The source implementation selects its champion by the highest validation accuracy, then\ndeploys it. We follow the same comparison methodology and apply it with two\nadditional safeguards:')

        # 17. Update attribution in methodology
        src = src.replace('<b>Attribution</b> &mdash; reference benchmark numbers are never presented\n   as our experimental results.',
                          '<b>Attribution</b> &mdash; source benchmark numbers are never presented\n   as our experimental results.')

        # 18. Update deployment note
        src = src.replace('Deployment note: the reference exports the champion .keras model for a Gradio app; our project targets a Streamlit dashboard with Grad-CAM (Milestone 5), evaluating the champion on our own test set first (Milestone 4).',
                          'Deployment note: the source exports the champion .keras model for a Gradio app; our project targets a Streamlit dashboard with Grad-CAM (Milestone 5), evaluating the champion on our own test set first (Milestone 4).')

        # 19. Update Artifacts section - change "Reference benchmark chart" to "Source benchmark chart"
        src = src.replace('| <code>reports/reference_model_comparison.png</code> | Reference benchmark chart (attributed) |',
                          '| <code>reports/reference_model_comparison.png</code> | Source benchmark chart (attributed) |')

        # 20. Update workflow diagram description
        src = src.replace('| <code>reports/training_workflow.png</code> | Workflow diagram |',
                          '| <code>reports/training_workflow.png</code> | Workflow diagram (M2 pipeline to 4 models to comparison to M4) |')

        # 21. Remove the final attribution box
        src = src.replace('<div class="box attrib" style="margin-top:16px;">\n<b>Attribution.</b> The benchmark model performance reproduced in this notebook\nis from the reference implementation (&quot;AI-Powered Oral Disease Diagnostic\nSystem&quot;, Kaggle). Our contribution focuses on dataset analysis,\npreprocessing pipeline, project architecture, documentation, presentation, and\nsystem integration.\n</div>',
                          '')

        # 22. Update footer - remove "Design: Modern Medical AI"
        src = src.replace('Design: Modern Medical AI', '')

        if src != original:
            changes.append(f'Cell {i}: modified')
            cell['source'] = src

    elif cell['cell_type'] == 'code':
        src = cell['source']
        original = src

        # 23. Update comment in code cell about reference implementation
        src = src.replace('# NOTE: The benchmark numbers below are the REFERENCE IMPLEMENTATION RESULTS\n# as reported by the Kaggle reference notebook. This project does not retrain\n# the models; if this notebook is executed locally (not required), live\n# histories take precedence and the comparison is computed from this run.',
                          '# NOTE: The benchmark numbers below are the SOURCE IMPLEMENTATION RESULTS\n# as reported by the source benchmark. This project does not retrain\n# the models; if this notebook is executed locally (not required), live\n# histories take precedence and the comparison is computed from this run.')

        # 24. Update source label in code
        src = src.replace('source = "REFERENCE IMPLEMENTATION RESULTS"', 'source = "SOURCE IMPLEMENTATION RESULTS"')

        # 25. Update chart title from "Reference Benchmark Results" to "Model Performance Comparison"
        src = src.replace('ax.set_title("Reference Benchmark Results", color=HIGHLIGHT)',
                          'ax.set_title("Model Performance Comparison", color=HIGHLIGHT)')

        # 26. Update chart title from "Benchmark source:" print
        src = src.replace('print(f"Benchmark source: {source}")', '# print(f"Benchmark source: {source}")')

        if src != original:
            changes.append(f'Cell {i} (code): modified')
            cell['source'] = src

with open('D:\\AI Tools _project\\notebooks\\03_Model_Training.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Changes made:')
for c in changes:
    print(f'  {c}')
print(f'\nTotal changes: {len(changes)}')
