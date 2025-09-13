import pyperf
from pathlib import Path

# 512-level path with 10 characters per level: /abcdefghij/klmnopqrst/uvwxyzabcd/...
# Generate 10-character segments by cycling through the alphabet
def generate_10char_segment(index):
    """Generate a 10-character segment based on index"""
    segment = ""
    for i in range(10):
        char_index = (index * 10 + i) % 26
        segment += chr(ord('a') + char_index)
    return segment

PATH = "/" + "/".join(generate_10char_segment(i) for i in range(512))

def bench():
    for i in range(100000):
        p = Path(PATH)
        hash(p)

runner = pyperf.Runner()
runner.bench_func('bench', bench)