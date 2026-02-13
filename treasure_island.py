"""Treasure Island — simple text adventure game.

Run this file and follow the prompts to find the treasure.
Features:
- Case-insensitive input with validation
- Clear win/lose messages
- Replay option
- Encapsulated in functions for reuse / testing
"""

import sys


def prompt_choice(prompt: str, choices: tuple) -> str:
    """Prompt the user until they enter a valid choice.

    - prompt: the question shown to the user
    - choices: tuple of allowed strings (case-insensitive)
    Returns the normalized chosen option (lowercase).
    """
    choices_lower = {c.lower() for c in choices}
    while True:
        answer = input(prompt).strip().lower()
        if answer in choices_lower:
            return answer
        print(f"Please enter one of: {', '.join(sorted(choices_lower))}.")


def play_round() -> bool:
    """Play one round of Treasure Island. Returns True if player wins."""
    print("\nWelcome to Treasure Island! Your mission is to find the treasure.")
    print("You're at a crossroad. Where do you want to go? (left/right)")

    choice1 = prompt_choice("Type 'left' or 'right': ", ("left", "right"))
    if choice1 == "right":
        print("You fell into a hole. Game over. 💥")
        return False

    # left path
    print("You come to a lake. There is an island in the middle of the lake.")
    print("You can 'wait' for a boat or try to 'swim' across.")

    choice2 = prompt_choice("Type 'wait' or 'swim': ", ("wait", "swim"))
    if choice2 == "swim":
        print("You were attacked by a trout. Game over. 🐟")
        return False

    # waited -> reach island
    print("You arrive at the island unharmed. There is a house with 3 doors.")
    print("One red, one yellow, and one blue. Which do you choose?")

    choice3 = prompt_choice("Choose 'red', 'yellow', or 'blue': ", ("red", "yellow", "blue"))
    if choice3 == "red":
        print("It's a room full of fire. Game over. 🔥")
        return False
    if choice3 == "blue":
        print("You enter a room of beasts. Game over. 🐉")
        return False
    if choice3 == "yellow":
        print("You found the treasure! You win! 🏆")
        return True

    # safety fallback
    print("That door doesn't exist. Game over.")
    return False


def main() -> None:
    print("=== Treasure Island ===")
    while True:
        won = play_round()
        again = prompt_choice("Play again? (yes/no): ", ("yes", "no"))
        if again == "no":
            print("Thanks for playing — goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting... goodbye!")
        sys.exit(0)
