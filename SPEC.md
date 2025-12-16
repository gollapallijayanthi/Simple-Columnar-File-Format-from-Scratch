Custom Columnar File Format Specification



Endianness:

All multi-byte values use little-endian format.



Magic Number:

4 bytes: CSTM



Header Layout:

\- Magic number (4 bytes)

\- Number of columns (int32)

\- Number of rows (int32)



For each column:

\- Column name length (uint16)

\- Column name (UTF-8)

\- Data type (1 byte)

\- Data offset (uint64)

\- Compressed size (uint64)

\- Uncompressed size (uint64)



Data Types:

1 → int32

2 → float64

3 → string



Column Data:

Each column is stored as a compressed block using zlib.



String columns:

\- Offset array (int32 per row)

\- Concatenated UTF-8 string bytes



