from __future__ import annotations

import importlib
import importlib.machinery
import importlib.util
from pathlib import Path


def _load_extension():
    package_dir = Path(__file__).resolve().parent
    for suffix in importlib.machinery.EXTENSION_SUFFIXES:
        candidate = package_dir / ("_rust_wrapper" + suffix)
        if candidate.exists():
            spec = importlib.util.spec_from_file_location("carta._rust_wrapper_ext", candidate)
            if spec is None or spec.loader is None:
                continue
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module

    try:
        return importlib.import_module("_rust_wrapper")
    except ModuleNotFoundError as error:
        raise ImportError(
            "Could not find the compiled `_rust_wrapper` extension module in the carta package"
        ) from error

_ext = _load_extension()

convert_text = _ext.convert_text
convert = _ext.convert
