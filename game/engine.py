def initialize_game(word):
    return {
        'word': word.lower(),
        'guessed': set(),
        'wrong': 0,
        'max_wrong': 6,
        'score': 0
    }

def process_guess(state, guess):
    guess = guess.lower()
    if guess in state['guessed']:
        return "Repeated"
    state['guessed'].add(guess)
    if guess in state['word']:
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
