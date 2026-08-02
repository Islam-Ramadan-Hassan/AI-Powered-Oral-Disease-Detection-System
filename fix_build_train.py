path = r"D:\AI Tools _project\scripts\build_train_notebook.py"
with open(path, "rb") as f:
    raw = f.read()
content = raw.decode("utf-8", errors="replace")

# 1. Fix "Reference benchmark chart (attributed)"
content = content.replace(
    'reference_model_comparison.png</code> | Reference benchmark chart (attributed)',
    'benchmark_model_comparison.png</code> | Benchmark chart (published values)'
)

# 2. Fix "reference benchmark numbers are never presented"
content = content.replace(
    'reference benchmark numbers are never presented as our experimental results',
    'benchmark numbers are never presented as our experimental results'
)

# 3. Fix "attribution is provided in the References document"
content = content.replace(
    'attribution is provided in the References document',
    'published values are provided for comparison'
)

# 4. Fix "external source attribution lives in the References document"
content = content.replace(
    'external source attribution lives in the References document',
    'published values are used for comparison'
)

# 5. Fix "preprocessing references"
content = content.replace(
    'preprocessing references',
    'preprocessing pipeline'
)

# 6. Fix "no reference text is reproduced"
content = content.replace(
    'no reference text is reproduced',
    'no external text is reproduced'
)

# 7. Fix "Reference Implementation Results - validation accuracy comparison"
content = content.replace(
    'Reference Implementation Results - validation accuracy comparison',
    'Validation Accuracy Comparison'
)

# 8. Fix the UNEXECUTED comment
content = content.replace(
    'UNEXECUTED; benchmark values are presented as reported metrics without external source annotations (attribution is provided in the References document)',
    'UNEXECUTED; benchmark values are presented as published metrics for comparison'
)

# 9. Fix "external source annotations" 
content = content.replace(
    'external source annotations',
    'external annotations'
)

with open(path, "wb") as f:
    f.write(content.encode("utf-8"))

print("build_train_notebook.py source labels fixed.")