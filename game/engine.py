def initialize_game(word):
    return {
        'word': word.lower(),
        'guessed': set(),
        'wrong': 0,
        'max_wrong': 6,
        'score': 0
    }

def process_guess(state, guess):
    guess = guess.lower().strip()
    word = state['word']

    # Full-word guess
    if len(guess) > 1 and guess.isalpha():
        if guess == word:
            state['guessed'].update(set(word))
            return "FullCorrect"
        else:
            # Deduct only 1 for wrong full-word guess
            state['wrong'] += 1
            return "FullWrong"

    # Multi-letter partial guesses (like 'hgw')
    if len(guess) > 1:
        correct_found = False
        for letter in guess:
            if letter in word:
                state['guessed'].add(letter)
                correct_found = True
            else:
                state['guessed'].add(letter)

        if correct_found:
            # If at least one correct letter was found, no penalty
            return "PartialMixed"
        else:
            # All letters wrong → only one penalty
            state['wrong'] += 1
            return "PartialWrong"

    # Single-letter guess (normal case)
    if guess in state['guessed']:
        return "Repeated"
    state['guessed'].add(guess)
    if guess in word:
        return "Correct"
    else:
        state['wrong'] += 1
        return "Wrong"

def check_win(state):
    return all(letter in state['guessed'] for letter in state['word'])

def check_loss(state):
    return state['wrong'] >= state['max_wrong']

def calculate_score(word, wrong_guesses):
    return max(0, len(word)*10 - wrong_guesses*5)
