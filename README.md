# master-qr
Generador de códigos QR estáticos (un QR no “vence” por sí mismo).

## Requisitos

- Python 3.10+

## Instalación

Desde esta carpeta:

```bash
python -m pip install -r QR/requirements.txt
```

Opcional (modo proyecto instalable / scripts):

```bash
python -m pip install -e .
```

## Uso (Interfaz gráfica)

Ejecuta sin argumentos para abrir la GUI:

```bash
python QR/main.py
```

Si instalaste el proyecto:

```bash
master-qr-gui
```

## Uso (Consola / CLI)

```bash
python QR/main.py "https://ejemplo.com" -o QR/salida/mi_qr.png
python QR/main.py "TEXTO" -o QR/salida/mi_qr.svg
```

Si instalaste el proyecto:

```bash
master-qr "https://ejemplo.com" -o mi_qr.png
```

Opciones útiles:

- `--overwrite` para sobrescribir
- `--dark` / `--light` para colores (hex)
- `--logo` para incrustar un logo (solo PNG; fuerza error level H)
- `--history` para cambiar la ruta del historial

## Historial

Cada QR generado se registra automáticamente en `QR/historial.jsonl` (una línea JSON por QR).

En la GUI, el botón “Ver historial” permite abrir el archivo generado y copiar datos/rutas.

## Configuración (GUI)

La aplicación recuerda tus opciones (formato, colores, etc.) en `QR/config.json`.

## QR “dinámico” (opcional)

Esto no hace que el QR “no venza”, sino que el QR apunte a una URL intermedia que tú puedes redirigir.

1. Define un código y su destino:

```bash
python -m master_qr.redirect_server --db QR/redirects.json set MI-CODIGO https://destino.com
```

1. Inicia el servidor local:

```bash
python -m master_qr.redirect_server --db QR/redirects.json serve --host 127.0.0.1 --port 5000
```

1. Genera el QR apuntando a:
`http://127.0.0.1:5000/r/MI-CODIGO`

Nota: esto es para uso local. No lo expongas a Internet sin autenticación.

## Ejecutable Windows (opcional)

Con PyInstaller (requiere dependencias dev):

```powershell
./build_exe.ps1
```

Genera `dist/master-qr.exe`.

## Release ZIP

Para crear un ZIP listo para compartir (incluye `dist/master-qr.exe` + `README.md` + `LICENSE`):

```powershell
./release.ps1
```

Salida: `release/master-qr-<version>-win64.zip`

## Instalador (Inno Setup)

Template listo: `installer.iss`.

Pasos:

1. Genera el `.exe` (PyInstaller)
1. Abre `installer.iss` con Inno Setup y compílalo (o usa `ISCC.exe`)

Salida: `release/master-qr-setup-<version>.exe`

## Firma de ejecutable (recomendado)

Para un proyecto “pro”, firma `dist/master-qr.exe` con un certificado de Code Signing.

- Requiere un certificado (pfx) y herramientas de Windows SDK (`signtool.exe`).
- Ejemplo (ajusta rutas):

  - `signtool sign /f tu_cert.pfx /p TU_PASSWORD /tr http://timestamp.digicert.com /td sha256 /fd sha256 dist\master-qr.exe`


