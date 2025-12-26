from __future__ import annotations

import sys

from .cli import main as cli_main
from .gui import main as gui_main


def main() -> int:
    # Sin args => GUI. Con args => CLI.
    if len(sys.argv) <= 1 or "--gui" in sys.argv:
        return gui_main()
    return cli_main()


if __name__ == "__main__":
    raise SystemExit(main())
