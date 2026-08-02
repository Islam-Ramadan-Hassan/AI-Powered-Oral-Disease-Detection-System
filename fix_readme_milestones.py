path = r"D:\AI Tools _project\README.md"
with open(path, "rb") as f:
    raw = f.read()
content = raw.decode("utf-8", errors="replace")

# Update M4 status from '⏳ Next' to '✅ Complete' and fix notebook name
content = content.replace(
    "| 4 | `04_Evaluation.ipynb` — Metrics, confusion matrix | ⏳ Next |",
    "| 4 | `04_Model_Evaluation.ipynb` — Metrics, confusion matrix, test evaluation | ✅ Complete |"
)

with open(path, "wb") as f:
    f.write(content.encode("utf-8"))
print("README.md milestones updated.")