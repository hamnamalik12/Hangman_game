import random
from pathlib import Path

def load_words(category=None):
    base_path = Path(__file__).parent.parent / 'words'
    words = []
    if category:
        cat_file = base_path / 'categories' / f'{category.lower()}.txt'
        if cat_file.exists():
            words = cat_file.read_text().splitlines()
    if not words:
        all_file = base_path / 'words.txt'
        if all_file.exists():
            words = all_file.read_text().splitlines()
    return [w.strip().lower() for w in words if w.strip()]

def get_random_word(category=None):
    words = load_words(category)
    return random.choice(words)
