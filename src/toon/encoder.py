"""Core TOON encoding functionality."""

from typing import Any, Optional

from .constants import DEFAULT_DELIMITER, DELIMITERS
from .encoders import encode_value
from .normalize import normalize_value
from .types import EncodeOptions, ResolvedEncodeOptions
from .writer import LineWriter


def encode(value: Any, options: Optional[EncodeOptions] = None) -> str:
    """Encode a value into TOON format.

    Args:
        value: The value to encode (must be JSON-serializable)
        options: Optional encoding options

    Returns:
        TOON-formatted string
    """
    pass


def resolve_options(options: Optional[EncodeOptions]) -> ResolvedEncodeOptions:
    """Resolve encoding options with defaults.

    Args:
        options: Optional user-provided options

    Returns:
        Resolved options with defaults applied
    """
    pass
