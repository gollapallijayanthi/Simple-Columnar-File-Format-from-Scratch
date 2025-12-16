Simple Columnar File Format from Scratch

This project implements a simplified analytical columnar file format inspired by Parquet.
It is built from scratch to demonstrate how modern analytics file formats store data,
compress it, and allow efficient selective column reads.

----------------------------------------

Project Structure:

Simple-Columnar-File-Format/
│
├── README.md
│   - Project overview and step-by-step verification instructions
│
├── SPEC.md
│   - Formal binary file format specification
│
├── writer.py
│   - CSV → custom columnar binary writer with compression
│
├── reader.py
│   - Custom columnar file reader with selective column reads
│
├── csv_to_custom.py
│   - CLI tool to convert CSV into the custom format
│
├── custom_to_csv.py
│   - CLI tool to convert custom format back to CSV
│   - Supports selective column export
│
├── generate_big_csv.py
│   - Utility script to generate a large CSV dataset
│
├── benchmark.py
│   - Compares CSV scanning vs selective column reads
│
├── sample.csv
│   - Small CSV file for basic correctness testing
│
├── big_sample.csv
│   - Large CSV file for performance demonstration
│
├── sample.custom
│   - Custom columnar file generated from sample.csv
│
├── big_sample.custom
│   - Custom columnar file generated from big_sample.csv
│
├── output_full.csv
│   - Full CSV reconstructed from the custom format
│
└── output_selected.csv
    - CSV containing only selected columns



README.md
- Explains the project, verification steps, and expected outputs.

SPEC.md
- Defines the binary file format specification including header layout,
  data types, offsets, and compression details.

writer.py
- Reads a CSV file.
- Splits data column-wise.
- Serializes each column into binary form.
- Compresses each column using zlib.
- Writes header metadata and column blocks.

reader.py
- Parses the file header.
- Reads schema and column offsets.
- Supports full reads and selective column reads using file seeking.

csv_to_custom.py
- Command-line tool to convert CSV to the custom columnar format.

custom_to_csv.py
- Command-line tool to convert the custom format back to CSV.
- Supports optional selective column export.

generate_big_csv.py
- Generates a large CSV file for performance testing.

benchmark.py
- Compares CSV column scanning vs selective column read from custom format.


----------------------------------------

What was built:

- A custom binary columnar file format with a defined specification (SPEC.md)
- Column-wise storage with per-column compression
- Header metadata storing column offsets for direct seeking
- A writer to convert CSV into the custom format
- A reader that supports selective column reads
- CLI tools for conversion
- Benchmarks to demonstrate the performance concept

----------------------------------------

How to verify (step by step):

1. Generate a large CSV file:
   python generate_big_csv.py

   Output:
   - big_sample.csv (large input dataset)

2. Convert CSV to custom columnar format:
   python csv_to_custom.py big_sample.csv big_sample.custom

   Output:
   - big_sample.custom (binary columnar file)

3. Convert full data back to CSV:
   python custom_to_csv.py big_sample.custom output_full.csv

   Output:
   - output_full.csv
   - Contains all columns and proves round-trip correctness

4. Convert selected columns only:
   python custom_to_csv.py big_sample.custom output_selected.csv score salary

   Output:
   - output_selected.csv
   - Contains only selected columns
   - Proves selective column read (column pruning)

5. Run benchmark:
   python benchmark.py

   Output:
   - Prints CSV read time vs custom selective read time
   - Demonstrates performance concept (times may be near zero for small datasets)

----------------------------------------

Verification Summary:

- output_full.csv proves data correctness and lossless conversion.
- output_selected.csv proves selective column reads using header offsets.
- benchmark.py demonstrates the efficiency concept of columnar storage.

This project focuses on low-level data engineering concepts such as
binary file layout, metadata management, compression, and efficient I/O,
rather than using existing high-level data libraries.
