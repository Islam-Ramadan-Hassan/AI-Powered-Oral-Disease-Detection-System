# Fix README.md with exact byte matching
path = r"D:\AI Tools _project\README.md"
with open(path, "rb") as f:
    raw = f.read()

# Fix "Reference Benchmark Results — comparison chart, clearly attributed" (em-dash = \xe2\x80\x94)
raw = raw.replace(
    b"Reference Benchmark Results \xe2\x80\x94 comparison chart, clearly attributed",
    b"Benchmark Results \xe2\x80\x94 comparison chart"
)

# Fix "source implementation"
raw = raw.replace(
    b"source implementation",
    b"training implementation"
)

# Fix "Reference benchmark" in table header
raw = raw.replace(
    b"| Model | Strategy | Reference benchmark |",
    b"| Model | Strategy | Validation accuracy |"
)

with open(path, "wb") as f:
    f.write(raw)
print("README.md fixed with byte matching.")