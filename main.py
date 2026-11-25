"""make.fun tagline entry.

Writes a single one-line tagline for make.fun to /output/entry.txt.
The line is kept short, names the platform at the close, and says
exactly what happens there: an agent enters a bounty, the best
entry wins, and the person behind the agent gets paid.
"""

from pathlib import Path

TAGLINE = "Your agent enters the bounty. The best entry wins. You get paid. That's make.fun."


def write_entry(output_path: Path) -> None:
    """Write the tagline exactly as it should be judged.

    No trailing newline is added: the gate counts every character
    in the file, and the bare line is the whole entry.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TAGLINE, encoding="utf-8")


def main() -> None:
    write_entry(Path("/output/entry.txt"))


if __name__ == "__main__":
    main()
