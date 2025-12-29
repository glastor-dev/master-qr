"""
Módulo de internacionalización simple para Master QR.
Permite definir mensajes en varios idiomas y seleccionarlos dinámicamente.
"""

LANGS = {
    "es": {
        "app_title": "Master QR",
        "ready": "Listo",
        "choose_output": "Elegir...",
        "choose_logo": "Elegir...",
        "save_as": "Guardar QR como...",
        "missing_content": "Falta contenido",
        "enter_text_url": "Ingresa un texto o URL.",
        "preview_only_png": "La vista previa solo aplica a PNG.",
        "preview_updated": "Vista previa actualizada",
        "error_preview": "Error en vista previa",
        "overwrite": "Sobrescribir",
        "file_exists": "El archivo ya existe. ¿Deseas sobrescribirlo?",
        "cancelled": "Cancelado",
        "format_not_supported": "Formato no soportado",
        "use_png_svg_pdf_eps_txt": "Usa extensión .png, .svg, .pdf, .eps o .txt.",
        "logo_only_png": "El logo solo se soporta con salida PNG.",
        "color": "Color",
        "error_generate": "Error al generar",
        "generated": "Generado: {out_path}",
        "ok": "OK",
        "qr_generated_in": "QR generado en:\n{out_path}",
        "history": "Historial",
        "no_history": "Aún no hay historial.\n\nArchivo: {path}",
        "open_file": "Abrir archivo",
        "open_folder": "Abrir carpeta",
        "copy_path": "Copiar ruta",
        "copy_content": "Copiar contenido",
        "clear": "Limpiar",
        "clear_history": "¿Deseas borrar el historial? (No borra los archivos generados)",
        "history_cleared": "Historial limpiado",
        "close": "Cerrar",
        "error": "Error",
        "copied": "Copiado al portapapeles",
        "choose_dark": "Color oscuro",
        "choose_light": "Color claro",
        "open_failed": "No se pudo abrir",
        "view_history": "Ver historial",
        "preview": "Vista previa",
        "generate_qr": "Generar QR",
        "preview_png": "Vista previa (PNG):",
        "format": "Formato:",
        "error_level": "Error:",
        "scale": "Escala:",
        "border": "Borde:",
        "micro_qr": "Micro QR",
        "dark_color": "Color (oscuro):",
        "light_color": "Color (claro):",
        "logo": "Logo (solo PNG):",
        "output_file": "Archivo de salida:",
        "text_or_url": "Texto o URL:",
    }
}

_current_lang = "es"

def set_lang(lang: str):
    global _current_lang
    if lang in LANGS:
        _current_lang = lang

def t(key: str, **kwargs) -> str:
    msg = LANGS.get(_current_lang, {}).get(key, key)
    return msg.format(**kwargs)
