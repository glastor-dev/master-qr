from __future__ import annotations

"""
Módulo de renderizado de códigos QR para Master QR.
Incluye funciones para guardar QR en diferentes formatos y aplicar logos.
"""
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
    """
    Genera y guarda un código QR en el archivo especificado.

    Args:
        data: Texto o URL a codificar.
        output: Ruta de salida (incluye extensión para formato).
        error: Nivel de corrección de error ('L', 'M', 'Q', 'H').
        micro: Si es True, genera un Micro QR.
        scale: Escala/tamaño del QR.
        border: Borde (quiet zone) en módulos.
        dark: Color de los módulos (hex o None).
        light: Color de fondo (hex o None).
        logo: Ruta a un logo para incrustar (solo PNG).
    Raises:
        ValueError: Si se intenta incrustar logo en un formato distinto a PNG.
    """
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
    """
    Incrusta un logo en el centro de un QR PNG.

    Args:
        qr_png: Ruta al archivo PNG del QR generado.
        logo_path: Ruta al logo (PNG/JPG).
    """
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
