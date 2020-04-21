import dataclasses as dc
from typing import Literal


"""
The model of the answer sent to the page
"""


@dc.dataclass
class Answer:
    status: Literal["ok", "failure"]
    text: str
    warning: str = ""
    info: str = ""
    
    def asdict(self):
        return dc.asdict(self)
