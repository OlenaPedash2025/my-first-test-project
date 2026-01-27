import json
import os  


script_dir = os.path.dirname(os.path.abspath(__file__)) 

file_path = os.path.join(script_dir, '..', 'resources', 'exhibit.json')

with open(file_path, 'r', encoding='utf-8') as file:
    exhibit = json.load(file)
    print(exhibit['title'])