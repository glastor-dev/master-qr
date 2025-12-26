from __future__ import annotations

import argparse
from pathlib import Path

from .history import append_history
from .render import save_qr


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="master-qr",
        description=(
            "Genera códigos QR estáticos (no vencen por sí solos). "
            "El contenido que codifiques (texto/URL) determina su vigencia."
        ),
    )

    parser.add_argument(
        "data",
        help="Texto o URL a codificar dentro del QR (por ejemplo https://...).",
    )

    parser.add_argument(
        "-o",
        "--output",
        default="qr.png",
        help="Ruta de salida (por defecto: qr.png). La extensión define el formato.",
    )

    parser.add_argument(
        "--history",
        default=None,
        help="Ruta del archivo historial.jsonl (por defecto: QR/historial.jsonl).",
    )

    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Sobrescribe el archivo de salida si ya existe.",
    )

    parser.add_argument(
        "--scale",
        type=int,
        default=8,
        help="Escala/tamaño del QR (por defecto: 8).",
    )

    parser.add_argument(
        "--border",
        type=int,
        default=4,
        help="Borde (quiet zone) en módulos (por defecto: 4).",
    )

    parser.add_argument(
        "--error",
        choices=["L", "M", "Q", "H"],
        default="M",
        help="Nivel de corrección de error (L, M, Q, H). Por defecto: M.",
    )

    parser.add_argument(
        "--dark",
        default=None,
        help="Color de módulos (ej: #000000).",
    )

    parser.add_argument(
        "--light",
        default=None,
        help="Color de fondo (ej: #FFFFFF).",
    )

    parser.add_argument(
        "--logo",
        default=None,
        help="Ruta a un logo para incrustar (solo salida PNG).",
    )

    parser.add_argument(
        "--micro",
        action="store_true",
        help="Genera Micro QR (si es posible).",
    )

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if out_path.exists() and not args.overwrite:
        parser.error(
            "El archivo de salida ya existe. Usa --overwrite para sobrescribirlo."
        )

    suffix = out_path.suffix.lower()
    if suffix not in {".png", ".svg", ".pdf", ".eps", ".txt"}:
        parser.error("Formato no soportado. Usa extensión .png, .svg, .pdf, .eps o .txt")

    logo_path = Path(args.logo) if args.logo else None

    # Para logos, conviene usar corrección alta.
    error = args.error
    if logo_path is not None and error != "H":
        error = "H"

    save_qr(
        data=args.data,
        output=out_path,
        error=error,
        micro=args.micro,
        scale=args.scale,
        border=args.border,
        dark=args.dark,
        light=args.light,
        logo=logo_path,
    )

    append_history(
        data=args.data,
        output=out_path,
        fmt=suffix.lstrip("."),
        error=error,
        scale=args.scale,
        border=args.border,
        micro=args.micro,
        history_path=Path(args.history) if args.history else None,
    )

    print(f"OK: generado {out_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
