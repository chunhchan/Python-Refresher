# echo.py


def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    tail = text[-repetitions:]  # last N characters
    lines = []

    while tail:
        lines.append(tail)
        tail = tail[1:]  # remove first char to fade

    lines.append(".")
    return "\n".join(lines)


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
