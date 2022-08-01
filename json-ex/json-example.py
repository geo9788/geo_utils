import json
from pathlib import Path

# explicit path
with open('some/path/to/json.json') as f:
    something = json.load(f)

# relative path
with open(Path(__file__).parent/'something.json') as f:
    something = json.load(f)
