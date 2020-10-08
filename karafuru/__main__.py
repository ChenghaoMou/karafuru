# type: ignore[attr-defined]
import colorsys

import typer
from karafuru import COLORS
from rich.console import Console

app = typer.Typer(
    name="colors",
    help="Traditional Chinese colors in your terminal",
    add_completion=False,
)
console = Console()


@app.command()
def get(base: str = typer.Option("red", help="Base color family")):
    for family in COLORS:
        if family["name"] == base or base == "all":
            for color in sorted(family["colors"], key=lambda x: x["hex"]):
                R, G, B = tuple(
                    int(color["hex"][1:][i : i + 2], 16) for i in (0, 2, 4)
                )
                luminance = (0.299 * R + 0.587 * G + 0.114 * B) / 255
                if luminance > 0.5:
                    font_color = "black"
                else:
                    font_color = "white"

                console.print(
                    f"{color['hex']:>10} {color['name']:<10}",
                    justify="left",
                    style=f"{font_color} on {color['hex']}",
                    width=20,
                    highlight=False,
                )


if __name__ == "__main__":
    app()
