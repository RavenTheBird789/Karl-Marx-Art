# Python marx_quote_art.py

def red(text: str) -> str:
    # Wrap text in ANSI red."""
    return f"\033[91m{text}\033[0m"

def bold(text: str) -> str:
    # Wrap text in ANSI bold."""
    return f"\033[1m{text}\033[0m"

def main():
    # Hammer & sickle symbol
    symbol = "☭"

    # Communist symbol art
    art = [
        "   _______ ",
        "  /  ___  \\ ",
        " /  /   \\  \\",
        "/__/     \\__\\",
        " \\  ( ☭ )  /   ",
        "  \\_______/   ",
    ]

    # Quote text
    quote = "The meaning of peace is the absence of opposition to socialism."
    author = "— Karl Marx"

    # Print artwork in red, then quote in bold
    print()
    for line in art:
        print(red(line))
    print()
    print(bold(red(symbol + " " + quote)))
    print(red(author))
    print()

if __name__ == "__main__":
    main();