from game.wordlist import get_random_word
from game.engine import initialize_game, process_guess, check_win, check_loss, calculate_score
from game.ascii_art import get_stage
from ui.display import show_progress
from game.logger import save_log, load_stats, save_stats
from pathlib import Path

def main():
    print("=== Welcome to Hangman ===")
    categories = ["Animals", "Countries", "cities", "entertainment","food","fruits","games","names","science","vegetables"]
    print("Available categories:", ", ".join(categories))
    category = input("Choose a category or press Enter for random: ").strip().title()

    word = get_random_word(category if category in categories else None)
    state = initialize_game(word)
    stats = load_stats()
    game_id = stats["games_played"] + 1
    guesses = []

    print(f"\nNew word selected (length: {len(word)})")

    while True:
        show_progress(state, get_stage(state['wrong']))
        guess = input("\nEnter a letter (or type 'quit' to exit): ").lower().strip()
        if guess == "quit":
            print("Exiting game...")
            break
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter a single letter.")
            continue

        result = process_guess(state, guess)
        guesses.append((guess, result))

        if result == "Correct":
            print(f" Correct! '{guess}' is in the word.")
        elif result == "Wrong":
            print(f" Wrong! '{guess}' is not in the word.")
        else:
            print(f" You already guessed '{guess}'.")

        if check_win(state):
            score = calculate_score(state['word'], state['wrong'])
            print(f"\n You win! The word was: {state['word'].upper()}")
            print(f"Points earned: {score}")
            stats["wins"] += 1
            stats["total_score"] += score
            result = "Win"
            break

        if check_loss(state):
            # Show the final (complete) hangman drawing
            print("\n" + get_stage(state['wrong']))
            print("\n GAME OVER ")
            print("You lose! The hangman is complete.")
            print(f"The correct word was: {state['word'].upper()}")
            score = 0
            stats["losses"] += 1
            result = "Loss"
            break

    stats["games_played"] += 1
    stats["win_rate"] = round((stats["wins"] / stats["games_played"]) * 100, 2)
    stats["average_score_per_game"] = round(stats["total_score"] / stats["games_played"], 2)

    save_stats(stats)
    save_log(game_id, category, state['word'], guesses, state['wrong'], result, score, stats)

    print("\n Game Summary:")
    print(f"Games played: {stats['games_played']} | Wins: {stats['wins']} | Losses: {stats['losses']}")
    print(f"Win rate: {stats['win_rate']}% | Total score: {stats['total_score']}")

if __name__ == "__main__":
    main()
