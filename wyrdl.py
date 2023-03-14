# wydrl.py
import pathlib
import random
from string import ascii_letters
from rich.console import Console
from rich.theme import Theme

console = Console(width=40, theme=Theme({"warning": "red on yellow"}))

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

def get_random_word(word_list):
    """Get a random five-letter word from a list of strings.

    ## Example:
    
    >>> get_random_word(["snake", "worm", "it'll"])
    'SNAKE'
    """
    words = [
        word.upper()
        for word in word_list
        if len(word) == 5 and all(letter in ascii_letters for letter in word)
    ]

    return random.choice(words)

def show_guesses(guesses, word):
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green"
            elif letter in word:
                style = "bold white on yellow"
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")
            
        console.print("".join(styled_guess), justify="center")

def game_over(word):
    print(f"The word was {word}")

def main():
    # Pre-process
    words_path = pathlib.Path(__file__).parent / "wordlist.txt"
    words_list = words_path.read_text(encoding="utf-8").split("\n")
    word = get_random_word(words_list)
    guesses = ["_"*5] * 6

    print(word)

    # Process (main loop)
    for i in range(6):
        refresh_page(headline=f"Guess {i + 1}")
        show_guesses(guesses, word)
        
        guesses[i] = input(f"\nGuess {i + 1}: ").upper()
        if guesses[i] == word:
            break

    # Post-process
    else:
        game_over(word)

if __name__ == "__main__":
    main()
