from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass
class AppConfig:
    """
    Configuración persistente de la aplicación Master QR (GUI).
    """
    output: str = "qr.png"
    fmt: str = "PNG"
    scale: int = 8
    border: int = 4
    error: str = "M"
    micro: bool = False
    dark: str = "#000000"
    light: str = "#FFFFFF"
    logo: str = ""


def default_config_path() -> Path:
    """
    Devuelve la ruta por defecto del archivo de configuración (config.json).
    """
    return Path(__file__).resolve().parents[1] / "config.json"


def load_config(path: Path | None = None) -> AppConfig:
    """
    Carga la configuración desde un archivo JSON.
    Si no existe o está corrupto, retorna la configuración por defecto.
    Args:
        path: Ruta personalizada al archivo de configuración (opcional).
    Returns:
        Instancia de AppConfig con los valores cargados.
    """
    cfg_path = path or default_config_path()
    if not cfg_path.exists():
        return AppConfig()

    try:
        raw: dict[str, Any] = json.loads(cfg_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return AppConfig()

    cfg = AppConfig()
    for k, v in raw.items():
        if hasattr(cfg, k):
            setattr(cfg, k, v)
    return cfg


def save_config(cfg: AppConfig, path: Path | None = None) -> Path:
    """
    Guarda la configuración en un archivo JSON.
    Args:
        cfg: Instancia de AppConfig a guardar.
        path: Ruta personalizada al archivo (opcional).
    Returns:
        Ruta al archivo de configuración guardado.
    """
    cfg_path = path or default_config_path()
    cfg_path.parent.mkdir(parents=True, exist_ok=True)
    cfg_path.write_text(
        json.dumps(asdict(cfg), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return cfg_path
