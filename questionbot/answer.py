from dataclasses import dataclass
from .stanza.pword import PWord
from typing import Literal


"""
The model of the answer sent to the page
"""


@dataclass
class Answer:
    status: Literal["ok", "failure"]
    text: str
    warning: str = ""
    info: str = ""
