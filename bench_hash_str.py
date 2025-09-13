import pyperf
from pathlib import Path

PATH = "/abc"

def bench():
    for i in range(100000):
        p = Path(PATH)
        hash(p)
        str(p)

runner = pyperf.Runner()
runner.bench_func('bench', bench)