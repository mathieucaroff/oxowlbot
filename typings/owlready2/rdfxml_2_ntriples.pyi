"""
This type stub file was generated by pyright.
"""

import sys
import time
from typing import Any, Optional

INT_DATATYPES = "http://www.w3.org/2001/XMLSchema#integer", "http://www.w3.org/2001/XMLSchema#byte", "http://www.w3.org/2001/XMLSchema#short", "http://www.w3.org/2001/XMLSchema#int", "http://www.w3.org/2001/XMLSchema#long", "http://www.w3.org/2001/XMLSchema#unsignedByte", "http://www.w3.org/2001/XMLSchema#unsignedShort", "http://www.w3.org/2001/XMLSchema#unsignedInt", "http://www.w3.org/2001/XMLSchema#unsignedLong", "http://www.w3.org/2001/XMLSchema#negativeInteger", "http://www.w3.org/2001/XMLSchema#nonNegativeInteger", "http://www.w3.org/2001/XMLSchema#positiveInteger"
FLOAT_DATATYPES = "http://www.w3.org/2001/XMLSchema#decimal", "http://www.w3.org/2001/XMLSchema#double", "http://www.w3.org/2001/XMLSchema#float", "http://www.w3.org/2002/07/owl#real"
def is_bn(x):
  ...

def is_fake_bn(x):
  ...

def parse(f, on_prepare_obj: Optional[Any] = ..., on_prepare_data: Optional[Any] = ..., new_blank: Optional[Any] = ..., default_base=...):
  ...

if __name__ == "__main__":
  filename = sys.argv[- 1]
  t = time.time()
  nb_triple = parse(filename)
  t = time.time() - t