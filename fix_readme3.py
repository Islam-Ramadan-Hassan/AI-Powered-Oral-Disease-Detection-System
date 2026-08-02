# Fix README.md
path = r"D:\AI Tools _project\README.md"
with open(path, "rb") as f:
    raw = f.read()
content = raw.decode("utf-8", errors="replace")

# Fix "Reference Benchmark Results -- comparison chart, clearly attributed"
content = content.replace(
    "Reference Benchmark Results \u2014 comparison chart, clearly attributed",
    "Benchmark Results \u2014 comparison chart"
)

# Fix "The benchmark model performance is reproduced from the source implementation"
content = content.replace(
    "The benchmark model performance is reproduced from the source implementation",
    "The benchmark model performance is reproduced from the training implementation"
)

# Fix "Reference benchmark" in table (| Model | Strategy | Reference benchmark |)
content = content.replace(
    "| Model | Strategy | Reference benchmark |",
    "| Model | Strategy | Validation accuracy |"
)

with open(path, "wb") as f:
    f.write(content.encode("utf-8"))
print("README.md fixed.")