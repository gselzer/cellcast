import sys
import types
from .cellcast import *
from . import cellcast as _ext

# Maturin installs the Rust extension as `cellcast.cellcast`, so PyO3 registers
# submodules (e.g. `models`) under `cellcast.cellcast.*` in sys.modules rather
# than `cellcast.*`. The star-import above brings them in as attributes, but
# `from cellcast.models import ...` fails unless sys.modules is also patched.
for _name in dir(_ext):
    _obj = getattr(_ext, _name)
    if isinstance(_obj, types.ModuleType):
        sys.modules.setdefault(f"cellcast.{_name}", _obj)
