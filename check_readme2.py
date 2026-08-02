with open(r"D:\AI Tools _project\README.md", "rb") as f:
    raw = f.read()

# Search for 'clearly attributed'
pattern = b"clearly attributed"
matches = []
start = 0
while True:
    idx = raw.find(pattern, start)
    if idx == -1:
        break
    matches.append(idx)
    start = idx + 1

print(f'Found "clearly attributed" at: {matches}')
for idx in matches:
    print(f"  At {idx}: {repr(raw[idx-60:idx+60])}")