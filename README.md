# Pathlib Performance Benchmark

This repository contains benchmarks for testing the performance improvements introduced in CPython PR #138645, which optimizes the hash calculation for `pathlib.Path` objects by removing an unnecessary join operation.

## 🎯 Background

CPython PR [#138645](https://github.com/python/cpython/pull/138645) addresses a performance regression in pathlib by optimizing hash calculations. The change targets removing computational overhead when hashing Path objects, showing improvements from **3.76 µs to 2.47 µs** in initial benchmarks.

## 📁 Repository Structure

```
pathlib-benchmark/
├── pathlib/                         # Original pathlib implementation
├── pathlib_new/                     # Optimized pathlib implementation (with PR changes)
├── perf_result/                     # Benchmark results (JSON format)
├── bench_single_level_path.py       # Short single-level path benchmark (original)
├── bench_single_level_path_new.py   # Short single-level path benchmark (optimized)
├── bench_long_single_level_path.py  # Long single-level path benchmark (original)
├── bench_long_single_level_path_new.py # Long single-level path benchmark (optimized)
├── bench_deep_path.py               # 512-level deep path benchmark (original)
├── bench_deep_path_new.py           # 512-level deep path benchmark (optimized)
├── bench_deep_long_path.py          # 512-level deep path with 10-char names (original)
├── bench_deep_long_path_new.py      # 512-level deep path with 10-char names (optimized)
├── bench_str_only.py                # str(p) only operation benchmark (original)
├── bench_str_only_new.py            # str(p) only operation benchmark (optimized)
├── bench_str_hash.py                # str(p); hash(p) operation benchmark (original)
├── bench_str_hash_new.py            # str(p); hash(p) operation benchmark (optimized)
├── bench_hash_str.py                # hash(p); str(p) operation benchmark (original)
├── bench_hash_str_new.py            # hash(p); str(p) operation benchmark (optimized)
└── pyproject.toml                   # Project dependencies
```

## 🔧 Setup

This project uses Python 3.13+ and requires `pyperf` for accurate benchmarking:

```bash
# Install dependencies
pip install -e .

# Or using uv
uv sync
```

## 🧪 Available Tests

- **Short Single-Level Path Benchmark**: Tests hash performance on simple paths like `"/abc"`
  - `bench_single_level_path.py` - Original pathlib implementation
  - `bench_single_level_path_new.py` - Optimized pathlib implementation

- **Long Single-Level Path Benchmark**: Tests hash performance on 512-character paths
  - `bench_long_single_level_path.py` - Original pathlib implementation
  - `bench_long_single_level_path_new.py` - Optimized pathlib implementation

- **Deep Path Benchmark**: Tests hash performance on 512-level deep paths (`/a/b/c/...`)
  - `bench_deep_path.py` - Original pathlib implementation
  - `bench_deep_path_new.py` - Optimized pathlib implementation

- **Deep Long Path Benchmark**: Tests hash performance on 512-level deep paths with 10-character names (`/abcdefghij/klmnopqrst/...`)
  - `bench_deep_long_path.py` - Original pathlib implementation
  - `bench_deep_long_path_new.py` - Optimized pathlib implementation

## 📊 Benchmark Details

The benchmark tests hash performance on single-level paths (`"/abc"`) by:

- Creating 100,000 Path objects in a loop
- Computing hash for each Path object
- Using `pyperf` for statistical accuracy

## 📈 Performance Results

### Short Single-Level Path Results

```
+-----------+-------------------+-----------------------+
| Benchmark | single_level_path | single_level_path_new |
+===========+===================+=======================+
| bench     | 268 ms            | 173 ms: 1.55x faster  |
+-----------+-------------------+-----------------------+
```

**Summary**: The optimized implementation shows a **1.55x performance improvement** (55% faster) for short single-level path hashing operations.

### Long Single-Level Path Results

```
+-----------+------------------------+----------------------------+
| Benchmark | long_single_level_path | long_single_level_path_new |
+===========+========================+============================+
| bench     | 314 ms                 | 214 ms: 1.46x faster       |
+-----------+------------------------+----------------------------+
```

**Summary**: The optimized implementation shows a **1.46x performance improvement** (46% faster) for long single-level path hashing operations.

### Deep Path Results

```
+-----------+-----------+------------------------+
| Benchmark | deep_path | deep_path_new          |
+===========+===========+========================+
| bench     | 1.19 sec  | 1.06 sec: 1.13x faster |
+-----------+-----------+------------------------+
```

**Summary**: The optimized implementation shows a **1.13x performance improvement** (13% faster) for 512-level deep path hashing operations.

### Deep Long Path Results

```
+-----------+----------------+------------------------+
| Benchmark | deep_long_path | deep_long_path_new     |
+===========+================+========================+
| bench     | 2.09 sec       | 2.13 sec: 1.02x slower |
+-----------+----------------+------------------------+
```

**Summary**: The optimized implementation shows a **1.02x performance regression** (2% slower) for 512-level deep paths with 10-character component names.

### Operation Pattern Results

Testing different operation patterns on short single-level paths (`/abc`):

#### 1. hash(p) only - **1.55x faster** ✅

```
+-----------+-------------------+-----------------------+
| Benchmark | single_level_path | single_level_path_new |
+===========+===================+=======================+
| bench     | 268 ms            | 173 ms: 1.55x faster  |
+-----------+-------------------+-----------------------+
```

#### 2. str(p) only - **Equal performance** ✅

```
Benchmark hidden because not significant (1): bench
```

#### 3. str(p); hash(p) - **1.18x faster** ✅

```
+-----------+----------+----------------------+
| Benchmark | str_hash | str_hash_new         |
+===========+==========+======================+
| bench     | 279 ms   | 236 ms: 1.18x faster |
+-----------+----------+----------------------+
```

#### 4. hash(p); str(p) - **1.15x faster** ✅

```
+-----------+----------+----------------------+
| Benchmark | hash_str | hash_str_new         |
+===========+==========+======================+
| bench     | 272 ms   | 237 ms: 1.15x faster |
+-----------+----------+----------------------+
```

### Original CPython PR Results

Based on initial testing from the CPython PR:

- **Before optimization**: ~3.76 µs per hash operation
- **After optimization**: ~2.47 µs per hash operation
- **Improvement**: ~34% performance gain

## 🧪 Test Environment

Benchmarks are performed using:

- **Hardware**: AMD Ryzen 9 9950X3D 16-Core Processor
- **OS**: Linux with amd-pstate-epp driver
- **Python**: 3.13.7 (64-bit) with optimizations enabled
- **Profiler**: pyperf 2.9.0 with CLOCK_MONOTONIC timer

## 📝 Contributing

This benchmark suite helps validate the performance improvements before the changes are merged into CPython. Results help ensure the optimization provides consistent benefits across different environments and use cases.

## 🔗 Related Links

- [CPython PR #138645](https://github.com/python/cpython/pull/138645) - Original performance optimization
- [Python Issue gh-138407](https://github.com/python/cpython/issues/138407) - Performance regression report
- [pyperf documentation](https://pyperf.readthedocs.io/) - Benchmarking tool used