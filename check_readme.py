with open(r"D:\AI Tools _project\README.md", "rb") as f:
    raw = f.read()

# Search for the exact pattern
pattern = b"Reference Benchmark Results"
matches = []
start = 0
while True:
    idx = raw.find(pattern, start)
    if idx == -1:
        break
    matches.append(idx)
    start = idx + 1

print(f'Found "Reference Benchmark Results" at positions: {matches}')

for idx in matches:
    print(f"  At {idx}: {repr(raw[idx-10:idx+80])}")