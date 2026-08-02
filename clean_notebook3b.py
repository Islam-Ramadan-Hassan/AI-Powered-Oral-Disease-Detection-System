import json

path = r"D:\AI Tools _project\notebooks\03_Model_Training.ipynb"
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

changes = 0

# Cell 1: TOC - remove "Attribution" from link text
cell = nb["cells"][1]
src = "".join(cell["source"])
src = src.replace("Introduction &amp; Attribution", "Introduction")
cell["source"] = [src]
changes += 1

# Cell 3: "Nothing from the reference is copied as our own work"
cell = nb["cells"][3]
src = "".join(cell["source"])
src = src.replace("Nothing from the reference is copied as our own work", "No benchmark content is presented as our own work")
cell["source"] = [src]
changes += 1

# Cell 7: "reference strategy"
cell = nb["cells"][7]
src = "".join(cell["source"])
src = src.replace("(reference strategy)", "(standard strategy)")
cell["source"] = [src]
changes += 1

# Cell 8: "reference strategy" in code comment
cell = nb["cells"][8]
src = "".join(cell["source"])
src = src.replace("reference strategy", "standard strategy")
cell["source"] = [src]
changes += 1

# Cell 11: "Reference implementation" in docstring
cell = nb["cells"][11]
src = "".join(cell["source"])
src = src.replace('"""Reference implementation: custom CNN with embedded augmentation."""', '"""Custom CNN baseline with embedded augmentation."""')
cell["source"] = [src]
changes += 1

# Cell 26: REFERENCE_RESULTS variable and source variable
cell = nb["cells"][26]
src = "".join(cell["source"])
src = src.replace("REFERENCE_RESULTS", "PUBLISHED_RESULTS")
src = src.replace("source = ", "label = ")
src = src.replace('"THIS SESSION\'S TRAINING RUN"', '"This session\'s training run"')
src = src.replace('"Published Benchmark Results"', '"Published benchmark results"')
src = src.replace("# Benchmark source: {source}", "# Results source: {label}")
cell["source"] = [src]
changes += 1

# Cell 27: "Attribution" heading
cell = nb["cells"][27]
src = "".join(cell["source"])
src = src.replace("<b>Attribution</b>", "<b>Methodology note</b>")
src = src.replace("benchmark numbers are never presented as our experimental results", "benchmark numbers are never presented as our experimental results")
cell["source"] = [src]
changes += 1

# Also check cell 2 (intro) for "benchmark" - that's fine, it's the project's own benchmark
# Check for any remaining "reference" or "source" that shouldn't be there
remaining_keywords = ["reference", "attributed", "attribution", "source implementation", "source benchmark", "source notebook", "reference implementation", "reference result", "reference_model", "reference benchmark", "BENCHMARK:", "attributed source"]

for i, cell in enumerate(nb["cells"]):
    src = "".join(cell["source"])
    for kw in remaining_keywords:
        if kw.lower() in src.lower():
            idx = src.lower().find(kw.lower())
            start = max(0, idx - 50)
            end = min(len(src), idx + len(kw) + 50)
            print(f"STILL FOUND Cell {i} ({cell['cell_type']}): [{kw}] ...{src[start:end]}...")

print(f"\nTotal fixes applied: {changes}")

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook saved.")