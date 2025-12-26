from __future__ import annotations

import json
from pathlib import Path

from master_qr.history import append_history, read_history


def test_append_and_read_history(tmp_path: Path) -> None:
    history_path = tmp_path / "historial.jsonl"
    out = tmp_path / "qr.png"

    append_history(
        data="hola",
        output=out,
        fmt="png",
        error="M",
        scale=8,
        border=4,
        micro=False,
        history_path=history_path,
    )

    items = read_history(history_path)
    assert len(items) == 1
    assert items[0]["data"] == "hola"
    assert "data_sha256" in items[0]
    assert items[0]["fmt"] == "png"

    # Verifica que sea JSON por línea.
    line = history_path.read_text(encoding="utf-8").strip().splitlines()[0]
    json.loads(line)
