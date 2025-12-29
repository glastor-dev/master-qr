# 🎯 Master QR - Professional QR Code Generator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/GUI-Tkinter-orange.svg" alt="GUI Framework">
</p>

## 📋 Overview

**Master QR** is a professional-grade static QR code generator with both graphical and command-line interfaces. Static QR codes are permanent and never expire, making them ideal for printed materials, product packaging, and long-term deployments.

### ✨ Key Features

- 🖼️ **Dual Interface**: Intuitive GUI and powerful CLI
- 🎨 **Customization**: Custom colors, logos, and output formats (PNG, SVG)
- 📊 **History Tracking**: Automatic generation history with metadata
- 🔄 **Optional Dynamic URLs**: Built-in redirect server for URL management
- 💾 **Persistent Settings**: Remembers your preferences across sessions
- 📦 **Standalone Executable**: Windows installer available
- 🔒 **Code Signing Ready**: Professional deployment support

---

## 🚀 Quick Start

### Prerequisites

- **Python**: Version 3.10 or higher
- **pip**: Python package installer (included with Python)
- **Operating System**: Windows, Linux, or macOS

### Installation

#### Option 1: Standard Installation (Recommended)
```bash
# Navigate to the project directory
cd master-qr

# Install dependencies
python -m pip install -r QR/requirements.txt
```

#### Option 2: Editable Installation (Development Mode)

Install as an editable package with CLI commands:
```bash
python -m pip install -e .
```

**Benefits:**
- Enables `master-qr` and `master-qr-gui` commands globally
- Ideal for development and testing
- Changes to source code are immediately reflected

---

## 💻 Usage Guide

### Graphical User Interface (GUI)

#### Launch GUI - Standard Installation
```bash
python QR/main.py
```

#### Launch GUI - Editable Installation
```bash
master-qr-gui
```

**GUI Features:**
- Drag-and-drop interface for logo embedding
- Real-time QR preview
- Color picker for customization
- Integrated history viewer
- Export format selection (PNG, SVG)
- Error correction level configuration

---

### Command Line Interface (CLI)

#### Basic Usage - Standard Installation
```bash
# Generate QR from URL
python QR/main.py "https://example.com" -o QR/output/my_qr.png

# Generate QR from text
python QR/main.py "Custom Text Content" -o QR/output/text_qr.png

# Generate SVG format
python QR/main.py "https://example.com" -o QR/output/my_qr.svg
```

#### Basic Usage - Editable Installation
```bash
master-qr "https://example.com" -o my_qr.png
```

#### Advanced CLI Options
```bash
# Full customization example
master-qr "https://example.com" \
  -o output/branded_qr.png \
  --dark "#1a1a1a" \
  --light "#ffffff" \
  --logo assets/company_logo.png \
  --overwrite \
  --history data/custom_history.jsonl
```

**Available Arguments:**

| Argument | Description | Example |
|----------|-------------|---------|
| `data` | Content to encode (URL, text, vCard, etc.) | `"https://example.com"` |
| `-o, --output` | Output file path | `output/qr.png` |
| `--dark` | Dark module color (hex) | `#000000` |
| `--light` | Light module color (hex) | `#FFFFFF` |
| `--logo` | Path to logo image (PNG only) | `logo.png` |
| `--overwrite` | Overwrite existing files without prompt | Flag only |
| `--history` | Custom history file location | `data/history.jsonl` |

**Note:** When using `--logo`, error correction level is automatically set to `H` (High, ~30% data recovery) to ensure QR code remains scannable with the logo overlay.

---

## 📚 Advanced Features

### 📜 Generation History

Master QR automatically logs every generated QR code to a JSONL (JSON Lines) file for audit trails and reproducibility.

**Default Location:** `QR/historial.jsonl`

**Log Entry Format:**
```json
{
  "timestamp": "2025-12-29T14:30:45.123456",
  "content": "https://example.com",
  "output_path": "QR/output/example_qr.png",
  "format": "png",
  "colors": {
    "dark": "#000000",
    "light": "#ffffff"
  },
  "logo": null,
  "error_level": "M"
}
```

**GUI History Viewer:**
- Click **"View History"** button in the GUI
- Browse all generated QR codes
- Copy data or file paths to clipboard
- Filter by date, content, or format

---

### ⚙️ Configuration Persistence (GUI)

The application automatically saves your preferences for seamless workflow continuity.

**Configuration File:** `QR/config.json`

**Saved Settings:**
- Output format (PNG/SVG)
- Default color scheme
- Last used output directory
- Error correction level preference
- Window size and position

**Manual Configuration:**
```json
{
  "output_format": "png",
  "dark_color": "#000000",
  "light_color": "#ffffff",
  "default_output_dir": "QR/output",
  "error_level": "M",
  "window_geometry": "800x600+100+100"
}
```

---

### 🔄 Dynamic URL Redirect System (Optional)

While QR codes themselves are static, you can implement dynamic behavior by pointing them to a redirect URL that you control.

#### Use Case Scenario

Instead of encoding `https://final-destination.com` directly, encode:
```
http://127.0.0.1:5000/r/CAMPAIGN-2025
```

You can later update where `CAMPAIGN-2025` points without regenerating the QR code.

#### Setup Instructions

**1. Define Redirect Mappings**
```bash
# Add a new redirect
python -m master_qr.redirect_server \
  --db QR/redirects.json \
  set CAMPAIGN-2025 https://new-destination.com

# List all redirects
python -m master_qr.redirect_server \
  --db QR/redirects.json \
  list

# Delete a redirect
python -m master_qr.redirect_server \
  --db QR/redirects.json \
  delete CAMPAIGN-2025
```

**2. Start the Redirect Server**
```bash
python -m master_qr.redirect_server \
  --db QR/redirects.json \
  serve \
  --host 127.0.0.1 \
  --port 5000
```

**Server Endpoints:**
- `GET /r/<code>` - Redirect to mapped URL
- `GET /health` - Health check endpoint
- `GET /stats` - View redirect statistics (optional)

**3. Generate QR Code**
```bash
master-qr "http://127.0.0.1:5000/r/CAMPAIGN-2025" -o campaign_qr.png
```

#### ⚠️ Security Considerations

**Local Development Only:**
- Default configuration is for local testing
- **DO NOT expose to the internet without proper security measures**

**Production Deployment Requirements:**
- Implement authentication (API keys, OAuth)
- Use HTTPS with valid SSL certificates
- Add rate limiting to prevent abuse
- Implement logging and monitoring
- Set up CORS policies appropriately
- Use environment variables for sensitive configuration

**Recommended Production Stack:**
- Nginx or Apache as reverse proxy
- Let's Encrypt for SSL certificates
- Gunicorn or uWSGI for WSGI server
- Redis for caching redirect mappings
- PostgreSQL for persistent storage

---

## 📦 Distribution & Deployment

### Windows Executable (PyInstaller)

Create a standalone `.exe` file that doesn't require Python installation.

#### Prerequisites
```bash
# Install development dependencies
pip install pyinstaller
```

#### Build Process

**Option 1: PowerShell Script (Automated)**
```powershell
# Execute build script
.\build_exe.ps1
```

**Option 2: Manual Build**
```bash
pyinstaller --onefile \
  --windowed \
  --name master-qr \
  --icon assets/icon.ico \
  --add-data "QR/assets;assets" \
  QR/main.py
```

**Output:** `dist/master-qr.exe`

**Build Configuration:**
- Single-file executable (`--onefile`)
- No console window for GUI (`--windowed`)
- Custom application icon (`--icon`)
- Bundled assets (`--add-data`)

---

### Release Package Creation

Generate a complete distribution package with all necessary files.

#### Build Release ZIP
```powershell
# Execute release script
.\release.ps1
```

**Package Contents:**
- `master-qr.exe` - Standalone executable
- `README.md` - Documentation
- `LICENSE` - License information
- `examples/` - Sample usage examples (optional)
- `CHANGELOG.md` - Version history (optional)

**Output:** `release/master-qr-<version>-win64.zip`

**Version Detection:**
The script automatically extracts version from:
1. `setup.py` - `version` parameter
2. `QR/__init__.py` - `__version__` variable
3. Git tags - `git describe --tags`

---

### Professional Installer (Inno Setup)

Create a Windows installer with professional branding and system integration.

#### Prerequisites

Download and install [Inno Setup](https://jrsoftware.org/isinfo.php) (free, open-source)

#### Build Installer

**Option 1: Inno Setup GUI**

1. Open `installer.iss` in Inno Setup Compiler
2. Click **Build → Compile**
3. Installer will be generated in `release/` directory

**Option 2: Command Line**
```powershell
# Requires Inno Setup in PATH
ISCC.exe installer.iss
```

**Installer Features:**
- Custom welcome screen and branding
- License agreement display
- Installation directory selection
- Start Menu shortcuts
- Desktop shortcut (optional)
- Uninstaller with clean removal
- Registry entries for file associations (optional)
- Automatic updates check (configurable)

**Output:** `release/master-qr-setup-<version>.exe`

#### Customization

Edit `installer.iss` to modify:
```pascal
[Setup]
AppName=Master QR Generator
AppVersion=1.0.0
AppPublisher=Your Company Name
AppPublisherURL=https://yourwebsite.com
DefaultDirName={autopf}\MasterQR
DefaultGroupName=Master QR
OutputDir=release
OutputBaseFilename=master-qr-setup-{#AppVersion}
Compression=lzma2/max
SolidCompression=yes

[Files]
Source: "dist\master-qr.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "README.md"; DestDir: "{app}"; Flags: isreadme
Source: "LICENSE"; DestDir: "{app}"

[Icons]
Name: "{group}\Master QR"; Filename: "{app}\master-qr.exe"
Name: "{autodesktop}\Master QR"; Filename: "{app}\master-qr.exe"
```

---

### 🔐 Code Signing (Production Recommended)

Digital signatures verify your application's authenticity and prevent security warnings.

#### Prerequisites

- **Code Signing Certificate**: Purchase from trusted CA (DigiCert, Sectigo, GlobalSign)
- **Windows SDK**: Includes `signtool.exe` (install via Visual Studio or standalone)

#### Signing Process

**1. Locate SignTool**
```powershell
# Typical locations
C:\Program Files (x86)\Windows Kits\10\bin\<version>\x64\signtool.exe
```

**2. Sign Executable**
```powershell
# Basic signing
signtool sign /f certificate.pfx /p PASSWORD dist\master-qr.exe

# Recommended: With timestamp server
signtool sign `
  /f certificate.pfx `
  /p PASSWORD `
  /tr http://timestamp.digicert.com `
  /td sha256 `
  /fd sha256 `
  /d "Master QR Generator" `
  /du "https://yourwebsite.com" `
  dist\master-qr.exe
```

**Parameter Explanation:**
- `/f` - Certificate file (.pfx)
- `/p` - Certificate password
- `/tr` - RFC 3161 timestamp server URL
- `/td` - Timestamp digest algorithm (SHA-256)
- `/fd` - File digest algorithm (SHA-256)
- `/d` - Description displayed to users
- `/du` - URL with more information

**3. Verify Signature**
```powershell
signtool verify /pa /v dist\master-qr.exe
```

#### Timestamp Servers (Recommended)

Timestamps ensure signatures remain valid after certificate expiration.

**Popular Timestamp Servers:**
- DigiCert: `http://timestamp.digicert.com`
- Sectigo: `http://timestamp.sectigo.com`
- GlobalSign: `http://timestamp.globalsign.com`

#### Automation Script
```powershell
# sign_executable.ps1
param(
    [Parameter(Mandatory=$true)]
    [string]$CertPath,
    
    [Parameter(Mandatory=$true)]
    [string]$Password,
    
    [Parameter(Mandatory=$true)]
    [string]$ExePath
)

$SignTool = "C:\Program Files (x86)\Windows Kits\10\bin\10.0.22621.0\x64\signtool.exe"

& $SignTool sign `
    /f $CertPath `
    /p $Password `
    /tr http://timestamp.digicert.com `
    /td sha256 `
    /fd sha256 `
    /d "Master QR Generator" `
    dist\master-qr.exe

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Executable signed successfully" -ForegroundColor Green
    & $SignTool verify /pa /v $ExePath
} else {
    Write-Host "✗ Signing failed" -ForegroundColor Red
    exit 1
}
```

**Usage:**
```powershell
.\sign_executable.ps1 -CertPath "cert.pfx" -Password "secure_password" -ExePath "dist\master-qr.exe"
```

---

## 🛠️ Development

### Project Structure
```
master-qr/
├── QR/
│   ├── __init__.py
│   ├── main.py              # Entry point
│   ├── gui.py               # GUI implementation
│   ├── generator.py         # QR generation logic
│   ├── history.py           # History management
│   ├── config.py            # Configuration handler
│   ├── redirect_server.py   # Optional redirect server
│   ├── requirements.txt     # Python dependencies
│   ├── historial.jsonl      # Generation history (auto-generated)
│   └── config.json          # User preferences (auto-generated)
├── assets/
│   └── icon.ico             # Application icon
├── tests/
│   ├── test_generator.py
│   ├── test_history.py
│   └── test_redirect.py
├── docs/
│   └── API.md               # API documentation
├── setup.py                 # Package configuration
├── build_exe.ps1            # Build script
├── release.ps1              # Release packaging script
├── installer.iss            # Inno Setup configuration
├── README.md                # This file
├── LICENSE                  # License information
└── .gitignore
```

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run all tests
pytest tests/

# Run with coverage report
pytest --cov=QR tests/

# Run specific test file
pytest tests/test_generator.py
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting pull requests.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📞 Support

- **Documentation**: [GitHub Wiki](https://github.com/yourusername/master-qr/wiki)
- **Issues**: [Issue Tracker](https://github.com/yourusername/master-qr/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/master-qr/discussions)
- **Email**: support@yourcompany.com

---

## 🙏 Acknowledgments

- [qrcode](https://github.com/lincolnloop/python-qrcode) - Core QR code generation library
- [Pillow](https://python-pillow.org/) - Image processing
- [PyInstaller](https://www.pyinstaller.org/) - Executable packaging
- [Inno Setup](https://jrsoftware.org/isinfo.php) - Installer creation

---

<p align="center">
  Made with ❤️ by the Master QR Team
</p>

<p align="center">
  <a href="#-master-qr---professional-qr-code-generator">Back to Top ↑</a>
</p>