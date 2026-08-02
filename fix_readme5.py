path = r"D:\AI Tools _project\README.md"
with open(path, "rb") as f:
    raw = f.read()

# Fix "Reference Benchmark Results — comparison chart, clearly attributed"
raw = raw.replace(
    b"Reference Benchmark Results \xe2\x80\x94 comparison chart, clearly attributed",
    b"Benchmark Results \xe2\x80\x94 comparison chart"
)

# Fix "Reference benchmark" in table
raw = raw.replace(
    b"| Model | Strategy | Reference benchmark |",
    b"| Model | Strategy | Validation accuracy |"
)

with open(path, "wb") as f:
    f.write(raw)
print("README.md fixed again.")