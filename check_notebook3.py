import json

path = r"D:\AI Tools _project\notebooks\03_Model_Training.ipynb"
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

keywords = [
    "reference", "source", "Kaggle", "attributed", "attribution",
    "source implementation", "source benchmark", "source notebook",
    "reference implementation", "reference result", "reference_model",
    "reference benchmark", "BENCHMARK:", "attributed source",
]

for i, cell in enumerate(nb["cells"]):
    src = "".join(cell["source"])
    for kw in keywords:
        if kw.lower() in src.lower():
            idx = src.lower().find(kw.lower())
            start = max(0, idx - 40)
            end = min(len(src), idx + len(kw) + 40)
            print(f"Cell {i} ({cell['cell_type']}): [{kw}] ...{src[start:end]}...")
            print()

print("--- Done checking ---")