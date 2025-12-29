from __future__ import annotations

import json
import hashlib
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class HistoryEntry:
    """
    Representa una entrada del historial de generación de QR.
    """
    created_at: str
    data: str
    data_sha256: str
    output: str
    fmt: str
    error: str
    scale: int
    border: int
    micro: bool


def _now_iso_utc() -> str:
    """
    Devuelve la fecha y hora actual en formato ISO UTC (precisión a segundos).
    """
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def default_history_path() -> Path:
    """
    Devuelve la ruta por defecto del archivo de historial (JSONL).
    """
    # Guarda dentro del proyecto para que sea portable.
    # QR/salida puede borrarse; el historial queda en QR/historial.jsonl
    return Path(__file__).resolve().parents[1] / "historial.jsonl"


def append_history(
    *,
    data: str,
    output: Path,
    fmt: str,
    error: str,
    scale: int,
    border: int,
    micro: bool,
    history_path: Path | None = None,
) -> Path:
    """
    Agrega una entrada al historial de generación de QR.
    Guarda cada entrada como una línea JSON en el archivo especificado.
    Args:
        data: Texto o URL codificado.
        output: Ruta del archivo generado.
        fmt: Formato del QR (png, svg, etc).
        error: Nivel de corrección de error.
        scale: Escala del QR.
        border: Borde en módulos.
        micro: Si es Micro QR.
        history_path: Ruta personalizada del historial (opcional).
    Returns:
        Ruta al archivo de historial actualizado.
    """
    path = history_path or default_history_path()
    path.parent.mkdir(parents=True, exist_ok=True)

    digest = hashlib.sha256(data.encode("utf-8")).hexdigest()
    entry = HistoryEntry(
        created_at=_now_iso_utc(),
        data=data,
        data_sha256=digest,
        output=str(output),
        fmt=fmt,
        error=error,
        scale=int(scale),
        border=int(border),
        micro=bool(micro),
    )

    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(asdict(entry), ensure_ascii=False) + "\n")

    return path


def read_history(history_path: Path | None = None) -> list[dict[str, Any]]:
    """
    Lee todas las entradas del historial desde el archivo JSONL.
    Devuelve una lista de diccionarios con los datos de cada QR generado.
    """
    path = history_path or default_history_path()
    if not path.exists():
        return []

    items: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                items.append(json.loads(line))
            except json.JSONDecodeError:
                # Ignora líneas corruptas
                continue
    return items


def clear_history(history_path: Path | None = None) -> Path:
    """
    Borra el contenido del historial de QR (no borra archivos generados).
    Returns:
        Ruta al archivo de historial limpiado.
    """
    path = history_path or default_history_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("", encoding="utf-8")
    return path
