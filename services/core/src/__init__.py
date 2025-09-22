"""
Public API for core.

Usage:
    from core import TimeStampMixin, UUIDMixin
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("core")
except PackageNotFoundError:
    __version__ = "0.0.0"

# -------
__all__ = [
    # Mixins
    "TimeStampMixin",
    "UUIDMixin",
]

from .core.mixins.models import TimeStampMixin, UUIDMixin  # noqa
