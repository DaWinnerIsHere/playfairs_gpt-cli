import yaml
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "config.yaml")

def load_config(path=CONFIG_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError("No config.yaml found. Please create one and add your API keys.")
    with open(path, "r") as f:
        return yaml.safe_load(f)
