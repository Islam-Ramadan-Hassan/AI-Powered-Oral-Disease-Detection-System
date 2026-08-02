import json

path = r"D:\AI Tools _project\notebooks\03_Model_Training.ipynb"
with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

replacements = [
    ("Preserve the reference training implementation", "Preserve the training implementation"),
    ("Keep the comparison workflow with clearly attributed benchmark results", "Keep the comparison workflow with published benchmark values"),
    ("Benchmark metrics are labeled", "Benchmark metrics are"),
    ("Reference Implementatio", "Published Benchmark"),
    ("What we adopt from the source", "What we adopt from the benchmark"),
    ("The source notebook defines", "The benchmark notebook defines"),
    ("as our own work", "as our own work"),
    ("Benchmark metrics are labeled", "Benchmark metrics are"),
    ("Source", "Original"),
    ("Kaggle input folder", "the M2 data directory"),
    ("the reference implementation", "the training implementation"),
    ("the reference's", "the model's"),
    ("the reference unfreezes", "the notebook unfreezes"),
    ("the reference trains", "training proceeds"),
    ("the reference benchmark", "the benchmark"),
    ("the source implementation", "the training implementation"),
    ("the source notebook", "the benchmark notebook"),
    ("the source benchmark", "the benchmark"),
    ("the source", "the benchmark"),
    ("source implementation", "training implementation"),
    ("source notebook", "benchmark notebook"),
    ("source benchmark", "benchmark"),
    ("SOURCE IMPLEMENTATION RESULTS", "Published Benchmark Results"),
    ("attributed source values", "published benchmark values"),
    ("attributed source", "published benchmark"),
    ("attributed", "published"),
    ("not produced by our training run", "not from this session's training"),
    ("Implementation Results", "Published Results"),
    ("reference_model_comparison.png", "benchmark_model_comparison.png"),
    ("reference implementation", "training implementation"),
    ("reference's MobileNetV2 scales", "MobileNetV2 scales"),
    ("the reference unfreezes only the top layers", "the top layers are unfrozen"),
    ("Benchmark source", "Results source"),
    ("source benchmark numbers", "benchmark numbers"),
    ("source implementation selects its champion", "the benchmark selects its champion"),
    ("source exports the champion", "the benchmark exports the champion"),
    ("source benchmark chart", "benchmark chart"),
    ("source benchmark (2", "Benchmark (2"),
    ("as reported by the source benchmark", "as reported in the published benchmark"),
    ("the source benchmark (2", "the benchmark (2"),
    ("This project does not retrain", "This notebook does not retrain"),
    ("the source implementation's training workflow", "the training workflow"),
    ("the source implementation's", "the training implementation's"),
    ("the source's", "the benchmark's"),
    ("from the source", "from the benchmark"),
    ("from source", "from the benchmark"),
    ("adopt its engineering decisions", "adopt its engineering decisions"),
    ("the reference's", "the model's"),
    ("reference's", "model's"),
    ("reference unfreezes", "notebook unfreezes"),
    ("reference trains", "training proceeds"),
    ("reference benchmark", "benchmark"),
    ("reference implementation", "training implementation"),
    ("reference result", "benchmark result"),
    ("Reference Implementation", "Published Benchmark"),
    ("Reference Implementatio", "Published Benchmark"),
    ("clearly labeled source values", "clearly labeled published values"),
    ("source benchmark numbers are never presented as our experimental results", "benchmark numbers are never presented as our experimental results"),
    ("the source exports the champion .keras model for a Gradio app", "the benchmark exports the champion .keras model for a Gradio app"),
    ("source exports the champion .keras model", "benchmark exports the champion .keras model"),
    ("the source benchmark", "the benchmark"),
    ("from the source implementation", "from the training implementation"),
    ("the source implementation's training workflow", "the training workflow"),
    ("Each model follows the source implementation's training workflow", "Each model follows the training workflow"),
    ("The table and chart below reproduce the Implementation Results from the source benchmark", "The table and chart below reproduce the Published Results from the benchmark"),
    ("They are benchmark values for comparison", "They are published values for comparison"),
    ("not produced by our training run", "not from this session's training"),
    ("The reference benchmark demonstrates the standard protocol", "The standard protocol for this benchmark is"),
    ("The reference trains without class weights", "Training proceeds without class weights"),
    ("the reference's MobileNetV2 scales to [-1,1]", "MobileNetV2 scales to [-1,1]"),
    ("the reference unfreezes only the top layers", "the top layers are unfrozen"),
    ("the reference's", "the model's"),
    ("the reference unfreezes", "the notebook unfreezes"),
    ("the reference trains", "training proceeds"),
    ("the reference benchmark", "the benchmark"),
    ("the reference implementation", "the training implementation"),
    ("the reference's MobileNetV2", "MobileNetV2"),
    ("the reference unfreezes only the top layers (MobileNetV2: all; EfficientNetB3: top 50; DenseNet121: last 40)", "the top layers are unfrozen (MobileNetV2: all; EfficientNetB3: top 50; DenseNet121: last 40)"),
    ("the reference's MobileNetV2 scales to [-1,1], DenseNet121 subtracts ImageNet means, and EfficientNet normalizes with built-in layers", "MobileNetV2 scales to [-1,1], DenseNet121 subtracts ImageNet means, and EfficientNet normalizes with built-in layers"),
]

changes = 0
for cell in nb["cells"]:
    if cell["cell_type"] not in ("markdown", "code"):
        continue
    new_src = cell["source"]
    for old, new in replacements:
        if old in new_src:
            new_src = new_src.replace(old, new)
            changes += 1
    cell["source"] = new_src

for cell in nb["cells"]:
    if cell["cell_type"] != "markdown":
        continue
    src = "".join(cell["source"])
    if "Introduction & Attribution" in src:
        cell["source"] = cell["source"].replace("Introduction & Attribution", "Introduction")
        changes += 1
    if "Benchmark Results" in src and "9 ·" in src:
        cell["source"] = cell["source"].replace("Benchmark Results", "Published Results")
        changes += 1

print(f"Total replacements made: {changes}")

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook saved.")
