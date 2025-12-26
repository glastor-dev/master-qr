from __future__ import annotations

import os
import tempfile
import tkinter as tk
from pathlib import Path
from tkinter import colorchooser, filedialog, messagebox, ttk

from PIL import Image, ImageTk

from .config import AppConfig, load_config, save_config
from .history import append_history, clear_history, default_history_path, read_history
from .render import save_qr


class MasterQRApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Master QR")
        self.resizable(False, False)

        self._preview_photo: ImageTk.PhotoImage | None = None

        cfg = load_config()

        self.data_var = tk.StringVar()
        self.output_var = tk.StringVar(value=cfg.output)
        self.format_var = tk.StringVar(value=cfg.fmt)
        self.scale_var = tk.IntVar(value=int(cfg.scale))
        self.border_var = tk.IntVar(value=int(cfg.border))
        self.error_var = tk.StringVar(value=str(cfg.error))
        self.micro_var = tk.BooleanVar(value=bool(cfg.micro))
        self.dark_var = tk.StringVar(value=str(cfg.dark))
        self.light_var = tk.StringVar(value=str(cfg.light))
        self.logo_var = tk.StringVar(value=str(cfg.logo))
        self.status_var = tk.StringVar(value="Listo")

        container = ttk.Frame(self, padding=12)
        container.grid(row=0, column=0, sticky="nsew")

        # Contenido
        ttk.Label(container, text="Texto o URL:").grid(row=0, column=0, sticky="w")
        data_entry = ttk.Entry(container, textvariable=self.data_var, width=56)
        data_entry.grid(row=1, column=0, columnspan=3, sticky="we", pady=(4, 10))
        data_entry.focus_set()

        # Salida
        ttk.Label(container, text="Archivo de salida:").grid(row=2, column=0, sticky="w")
        out_entry = ttk.Entry(container, textvariable=self.output_var, width=44)
        out_entry.grid(row=3, column=0, columnspan=2, sticky="we", pady=(4, 10))
        ttk.Button(container, text="Elegir...", command=self._choose_output).grid(
            row=3, column=2, sticky="e", padx=(8, 0), pady=(4, 10)
        )

        # Opciones
        ttk.Label(container, text="Formato:").grid(row=4, column=0, sticky="w")
        format_combo = ttk.Combobox(
            container,
            textvariable=self.format_var,
            values=["PNG", "SVG", "PDF", "EPS", "TXT"],
            state="readonly",
            width=8,
        )
        format_combo.grid(row=5, column=0, sticky="w", pady=(4, 10))
        format_combo.bind("<<ComboboxSelected>>", lambda _e: self._sync_logo_state())

        ttk.Label(container, text="Error:").grid(row=4, column=1, sticky="w")
        error_combo = ttk.Combobox(
            container,
            textvariable=self.error_var,
            values=["L", "M", "Q", "H"],
            state="readonly",
            width=6,
        )
        error_combo.grid(row=5, column=1, sticky="w", pady=(4, 10))

        ttk.Label(container, text="Escala:").grid(row=4, column=2, sticky="w")
        scale_spin = ttk.Spinbox(
            container, from_=1, to=50, textvariable=self.scale_var, width=7
        )
        scale_spin.grid(row=5, column=2, sticky="w", pady=(4, 10))

        ttk.Label(container, text="Borde:").grid(row=6, column=0, sticky="w")
        border_spin = ttk.Spinbox(
            container, from_=0, to=20, textvariable=self.border_var, width=7
        )
        border_spin.grid(row=7, column=0, sticky="w", pady=(4, 10))

        ttk.Checkbutton(container, text="Micro QR", variable=self.micro_var).grid(
            row=6, column=1, sticky="w", pady=(0, 12)
        )

        ttk.Label(container, text="Color (oscuro):").grid(row=7, column=1, sticky="w")
        dark_entry = ttk.Entry(container, textvariable=self.dark_var, width=12)
        dark_entry.grid(row=8, column=1, sticky="w", pady=(4, 10))
        ttk.Button(container, text="Elegir", command=self._pick_dark).grid(
            row=8, column=1, sticky="e", pady=(4, 10)
        )

        ttk.Label(container, text="Color (claro):").grid(row=7, column=2, sticky="w")
        light_entry = ttk.Entry(container, textvariable=self.light_var, width=12)
        light_entry.grid(row=8, column=2, sticky="w", pady=(4, 10))
        ttk.Button(container, text="Elegir", command=self._pick_light).grid(
            row=8, column=2, sticky="e", pady=(4, 10)
        )

        ttk.Label(container, text="Logo (solo PNG):").grid(row=9, column=0, sticky="w")
        self.logo_entry = ttk.Entry(container, textvariable=self.logo_var, width=44)
        self.logo_entry.grid(row=10, column=0, columnspan=2, sticky="we", pady=(4, 10))
        self.logo_button = ttk.Button(container, text="Elegir...", command=self._choose_logo)
        self.logo_button.grid(
            row=10, column=2, sticky="e", padx=(8, 0), pady=(4, 10)
        )

        # Acciones
        ttk.Button(container, text="Ver historial", command=self._show_history).grid(
            row=11, column=0, sticky="w", pady=(0, 12)
        )
        ttk.Button(container, text="Vista previa", command=self._preview).grid(
            row=11, column=1, sticky="w", pady=(0, 12)
        )
        ttk.Button(container, text="Generar QR", command=self._generate).grid(
            row=11, column=2, sticky="e", pady=(0, 12)
        )

        ttk.Label(container, text="Vista previa (PNG):").grid(row=12, column=0, sticky="w")
        self.preview_label = ttk.Label(container)
        self.preview_label.grid(row=13, column=0, columnspan=3, sticky="w")

        ttk.Label(container, textvariable=self.status_var, foreground="gray").grid(
            row=14, column=0, columnspan=3, sticky="w"
        )

        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self._sync_logo_state()

        for i in range(3):
            container.columnconfigure(i, weight=1)

    def _choose_output(self) -> None:
        fmt = (self.format_var.get() or "PNG").lower()
        ext = f".{fmt}"

        initial = Path(self.output_var.get() or "qr.png")
        if initial.is_dir():
            initial = initial / f"qr{ext}"

        path = filedialog.asksaveasfilename(
            title="Guardar QR como...",
            initialdir=str(initial.parent),
            initialfile=initial.name,
            defaultextension=ext,
            filetypes=[
                ("PNG", "*.png"),
                ("SVG", "*.svg"),
                ("PDF", "*.pdf"),
                ("EPS", "*.eps"),
                ("TXT", "*.txt"),
                ("Todos", "*.*"),
            ],
        )
        if path:
            self.output_var.set(path)

    def _choose_logo(self) -> None:
        path = filedialog.askopenfilename(
            title="Elegir logo (PNG/JPG)",
            filetypes=[
                ("Imágenes", "*.png;*.jpg;*.jpeg"),
                ("PNG", "*.png"),
                ("JPG", "*.jpg;*.jpeg"),
                ("Todos", "*.*"),
            ],
        )
        if path:
            self.logo_var.set(path)

    def _pick_dark(self) -> None:
        color = colorchooser.askcolor(title="Color oscuro")
        if color and color[1]:
            self.dark_var.set(color[1])

    def _pick_light(self) -> None:
            def _sync_logo_state(self) -> None:
                is_png = (self.format_var.get() or "PNG").upper() == "PNG"
                state = "normal" if is_png else "disabled"
                self.logo_entry.configure(state=state)
                self.logo_button.configure(state=state)
                if not is_png:
                    self.logo_var.set("")

            def _normalize_hex(self, value: str) -> str:
                v = value.strip()
                if not v:
                    return v
                if not v.startswith("#"):
                    raise ValueError("El color debe ser hex, ej: #RRGGBB")
                h = v[1:]
                if len(h) == 3:
                    h = "".join(ch * 2 for ch in h)
                if len(h) != 6 or any(c not in "0123456789abcdefABCDEF" for c in h):
                    raise ValueError("Color inválido. Usa #RRGGBB o #RGB")
                return "#" + h.upper()

            def _save_config(self) -> None:
                cfg = AppConfig(
                    output=self.output_var.get(),
                    fmt=self.format_var.get(),
                    scale=int(self.scale_var.get()),
                    border=int(self.border_var.get()),
                    error=self.error_var.get(),
                    micro=bool(self.micro_var.get()),
                    dark=self.dark_var.get(),
                    light=self.light_var.get(),
                    logo=self.logo_var.get(),
                )
                save_config(cfg)

            def _on_close(self) -> None:
                # Guarda settings sin molestar al usuario.
                try:
                    self._save_config()
                finally:
                    self.destroy()
        color = colorchooser.askcolor(title="Color claro")
        if color and color[1]:
            self.light_var.set(color[1])

    def _effective_output_path(self) -> Path:
        out_path = Path(self.output_var.get().strip() or "qr.png")
        fmt = (self.format_var.get() or "PNG").lower()
        desired_suffix = f".{fmt}"

        if out_path.suffix:
            out_path = out_path.with_suffix(desired_suffix)
        else:
            out_path = Path(str(out_path) + desired_suffix)

        return out_path

    def _open_path(self, path: str) -> None:
        try:
            os.startfile(path)  # type: ignore[attr-defined]
        except Exception as exc:
            messagebox.showerror("No se pudo abrir", str(exc))

    def _copy_to_clipboard(self, text: str) -> None:
        self.clipboard_clear()
        self.clipboard_append(text)
        self.update_idletasks()
        self.status_var.set("Copiado al portapapeles")

    def _preview(self) -> None:
        data = self.data_var.get().strip()
        if not data:
            messagebox.showerror("Falta contenido", "Ingresa un texto o URL.")
            return

        if (self.format_var.get() or "PNG").upper() != "PNG":
            messagebox.showinfo("Vista previa", "La vista previa solo aplica a PNG.")
            return

        try:
            tmp = Path(tempfile.gettempdir()) / "master_qr_preview.png"

            logo_path = Path(self.logo_var.get()) if self.logo_var.get().strip() else None
            error = self.error_var.get()
            if logo_path is not None and error != "H":
                error = "H"

            dark = self._normalize_hex(self.dark_var.get()) if self.dark_var.get().strip() else None
            light = self._normalize_hex(self.light_var.get()) if self.light_var.get().strip() else None
            if dark:
                self.dark_var.set(dark)
            if light:
                self.light_var.set(light)

            save_qr(
                data=data,
                output=tmp,
                error=error,
                micro=self.micro_var.get(),
                scale=int(self.scale_var.get()),
                border=int(self.border_var.get()),
                dark=dark,
                light=light,
                logo=logo_path,
            )

            img = Image.open(tmp)
            img.thumbnail((220, 220), Image.Resampling.LANCZOS)
            self._preview_photo = ImageTk.PhotoImage(img)
            self.preview_label.configure(image=self._preview_photo)
            self.status_var.set("Vista previa actualizada")
            self._save_config()
        except Exception as exc:
            messagebox.showerror("Error", str(exc))
            self.status_var.set("Error en vista previa")

    def _generate(self) -> None:
        data = self.data_var.get().strip()
        if not data:
            messagebox.showerror("Falta contenido", "Ingresa un texto o URL.")
            return

        out_path = self._effective_output_path()

        if out_path.suffix.lower() not in {".png", ".svg", ".pdf", ".eps", ".txt"}:
            messagebox.showerror(
                "Formato no soportado",
                "Usa extensión .png, .svg, .pdf, .eps o .txt.",
            )
            return

        if out_path.exists():
            ok = messagebox.askyesno(
                "Sobrescribir",
                "El archivo ya existe. ¿Deseas sobrescribirlo?",
            )
            if not ok:
                self.status_var.set("Cancelado")
                return

        try:
            dark = self._normalize_hex(self.dark_var.get()) if self.dark_var.get().strip() else None
            light = self._normalize_hex(self.light_var.get()) if self.light_var.get().strip() else None
            if dark:
                self.dark_var.set(dark)
            if light:
                self.light_var.set(light)
        except Exception as exc:
            messagebox.showerror("Color", str(exc))
            return

        logo_path = Path(self.logo_var.get()) if self.logo_var.get().strip() else None
        if logo_path is not None and out_path.suffix.lower() != ".png":
            messagebox.showerror("Logo", "El logo solo se soporta con salida PNG.")
            return

        error = self.error_var.get()
        if logo_path is not None and error != "H":
            error = "H"

        try:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            save_qr(
                data=data,
                output=out_path,
                error=error,
                micro=self.micro_var.get(),
                scale=int(self.scale_var.get()),
                border=int(self.border_var.get()),
                dark=dark,
                light=light,
                logo=logo_path,
            )

            append_history(
                data=data,
                output=out_path,
                fmt=out_path.suffix.lstrip("."),
                error=error,
                scale=int(self.scale_var.get()),
                border=int(self.border_var.get()),
                micro=bool(self.micro_var.get()),
            )
        except Exception as exc:  # pragma: no cover
            messagebox.showerror("Error", str(exc))
            self.status_var.set("Error al generar")
            return

        self.output_var.set(str(out_path))
        self.status_var.set(f"Generado: {out_path}")
        messagebox.showinfo("OK", f"QR generado en:\n{out_path}")
        self._save_config()

    def _show_history(self) -> None:
        items = read_history()
        if not items:
            messagebox.showinfo(
                "Historial",
                f"Aún no hay historial.\n\nArchivo: {default_history_path()}",
            )
            return

        win = tk.Toplevel(self)
        win.title("Historial")
        win.resizable(True, True)

        frame = ttk.Frame(win, padding=12)
        frame.grid(row=0, column=0, sticky="nsew")
        win.columnconfigure(0, weight=1)
        win.rowconfigure(0, weight=1)

        ttk.Label(frame, text=f"Archivo: {default_history_path()}").grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 8)
        )

        listbox = tk.Listbox(frame, height=14, width=110)
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=listbox.yview)
        listbox.configure(yscrollcommand=scrollbar.set)
        listbox.grid(row=1, column=0, sticky="nsew")
        scrollbar.grid(row=1, column=1, sticky="ns")

        # Muestra las últimas 50 entradas para no saturar la UI.
        shown = items[-50:]
        for it in shown:
            created_at = it.get("created_at", "")
            fmt = it.get("fmt", "")
            output = it.get("output", "")
            data = it.get("data", "")
            preview = data.replace("\n", " ")
            if len(preview) > 60:
                preview = preview[:57] + "..."
            listbox.insert(
                tk.END,
                f"{created_at} | {fmt.upper():<3} | {preview} | {output}",
            )

        def selected_item() -> dict:
            sel = listbox.curselection()
            if not sel:
                return {}
            return shown[int(sel[0])] or {}

        actions = ttk.Frame(frame)
        actions.grid(row=2, column=0, columnspan=2, sticky="we", pady=(10, 0))

        def on_open() -> None:
            it = selected_item()
            path = it.get("output", "")
            if not path:
                return
            self._open_path(path)

        def on_copy_path() -> None:
            it = selected_item()
            path = it.get("output", "")
            if path:
                self._copy_to_clipboard(path)

        def on_copy_data() -> None:
            it = selected_item()
            data = it.get("data", "")
            if data:
                self._copy_to_clipboard(data)

        def on_open_folder() -> None:
            it = selected_item()
            path = it.get("output", "")
            if not path:
                return
            folder = str(Path(path).parent)
            self._open_path(folder)

        def on_clear() -> None:
            ok = messagebox.askyesno(
                "Limpiar historial",
                "¿Deseas borrar el historial? (No borra los archivos generados)",
            )
            if not ok:
                return
            clear_history()
            listbox.delete(0, tk.END)
            self.status_var.set("Historial limpiado")

        ttk.Button(actions, text="Abrir archivo", command=on_open).grid(
            row=0, column=0, sticky="w"
        )
        ttk.Button(actions, text="Abrir carpeta", command=on_open_folder).grid(
            row=0, column=1, sticky="w", padx=(8, 0)
        )
        ttk.Button(actions, text="Copiar ruta", command=on_copy_path).grid(
            row=0, column=2, sticky="w", padx=(8, 0)
        )
        ttk.Button(actions, text="Copiar contenido", command=on_copy_data).grid(
            row=0, column=3, sticky="w", padx=(8, 0)
        )
        ttk.Button(actions, text="Limpiar", command=on_clear).grid(
            row=0, column=4, sticky="w", padx=(8, 0)
        )
        ttk.Button(actions, text="Cerrar", command=win.destroy).grid(
            row=0, column=5, sticky="e"
        )

        actions.columnconfigure(5, weight=1)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)


def main() -> int:
    app = MasterQRApp()
    app.mainloop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
