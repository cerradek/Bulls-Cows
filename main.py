import random


def print_intro() -> None:
    """Print the welcome message and game rules."""
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 47)


def generate_secret() -> str:
    """Generate a 4-digit secret number with unique digits."""
    digits = list("0123456789")
    first_digit = random.choice(digits[1:])
    digits.remove(first_digit)
    other_digits = random.sample(digits, 3)
    return first_digit + "".join(other_digits)


def validate_guess(guess: str) -> list[str]:
    """Validate user's guess and return a list of error messages."""
    errors = []

    if len(guess) != 4:
        errors.append("The number must have exactly 4 digits.")
    if not guess.isdigit():
        errors.append("The number must contain digits only.")
    if guess.startswith("0"):
        errors.append("The number must not start with 0.")
    if len(set(guess)) != len(guess):
        errors.append("The number must not contain duplicate digits.")

    return errors


def count_bulls(secret: str, guess: str) -> int:
    """Count bulls: correct digit in the correct position."""
    return sum(secret[i] == guess[i] for i in range(4))


def count_cows(secret: str, guess: str, bulls: int) -> int:
    """Count cows: correct digit in the wrong position."""
    matches = sum(digit in secret for digit in guess)
    return matches - bulls


def pluralize(count: int, singular: str, plural: str) -> str:
    """Return singular or plural word based on count."""
    if count == 1:
        return singular
    return plural


def evaluate_guess(secret: str, guess: str) -> tuple[int, int]:
    """Return number of bulls and cows for the given guess."""
    bulls = count_bulls(secret, guess)
    cows = count_cows(secret, guess, bulls)
    return bulls, cows


def get_valid_guess() -> str:
    """Ask user for a valid 4-digit guess."""
    while True:
        guess = input("Enter a number:\n>>> ").strip()
        errors = validate_guess(guess)

        if not errors:
            return guess

        print("-" * 47)
        for error in errors:
            print(error)
        print("-" * 47)


def main() -> None:
    """Run the Bulls and Cows game."""
    print_intro()
    secret = generate_secret()
    attempts = 0

    while True:
        guess = get_valid_guess()
        attempts += 1
        bulls, cows = evaluate_guess(secret, guess)

        print(
            f"{bulls} {pluralize(bulls, 'bull', 'bulls')}, "
            f"{cows} {pluralize(cows, 'cow', 'cows')}"
        )
        print("-" * 47)

        if guess == secret:
            print("Correct, you've guessed the right number!")
            print(f"You guessed it in {attempts} attempts.")
            break


if __name__ == "__main__":
    main()