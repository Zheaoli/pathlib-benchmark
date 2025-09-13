import pyperf
from pathlib_new import Path

PATH = "/abc"

def bench():
    for i in range(100000):
        p = Path(PATH)
        str(p)
        hash(p)

runner = pyperf.Runner()
runner.bench_func('bench', bench)