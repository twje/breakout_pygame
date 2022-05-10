import json
from json.decoder import JSONDecodeError
from pathlib import Path


class Preference:
    def __init__(self, store_name):
        self.preferences = {}
        self.store_name = f"{store_name}.json"
        self.create_store()

    def create_store(self):
        filepath = Path(self.store_name)
        filepath.touch(exist_ok=True)
        self.load()

    def add_preference(self, key, value):
        self.preferences[key] = value

    def flush(self):
        with open(self.store_name, "w") as fp:
            fp.write(json.dumps(self.preferences))

    def load(self):
        with open(self.store_name, "r") as fp:
            content = fp.read()
            if content == "":
                self.preferences = {}
            else:
                self.preferences = json.load(fp)

    def get_preference(self, key, default=None):
        return self.preferences.get(key, default)
