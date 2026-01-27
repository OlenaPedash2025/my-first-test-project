import json
import yaml
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent / "resources"
json_file = base_dir / "exhibit.json"
yaml_file = base_dir / "exhibit.yaml"


with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)


with open(yaml_file, 'w', encoding='utf-8') as f:
   
    yaml.dump(data, f, allow_unicode=True, default_flow_style=False)

print(f"Success! Data converted to {yaml_file.name}")