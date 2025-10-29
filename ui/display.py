def show_progress(state, ascii_art):
    progress = ''.join([l if l in state['guessed'] else '_' for l in state['word']])
    print(f"\nWord: {' '.join(progress)}")
    print(f"Guessed letters: {', '.join(sorted(state['guessed']))}")
    print(f"Remaining attempts: {state['max_wrong'] - state['wrong']}")
    print(ascii_art)
