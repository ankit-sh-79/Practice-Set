"""Simple command-line calculator."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def read_number(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Enter a valid number.")


def read_operation() -> str:
    valid_ops = {"+", "-", "*", "/", "c", "q"}
    while True:
        op = input("Operation (+, -, *, /, c=clear, q=quit): ").strip().lower()
        if op in valid_ops:
            return op
        print("Choose a valid operation.")


def calculate(a: float, op: str, b: float) -> float:
    if op == "+":
        return add(a, b)
    if op == "-":
        return subtract(a, b)
    if op == "*":
        return multiply(a, b)
    if op == "/":
        return divide(a, b)
    raise ValueError("Unsupported operation.")


def main() -> None:
    print("Simple Calculator")
    current = read_number("First number: ")

    while True:
        op = read_operation()
        if op == "q":
            print("Goodbye.")
            return
        if op == "c":
            current = read_number("First number: ")
            continue

        next_value = read_number("Next number: ")
        try:
            current = calculate(current, op, next_value)
        except ZeroDivisionError as exc:
            print(exc)
            continue

        print(f"Result: {current}")


if __name__ == "__main__":
    main()
