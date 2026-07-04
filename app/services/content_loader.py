import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def random_riddle():
    with open(BASE_DIR / "content" / "riddles.json", encoding="utf-8") as f:
        riddles = json.load(f)

    return random.choice(riddles)