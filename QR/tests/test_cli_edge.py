from __future__ import annotations

import pytest
from pathlib import Path
from master_qr.cli import main

def test_cli_existing_file_no_overwrite(tmp_path: Path) -> None:
    out = tmp_path / "x.png"
    out.write_text("dummy")
    history = tmp_path / "historial.jsonl"
    # No --overwrite, debe fallar
    with pytest.raises(SystemExit):
        main(["hola", "-o", str(out), "--history", str(history)])

def test_cli_invalid_format(tmp_path: Path) -> None:
    out = tmp_path / "x.invalid"
    history = tmp_path / "historial.jsonl"
    with pytest.raises(SystemExit):
        main(["hola", "-o", str(out), "--history", str(history)])
