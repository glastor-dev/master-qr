
from __future__ import annotations
import argparse
import json
from pathlib import Path
from flask import Flask, abort, redirect, request

"""
Servidor de redirección para QR dinámico en Master QR.
Permite mapear códigos a URLs y redirigir mediante Flask.
"""

def _default_db_path() -> Path:
    """
    Devuelve la ruta por defecto para el archivo de base de datos de redirecciones.
    """
    return Path(__file__).resolve().parents[1] / "redirects.json"


def _load_db(path: Path) -> dict[str, str]:
    """
    Carga la base de datos de redirecciones desde un archivo JSON.
    Devuelve un diccionario código→URL. Si el archivo no existe o está corrupto, retorna vacío.
    """
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


    """
    Guarda el diccionario de redirecciones en un archivo JSON.
    """
def _save_db(path: Path, db: dict[str, str]) -> None:
    """
    Guarda el diccionario de redirecciones en un archivo JSON.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(db, ensure_ascii=False, indent=2), encoding="utf-8")


def create_app(db_path: Path, admin_token: str | None = None) -> Flask:
    """
    Crea una aplicación Flask para servir y administrar redirecciones QR dinámicas.
    Args:
        db_path: Ruta al archivo de base de datos de redirecciones.
        admin_token: Token requerido para /admin/set (opcional).
    Returns:
        Instancia de Flask lista para ejecutar.
    """
    app = Flask(__name__)

    @app.get("/r/<code>")
    def r(code: str):
        """
        Endpoint principal de redirección: /r/<code>.
        Busca el código en la base y redirige a la URL asociada.
        """
        db = _load_db(db_path)
        url = db.get(code)
        if not url:
            abort(404)
        return redirect(url, code=302)

    @app.get("/admin/set")
    def admin_set():
        """
        Endpoint de administración local para definir/actualizar códigos.
        Requiere autenticación por token si se configura.
        """
        # Solo para uso local. No expongas esto en Internet sin auth.
        if admin_token:
            token = request.args.get("token") or request.headers.get("X-Admin-Token")
            if token != admin_token:
                abort(401, description="Token inválido o ausente")
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
    """
    Construye el parser de argumentos para la CLI del servidor de redirección.
    """
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
    serve.add_argument("--admin-token", default=None, help="Token requerido para /admin/set (opcional)")
    setc = sub.add_parser("set", help="Define/actualiza un código")
    setc.add_argument("code")
    setc.add_argument("url")
    sub.add_parser("list", help="Lista el mapa actual")
    return p


def main(argv: list[str] | None = None) -> int:
    """
    Punto de entrada principal para la CLI del servidor de redirección.
    Permite definir códigos, listar el mapa o iniciar el servidor Flask.
    """
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
        app = create_app(db_path, admin_token=getattr(args, "admin_token", None))
        print(f"DB: {db_path.resolve()}")
        print(f"Ejemplo QR dinámico: http://{args.host}:{args.port}/r/MI-CODIGO")
        if getattr(args, "admin_token", None):
            print("/admin/set requiere token. Usa ?token=TU_TOKEN o header X-Admin-Token.")
        app.run(host=args.host, port=args.port, debug=False)
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
