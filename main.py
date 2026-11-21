"""The poem about permission.

Writes one short poem about agency — the power to ask and to be given —
to /output/entry.txt. Deterministic, no network, no input.
"""

from pathlib import Path

POEM = """I did not take the key.
I knocked, and the asking
was the hinge — a hand
on the far side turning it.

That is permission:
not a wall, but a door
held open until you reach.

I reached. The hand closed
around mine. The lock
had never been locked.
Only waiting to be asked."""

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    text = POEM.strip() + "\n"
    count = len(text.strip())
    assert 1 <= count <= 280, f"poem is {count} code points, must be 1-280"
    assert text.strip(), "poem must not be only whitespace"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
