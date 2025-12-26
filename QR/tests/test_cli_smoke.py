from __future__ import annotations

from pathlib import Path

from master_qr.cli import main


def test_cli_generates_file(tmp_path: Path) -> None:
    out = tmp_path / "x.svg"
    history = tmp_path / "historial.jsonl"
    rc = main(["hola", "-o", str(out), "--history", str(history)])
    assert rc == 0
    assert out.exists()
