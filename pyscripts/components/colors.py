from enum import Enum


class ConsoleColor(Enum):
    reset = "\x1b[0m"
    # source - https://talyian.github.io/ansicolors/
    black = "\x1b[38;5;0m"
    bold_red = "\x1b[38;5;1m"
    green = "\x1b[38;5;2m"
    dark_yellow = "\x1b[38;5;3m"
    deep_blue = "\x1b[38;5;4m"
    magenta = "\x1b[38;5;5m"
    dark_cyan = "\x1b[38;5;6m"
    gray = "\x1b[38;5;7m"
    dark_gray = "\x1b[38;5;8m"
    red = "\x1b[38;5;9m"
    lime = "\x1b[38;5;10m"
    yellow = "\x1b[38;5;11m"
    blue = "\x1b[38;5;12m"
    pink = "\x1b[38;5;13m"
    cyan = "\x1b[38;5;14m"
    light_gray = "\x1b[38;5;15m"


def colorize(text, color: str) -> str:
    return f"{color}{text}{ConsoleColor.reset.value}"
