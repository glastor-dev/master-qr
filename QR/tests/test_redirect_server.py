from __future__ import annotations

from pathlib import Path

from master_qr.redirect_server import create_app


def test_redirect_server_set_and_redirect(tmp_path: Path) -> None:
    db = tmp_path / "redirects.json"
    app = create_app(db)
    client = app.test_client()

    # Set mapping
    r = client.get("/admin/set?code=ABC&url=https://example.com")
    assert r.status_code == 200

    # Redirect
    r2 = client.get("/r/ABC", follow_redirects=False)
    assert r2.status_code == 302
    assert r2.headers["Location"] == "https://example.com"
