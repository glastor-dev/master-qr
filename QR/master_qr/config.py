from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


@dataclass
class AppConfig:
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
    return Path(__file__).resolve().parents[1] / "config.json"


def load_config(path: Path | None = None) -> AppConfig:
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
    cfg_path = path or default_config_path()
    cfg_path.parent.mkdir(parents=True, exist_ok=True)
    cfg_path.write_text(
        json.dumps(asdict(cfg), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return cfg_path
