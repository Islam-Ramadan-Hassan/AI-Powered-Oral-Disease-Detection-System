import re

# Check README.md
with open(r"D:\AI Tools _project\README.md", "r", encoding="utf-8") as f:
    content = f.read()

print("=== README.md source labels ===")
keywords = ["attributed", "Reference result", "Attributed", "source implementation",
            "source benchmark", "source notebook", "reference benchmark", "reference result",
            "References document", "Kaggle input", "BENCHMARK:", "reference", "source"]
for kw in keywords:
    matches = [(m.start(), m.group()) for m in re.finditer(re.escape(kw), content, re.IGNORECASE)]
    if matches:
        for pos, _ in matches[:5]:
            ctx = content[max(0, pos-80):pos+len(kw)+80]
            # Replace problematic chars
            ctx = ctx.replace("\u2705", "[OK]").replace("\u274c", "[X]").replace("\u2014", "--")
            print(f"[{kw}] pos {pos}: ...{ctx}...")
            print()

print("\n=== build_train_notebook.py source labels ===")
with open(r"D:\AI Tools _project\scripts\build_train_notebook.py", "r", encoding="utf-8") as f:
    content = f.read()

for kw in keywords:
    matches = [(m.start(), m.group()) for m in re.finditer(re.escape(kw), content, re.IGNORECASE)]
    if matches:
        for pos, _ in matches[:5]:
            ctx = content[max(0, pos-80):pos+len(kw)+80]
            ctx = ctx.replace("\u2705", "[OK]").replace("\u274c", "[X]").replace("\u2014", "--")
            print(f"[{kw}] pos {pos}: ...{ctx}...")
            print()