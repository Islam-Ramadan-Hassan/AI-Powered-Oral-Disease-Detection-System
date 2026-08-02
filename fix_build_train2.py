path = r"D:\AI Tools _project\scripts\build_train_notebook.py"
with open(path, "rb") as f:
    raw = f.read()
content = raw.decode("utf-8", errors="replace")

# Fix remaining "reference benchmark numbers"
content = content.replace(
    'reference benchmark numbers are never presented as our experimental results',
    'benchmark numbers are never presented as our experimental results'
)

# Fix "References document" in first occurrence
content = content.replace(
    'attribution is provided in the References document',
    'published values are provided for comparison'
)

# Fix "external source attribution lives in the References document"
content = content.replace(
    'external source attribution lives in the References document',
    'published values are used for comparison'
)

with open(path, "wb") as f:
    f.write(content.encode("utf-8"))
print("build_train_notebook.py remaining labels fixed.")