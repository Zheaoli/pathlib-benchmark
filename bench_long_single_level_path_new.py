import pyperf
from pathlib_new import Path

# 512-character single-level path (starts with / and contains 511 more characters)
PATH = "/" + "a" * 511

def bench():
    for i in range(100000):
        p = Path(PATH)
        hash(p)

runner = pyperf.Runner()
runner.bench_func('bench', bench)