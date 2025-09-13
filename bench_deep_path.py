import pyperf
from pathlib import Path

# 512-level path with 1 character per level: /a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/p/...
# We'll use letters a-z repeatedly to create 512 levels
PATH = "/" + "/".join(chr(ord('a') + (i % 26)) for i in range(512))

def bench():
    for i in range(100000):
        p = Path(PATH)
        hash(p)

runner = pyperf.Runner()
runner.bench_func('bench', bench)