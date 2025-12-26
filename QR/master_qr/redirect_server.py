from __future__ import annotations

import argparse
import json
from pathlib import Path

from flask import Flask, abort, redirect, request


def _default_db_path() -> Path:
    return Path(__file__).resolve().parents[1] / "redirects.json"


def _load_db(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _save_db(path: Path, db: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")


def create_app(db_path: Path) -> Flask:
    app = Flask(__name__)

    @app.get("/r/<code>")
    def r(code: str):
        db = _load_db(db_path)
        url = db.get(code)
        if not url:
            abort(404)
        return redirect(url, code=302)

    @app.get("/admin/set")
    def admin_set():
        # Solo para uso local. No expongas esto en Internet sin auth.
        code = request.args.get("code", "").strip()
        url = request.args.get("url", "").strip()
        if not code or not url:
            abort(400)
        db = _load_db(db_path)
        db[code] = url
        _save_db(db_path, db)
        return {"ok": True, "code": code, "url": url}

    return app


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="master-qr-serve",
        description=(
            "Servidor local opcional para 'QR dinámico': el QR apunta a /r/<code> y "
            "tú puedes cambiar el destino en redirects.json."
        ),
    )

    p.add_argument(
        "--db",
        default=str(_default_db_path()),
        help="Ruta del archivo redirects.json (por defecto dentro de QR/).",
    )

    sub = p.add_subparsers(dest="cmd", required=True)

    serve = sub.add_parser("serve", help="Inicia el servidor de redirecciones")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=5000)

    setc = sub.add_parser("set", help="Define/actualiza un código")
    setc.add_argument("code")
    setc.add_argument("url")

    sub.add_parser("list", help="Lista el mapa actual")

    return p


def main(argv: list[str] | None = None) -> int:
    p = _build_parser()
    args = p.parse_args(argv)

    db_path = Path(args.db)

    if args.cmd == "set":
        db = _load_db(db_path)
        db[args.code] = args.url
        _save_db(db_path, db)
        print(f"OK: {args.code} -> {args.url}")
        print(f"DB: {db_path.resolve()}")
        return 0

    if args.cmd == "list":
        db = _load_db(db_path)
        for k in sorted(db.keys()):
            print(f"{k} -> {db[k]}")
        print(f"DB: {db_path.resolve()}")
        return 0

    if args.cmd == "serve":
        app = create_app(db_path)
        print(f"DB: {db_path.resolve()}")
        print(f"Ejemplo QR dinámico: http://{args.host}:{args.port}/r/MI-CODIGO")
        app.run(host=args.host, port=args.port, debug=False)
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
