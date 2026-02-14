"""Stone, Paper, Scissors — simple CLI game.

Features:
- Play vs computer
- Accepts `stone`/`rock`/`s`, `paper`/`p`, `scissors`/`sc`
- Best-of-N (odd) with sensible default (3)
- Input validation and option to quit or replay
"""

import random
import sys

CHOICES = ("stone", "paper", "scissors")
ALIASES = {
    # stone / rock
    "stone": "stone", "rock": "stone", "s": "stone", "st": "stone", "1": "stone",
    # paper
    "paper": "paper", "p": "paper", "2": "paper",
    # scissors
    "scissors": "scissors", "sc": "scissors", "3": "scissors",
}

WINS_AGAINST = {
    "stone": "scissors",
    "scissors": "paper",
    "paper": "stone",
}


def normalize_choice(text: str) -> str | None:
    """Normalize user input to one of the canonical choices or return None if invalid."""
    if not text:
        return None
    key = text.strip().lower()
    return ALIASES.get(key)


def get_user_choice() -> str | None:
    """Prompt until a valid choice is entered. Return None if user quits."""
    prompt = "Choose [stone(s)/paper(p)/scissors(sc)] or type 'quit' to exit: "
    while True:
        raw = input(prompt).strip().lower()
        if raw in ("quit", "exit", "q"):
            return None
        choice = normalize_choice(raw)
        if choice:
            return choice
        print("Invalid input — try again (e.g. 'stone', 's', 'paper', 'p', 'scissors', 'sc').")


def get_computer_choice() -> str:
    return random.choice(CHOICES)


def decide_winner(user: str, comp: str) -> str:
    """Return 'user', 'computer' or 'tie'."""
    if user == comp:
        return "tie"
    return "user" if WINS_AGAINST[user] == comp else "computer"


def play_match(best_of: int = 3) -> None:
    """Play a best-of-N match (N must be odd)."""
    if best_of <= 0 or best_of % 2 == 0:
        raise ValueError("best_of must be a positive odd integer")

    needed = best_of // 2 + 1
    user_score = 0
    comp_score = 0
    round_no = 0

    print(f"\nStarting best-of-{best_of} (first to {needed} wins). Ties are replayed.")

    try:
        while user_score < needed and comp_score < needed:
            round_no += 1
            print(f"\n--- Round {round_no} ---")
            user = get_user_choice()
            if user is None:
                print("Goodbye — thanks for playing!")
                return
            comp = get_computer_choice()
            result = decide_winner(user, comp)

            print(f"You chose: {user}    Computer chose: {comp}")
            if result == "tie":
                print("It's a tie — replaying the round.")
                continue

            if result == "user":
                user_score += 1
                print("You win this round ✅")
            else:
                comp_score += 1
                print("Computer wins this round ❌")

            print(f"Score — You: {user_score}  Computer: {comp_score}")

        # final outcome
        if user_score > comp_score:
            print("\n🎉 You won the match — well played!")
        else:
            print("\n🖥️ Computer won the match — better luck next time.")

    except KeyboardInterrupt:
        print("\nInterrupted — exiting.")


def main() -> None:
    print("Stone, Paper, Scissors — play vs computer")
    try:
        raw = input("Enter odd number of rounds for 'best of' (press Enter for 3): ").strip()
        if raw == "":
            best_of = 3
        else:
            try:
                best_of = int(raw)
                if best_of <= 0 or best_of % 2 == 0:
                    print("Value must be a positive odd integer — using default (3).")
                    best_of = 3
            except ValueError:
                print("Can't parse number — using default (3).")
                best_of = 3

        play_match(best_of)

        while True:
            again = input("\nPlay again? (y/N): ").strip().lower()
            if again in ("y", "yes"):
                play_match(best_of)
            else:
                print("Goodbye!")
                break

    except KeyboardInterrupt:
        print("\nInterrupted — goodbye.")


if __name__ == "__main__":
    main()
