from __future__ import annotations

from collections import OrderedDict
from pathlib import Path
from typing import Optional

import frida_bindgen_core as core

from .model import FACTORY, Customizations, Model

INCLUDED_GIO_OBJECT_TYPES = [
    "Cancellable",
    "IOStream",
    "InputStream",
    "OutputStream",
    "SocketAddress",
    "SocketAddressEnumerator",
    "SocketConnectable",
    "InetSocketAddress",
    "UnixSocketAddress",
]
INCLUDED_GIO_ENUMERATIONS = [
    "FileMonitorEvent",
    "SocketFamily",
    "UnixSocketAddressType",
]


def compute_model(
    frida_gir: Path,
    glib_gir: Path,
    gobject_gir: Path,
    gio_gir: Path,
    customizations: Customizations,
    frida_header: Optional[Path] = None,
) -> Model:
    model = core.compute_model(
        frida_gir,
        glib_gir,
        gobject_gir,
        gio_gir,
        customizations,
        FACTORY,
        INCLUDED_GIO_OBJECT_TYPES,
        INCLUDED_GIO_ENUMERATIONS,
        seed_object_first=True,
    )
    if frida_header is not None:
        available_symbols = frida_header.read_text(encoding="utf-8")
        model.available_symbols = available_symbols
        model._object_types = OrderedDict(
            (name, otype)
            for name, otype in model._object_types.items()
            if otype.c_type in available_symbols and otype.get_type in available_symbols
        )
        model.enumerations = OrderedDict(
            (name, enum)
            for name, enum in model.enumerations.items()
            if enum.c_type in available_symbols and enum.get_type in available_symbols
        )
    return model
