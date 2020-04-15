"""
This type stub file was generated by pyright.
"""

import warnings
from __future__ import absolute_import
from io import BytesIO
from google.protobuf.internal.encoder import _EncodeVarint
from google.protobuf.internal.decoder import _DecodeVarint
from google.protobuf.message import DecodeError
from .CoreNLP_pb2 import *
from typing import Any, Optional

def parseFromDelimitedString(obj, buf, offset=...):
    """
    Stanford CoreNLP uses the Java "writeDelimitedTo" function, which
    writes the size (and offset) of the buffer before writing the object.
    This function handles parsing this message starting from offset 0.

    @returns how many bytes of @buf were consumed.
    """
    ...

def writeToDelimitedString(obj, stream: Optional[Any] = ...):
    """
    Stanford CoreNLP uses the Java "writeDelimitedTo" function, which
    writes the size (and offset) of the buffer before writing the object.
    This function handles parsing this message starting from offset 0.

    @returns how many bytes of @buf were consumed.
    """
    ...

def to_text(sentence):
    """
    Helper routine that converts a Sentence protobuf to a string from
    its tokens.
    """
    ...
