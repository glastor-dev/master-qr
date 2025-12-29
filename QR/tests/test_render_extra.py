from __future__ import annotations

import pytest
from pathlib import Path
from master_qr.render import save_qr


def test_save_qr_svg(tmp_path: Path) -> None:
    out = tmp_path / "a.svg"
    save_qr(
        data="svg-test",
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
    assert out.suffix == ".svg"
    assert out.stat().st_size > 0

def test_save_qr_logo_png(tmp_path: Path) -> None:
    out = tmp_path / "b.png"
    logo = tmp_path / "logo.png"
    # Crear un logo PNG simple
    from PIL import Image
    img = Image.new("RGBA", (32, 32), (255, 0, 0, 255))
    img.save(logo)
    save_qr(
        data="logo-test",
        output=out,
        error="H",
        micro=False,
        scale=5,
        border=2,
        dark="#000000",
        light="#FFFFFF",
        logo=logo,
    )
    assert out.exists()
    assert out.suffix == ".png"
    assert out.stat().st_size > 0

def test_save_qr_logo_non_png(tmp_path: Path):
    out = tmp_path / "c.svg"
    logo = tmp_path / "logo.png"
    from PIL import Image
    img = Image.new("RGBA", (32, 32), (0, 255, 0, 255))
    img.save(logo)
    with pytest.raises(ValueError):
        save_qr(
            data="fail-logo",
            output=out,
            error="H",
            micro=False,
            scale=5,
            border=2,
            dark="#000000",
            light="#FFFFFF",
            logo=logo,
        )
