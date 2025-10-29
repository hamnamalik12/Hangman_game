from pathlib import Path
from datetime import datetime
import json

def save_log(game_id, category, word, guesses, wrong_count, result, score, stats):
    base = Path(__file__).parent.parent / 'game_log' / f'game{game_id}'
    base.mkdir(parents=True, exist_ok=True)
    log_file = base / 'log.txt'

    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(f"Game {game_id} Log\n")
        f.write(f"Category: {category}\n")
        f.write(f"Word: {word}\n")
        f.write(f"Wrong guesses: {wrong_count}\n")
        f.write(f"Result: {result}\n")
        f.write(f"Score: {score}\n\n")
        f.write("Guesses:\n")
        for i, (g, res) in enumerate(guesses, 1):
            f.write(f"{i}. {g} -> {res}\n")
        f.write(f"\nDate & Time: {datetime.now()}\n")
        f.write(f"\nOverall Stats:\n{json.dumps(stats, indent=2)}\n")

def load_stats():
    stats_file = Path(__file__).parent.parent / 'game_log' / 'stats.json'
    if stats_file.exists():
        return json.loads(stats_file.read_text())
    return {"games_played": 0, "wins": 0, "losses": 0, "total_score": 0, "win_rate": 0, "average_score_per_game": 0}

def save_stats(stats):
    stats_file = Path(__file__).parent.parent / 'game_log' / 'stats.json'
    stats_file.parent.mkdir(parents=True, exist_ok=True)
    stats_file.write_text(json.dumps(stats, indent=2))
