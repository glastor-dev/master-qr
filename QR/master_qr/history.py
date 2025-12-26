from __future__ import annotations

import json
import hashlib
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class HistoryEntry:
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
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def default_history_path() -> Path:
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
    path = history_path or default_history_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("", encoding="utf-8")
    return path
