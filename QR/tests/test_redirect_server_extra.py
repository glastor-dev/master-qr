from __future__ import annotations

import pytest
from pathlib import Path
from master_qr.redirect_server import create_app

def test_redirect_server_not_found(tmp_path: Path) -> None:
    db = tmp_path / "redirects.json"
    app = create_app(db)
    client = app.test_client()
    r = client.get("/r/NOPE", follow_redirects=False)
    assert r.status_code == 404

def test_redirect_server_set_missing_params(tmp_path: Path) -> None:
    db = tmp_path / "redirects.json"
    app = create_app(db)
    client = app.test_client()
    r = client.get("/admin/set?code=ONLY")
    assert r.status_code == 400
    r2 = client.get("/admin/set?url=https://x.com")
    assert r2.status_code == 400

def test_redirect_server_overwrite(tmp_path: Path) -> None:
    db = tmp_path / "redirects.json"
    app = create_app(db)
    client = app.test_client()
    # Set primero
    r = client.get("/admin/set?code=Z&url=https://a.com")
    assert r.status_code == 200
    # Sobrescribir
    r2 = client.get("/admin/set?code=Z&url=https://b.com")
    assert r2.status_code == 200
    # Redirige a la nueva URL
    r3 = client.get("/r/Z", follow_redirects=False)
    assert r3.status_code == 302
    assert r3.headers["Location"] == "https://b.com"
