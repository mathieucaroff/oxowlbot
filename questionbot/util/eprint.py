import sys

def eprint(*a, **kw):
    print(*a, **kw, file=sys.stderr)