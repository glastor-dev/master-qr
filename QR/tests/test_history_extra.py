from __future__ import annotations

import pytest
from pathlib import Path
from master_qr.history import append_history, read_history, clear_history

def test_append_history_multiple(tmp_path: Path) -> None:
    history_path = tmp_path / "historial.jsonl"
    for i in range(3):
        append_history(
            data=f"data-{i}",
            output=tmp_path / f"qr{i}.png",
            fmt="png",
            error="M",
            scale=8,
            border=4,
            micro=False,
            history_path=history_path,
        )
    items = read_history(history_path)
    assert len(items) == 3
    assert items[0]["data"].startswith("data-")

def test_clear_history(tmp_path: Path) -> None:
    history_path = tmp_path / "historial.jsonl"
    append_history(
        data="x",
        output=tmp_path / "qr.png",
        fmt="png",
        error="M",
        scale=8,
        border=4,
        micro=False,
        history_path=history_path,
    )
    clear_history(history_path)
    items = read_history(history_path)
    assert items == []

def test_read_history_corrupt_line(tmp_path: Path) -> None:
    history_path = tmp_path / "historial.jsonl"
    # Escribir línea corrupta
    with open(history_path, "w", encoding="utf-8") as f:
        f.write("{corrupt}\n")
        f.write("{}\n")
    items = read_history(history_path)
    assert isinstance(items, list)
    assert len(items) == 1
