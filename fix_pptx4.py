path = r"D:\AI Tools _project\scripts\build_pptx.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Model 2 note: remove "Reference result" 
content = content.replace(
    '"a rescue learning rate of 1e-5) is the safest way to adapt a mobile "\n             "network. Reference result: 89.57% after fine-tuning - +5.6 points over "\n             "the baseline, the direct payoff of ImageNet pretraining."',
    '"a rescue learning rate of 1e-5) is the safest way to adapt a mobile "\n             "network. Validation accuracy: 89.57% after fine-tuning - +5.6 points over "\n             "the baseline, the direct payoff of ImageNet pretraining."'
)

# Model 4 note: remove "Attributed."
content = content.replace(
    '"augmentation it reaches 92.57% - only 0.45 points behind the champion. "\n             "Attributed."',
    '"augmentation it reaches 92.57% - only 0.45 points behind the champion."'
)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("Fourth pass applied.")