# Fix build_train_notebook.py with exact byte matching
path = r"D:\AI Tools _project\scripts\build_train_notebook.py"
with open(path, "rb") as f:
    raw = f.read()

# Fix "reference benchmark numbers" with HTML entity
raw = raw.replace(
    b"reference benchmark numbers are never presented",
    b"benchmark numbers are never presented"
)

# Fix "attribution is provided in the References document"
raw = raw.replace(
    b"attribution is provided\nin the References document",
    b"published values are provided for comparison"
)

# Fix "external source attribution lives in the References document"
raw = raw.replace(
    b"external source attribution lives in the\n# References document",
    b"published values are used for comparison"
)

with open(path, "wb") as f:
    f.write(raw)
print("build_train_notebook.py fixed with byte matching.")