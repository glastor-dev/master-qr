from __future__ import annotations

import sys
from pathlib import Path

# Permite importar master_qr sin instalar el paquete.
ROOT = Path(__file__).resolve().parents[2]
QR_DIR = ROOT / "QR"
if str(QR_DIR) not in sys.path:
    sys.path.insert(0, str(QR_DIR))
