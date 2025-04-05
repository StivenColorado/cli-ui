import json
import os #to check if the file exists

def read_json(path):
    if not os.path.exists(path='data.json'):
        with open(path, 'w') as f:
            json.dump([],f)
    else:
        with open(path,'r') as f:
            data = json.load(f)

        return data

def write_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f)
