# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/),
y este proyecto adhiere al [Versionado Semántico](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Pendiente

- (pendiente) Firma de ejecutable con certificado de Code Signing.
- (pendiente) Instalador (MSI/MSIX o Inno Setup en máquina con tooling).

## [1.0.0] - 2025-12-25

### Added

- Generador de QR estático con interfaz gráfica (Tkinter).
- CLI para generar QR por consola.
- Exportación por extensión: PNG, SVG, PDF, EPS, TXT.
- Vista previa en la GUI (solo PNG).
- Personalización de colores (dark/light) con validación hex.
- Logo incrustado en el centro (solo PNG; fuerza nivel de error H).
- Historial automático de generación en `QR/historial.jsonl` (JSONL) con acciones desde la GUI:
  - Abrir archivo
  - Abrir carpeta
  - Copiar ruta y contenido
  - Limpiar historial
- Configuración persistente de la GUI en `QR/config.json`.
- Servidor local opcional de redirecciones para “QR dinámico”.
- Empaquetado de proyecto con `pyproject.toml` y scripts:
  - `master-qr` (CLI)
  - `master-qr-gui` (GUI)
  - `master-qr-serve` (redirect server)
- Build de ejecutable Windows con PyInstaller (`build_exe.ps1`).
- Empaquetado portable para distribución en ZIP (`release.ps1`).
- Template de instalador Inno Setup (`installer.iss`) para compilar donde exista Inno Setup.
- Tests automatizados (pytest) para render/historial/CLI/redirect server.
- CI en GitHub Actions para ejecutar tests en Windows (Python 3.10–3.13).

---

Este CHANGELOG se actualiza manualmente. Para contribuciones, sigue las guías de [Versionado Semántico](https://semver.org/).
