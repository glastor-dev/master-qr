from __future__ import annotations

from pathlib import Path

from master_qr.render import save_qr


def test_save_qr_png(tmp_path: Path) -> None:
    out = tmp_path / "a.png"
    save_qr(
        data="test",
        output=out,
        error="M",
        micro=False,
        scale=3,
        border=2,
        dark="#000000",
        light="#FFFFFF",
        logo=None,
    )
    assert out.exists()
    assert out.stat().st_size > 0
