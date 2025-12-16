# Simple Columnar File Format from Scratch



This project implements a **simplified analytical columnar file format**, inspired by modern data formats such as **Apache Parquet**.
It is built completely **from scratch** to demonstrate how analytical storage systems work internally.

The goal of this project is **learning and demonstration**, not production usage.
It focuses on understanding **binary file layout, column-wise storage, compression, metadata management, and efficient selective reads**.

---

## Key Concepts Demonstrated

* Column-oriented data storage
* Custom binary file format design
* Header metadata with column offsets
* Per-column compression using `zlib`
* Efficient selective column reads (column pruning)
* File seeking for performance
* CSV ↔ custom format conversion
* Basic benchmarking of access patterns

---

## Project Structure

```
Simple-Columnar-File-Format/
├── README.md
│   └── Project overview and verification steps
├── SPEC.md
│   └── Formal binary file format specification
├── writer.py
│   └── CSV → custom columnar binary writer with compression
├── reader.py
│   └── Custom columnar file reader with selective column reads
├── csv_to_custom.py
│   └── CLI tool to convert CSV into the custom format
├── custom_to_csv.py
│   └── CLI tool to convert custom format back to CSV
│       └── Supports selective column export
├── generate_big_csv.py
│   └── Utility script to generate a large CSV dataset
├── benchmark.py
│   └── Compares CSV scanning vs selective column reads
├── sample.csv
│   └── Small CSV file for correctness testing
├── big_sample.csv
│   └── Large CSV file for performance demonstration
├── sample.custom
│   └── Custom file generated from sample.csv
├── big_sample.custom
│   └── Custom file generated from big_sample.csv
├── output_full.csv
│   └── Full CSV reconstructed from custom format
└── output_selected.csv
    └── CSV containing only selected columns
```

---

## File Format Design

The custom file format is **binary and columnar**.

### High-level layout

* **Header**

  * Magic number
  * Number of rows
  * Schema (column names and data types)
  * Offsets and sizes of each column block
* **Column Data Blocks**

  * Each column stored independently
  * Each column compressed using `zlib`

This layout allows the reader to **jump directly to required columns** without scanning the entire file.

Full details are documented in **`SPEC.md`**.

---

## What Was Built

* A custom binary columnar file format
* A formal specification (`SPEC.md`)
* Column-wise storage with per-column compression
* Metadata-based column offsets for direct seeking
* CSV → custom format writer
* Custom format → CSV reader
* Support for selective column reads
* Command-line tools for conversion
* Benchmark to demonstrate performance concept

---

## How to Verify (Step by Step)

### 1. Generate a large CSV file

```bash
python generate_big_csv.py
```

**Output**

* `big_sample.csv`

---

### 2. Convert CSV to custom columnar format

```bash
python csv_to_custom.py big_sample.csv big_sample.custom
```

**Output**

* `big_sample.custom`

---

### 3. Convert full data back to CSV

```bash
python custom_to_csv.py big_sample.custom output_full.csv
```

**Output**

* `output_full.csv`
* Confirms **lossless round-trip conversion**

---

### 4. Convert selected columns only

```bash
python custom_to_csv.py big_sample.custom output_selected.csv score salary
```

**Output**

* `output_selected.csv`
* Contains only selected columns
* Demonstrates **selective column read (column pruning)**

---

### 5. Run benchmark

```bash
python benchmark.py
```

**Output**

* CSV full scan time
* Custom format selective column read time
* Demonstrates the **performance advantage concept** of columnar storage
  (timings may be small for small datasets)

---

## Verification Summary

* `output_full.csv` proves correctness and lossless conversion
* `output_selected.csv` proves selective column access
* `benchmark.py` demonstrates the efficiency concept of columnar formats

---


