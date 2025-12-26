from __future__ import annotations

from pathlib import Path

import segno
from PIL import Image


def save_qr(
    *,
    data: str,
    output: Path,
    error: str,
    micro: bool,
    scale: int,
    border: int,
    dark: str | None = None,
    light: str | None = None,
    logo: Path | None = None,
) -> None:
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)

    if logo is not None and output.suffix.lower() != ".png":
        raise ValueError("El logo solo se soporta con salida .png")

    qr = segno.make(data, error=error, micro=micro)

    save_kwargs: dict[str, object] = {
        "scale": int(scale),
        "border": int(border),
    }
    if dark:
        save_kwargs["dark"] = dark
    if light:
        save_kwargs["light"] = light

    qr.save(str(output), **save_kwargs)

    if logo is not None:
        _apply_logo_png(output, logo)


def _apply_logo_png(qr_png: Path, logo_path: Path) -> None:
    base = Image.open(qr_png).convert("RGBA")
    logo = Image.open(logo_path).convert("RGBA")

    # Escala del logo (aprox 22% del ancho del QR)
    max_w = int(base.size[0] * 0.22)
    max_h = int(base.size[1] * 0.22)

    logo.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)

    x = (base.size[0] - logo.size[0]) // 2
    y = (base.size[1] - logo.size[1]) // 2

    base.alpha_composite(logo, dest=(x, y))
    base.convert("RGB").save(qr_png)
