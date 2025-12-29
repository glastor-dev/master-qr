# 📝 Changelog

Todos los cambios notables en este proyecto están documentados en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/) y este proyecto sigue el [Versionado Semántico](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### 🔜 Próximamente

- Firma digital del ejecutable con certificado Code Signing
- Instalador MSI/MSIX para Windows
- Soporte para múltiples idiomas en la interfaz
- Modo batch para generar múltiples QR desde CSV

### 🐛 Correcciones pendientes

- Mejorar rendimiento en generación de QR grandes (>1000px)

---

## [1.0.0] - 2025-12-25 🎄

### 🎉 Lanzamiento inicial

Primera versión estable de Master QR con funcionalidad completa para generación de códigos QR estáticos y dinámicos.

### ✨ Nuevas Funcionalidades

#### Interfaz Gráfica (GUI)
- **Editor visual** con Tkinter para generación intuitiva de QR
- **Vista previa en vivo** del código generado (formato PNG)
- **Personalización de colores** con selector visual y validación hexadecimal
- **Logo central** personalizable (PNG, fuerza nivel de corrección H)
- **Historial inteligente** con acciones rápidas:
  - Abrir archivo generado
  - Explorar carpeta de destino
  - Copiar ruta y contenido al portapapeles
  - Limpiar historial completo
- **Configuración persistente** que recuerda tus preferencias

#### Línea de Comandos (CLI)
- **Comando `master-qr`** para generación desde terminal
- **Exportación múltiple**: PNG, SVG, PDF, EPS, TXT
- **Scripts automatizables** para integración en workflows

#### Servidor de Redirecciones
- **Servidor local** (`master-qr-serve`) para QR "dinámicos"
- Actualiza destinos sin regenerar códigos QR

#### Distribución y Empaquetado
- **Ejecutable Windows** standalone (PyInstaller)
- **Portable ZIP** listo para usar sin instalación
- **Instalador Inno Setup** (template incluido)
- **Scripts de build** automatizados (`build_exe.ps1`, `release.ps1`)

### 📦 Infraestructura

#### Desarrollo
- **`pyproject.toml`** moderno para gestión de dependencias
- **Entry points** configurados:
  - `master-qr` → CLI
  - `master-qr-gui` → Interfaz gráfica
  - `master-qr-serve` → Servidor de redirecciones

#### Testing
- **Suite completa de tests** con pytest
- Cobertura de: render, historial, CLI, servidor
- **CI/CD** en GitHub Actions
  - Tests en Windows
  - Python 3.10, 3.11, 3.12, 3.13

### 📁 Estructura de Datos

- **Historial**: `QR/historial.jsonl` (formato JSONL para eficiencia)
- **Configuración**: `QR/config.json` (preferencias de usuario)

### 🔧 Mejoras Técnicas

- Validación de entrada con feedback visual
- Manejo robusto de errores
- Logging estructurado para debugging
- Documentación inline completa

---

## 🤝 Contribuir

Para reportar bugs o sugerir mejoras, visita [Issues](https://github.com/glastor-dev/master-qr/issues).

Para contribuir código, consulta [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📋 Convenciones de Versionado

Este proyecto usa [Versionado Semántico](https://semver.org/):

- **MAJOR** (X.0.0): Cambios incompatibles en la API
- **MINOR** (1.X.0): Nueva funcionalidad compatible hacia atrás
- **PATCH** (1.0.X): Correcciones de bugs compatibles

---

**Última actualización**: 2025-12-25  
**Mantenido por**: [@glastor-dev](https://github.com/glastor-dev)