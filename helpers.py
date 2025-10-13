import json, os

DATA_DIR = 'data'
os.makedirs(DATA_DIR, exist_ok=True)

def read_json(name):
    path = os.path.join(DATA_DIR, name)
    if not os.path.exists(path):
        return {}
    with open(path, 'r') as f:
        try:
            return json.load(f)
        except Exception:
            return {}

def write_json(name, obj):
    path = os.path.join(DATA_DIR, name)
    with open(path, 'w') as f:
        json.dump(obj, f, indent=2)