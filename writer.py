import csv, struct, zlib

TYPE_INT = 1
TYPE_FLOAT = 2
TYPE_STRING = 3

def write_custom(csv_file, out_file):
    with open(csv_file) as f:
        rows = list(csv.reader(f))

    header = rows[0]
    data = rows[1:]
    cols = {h: [] for h in header}

    for row in data:
        for i, v in enumerate(row):
            cols[header[i]].append(v)

    with open(out_file, "wb") as f:
        f.write(b"CSTM")
        f.write(struct.pack("<i", len(header)))
        f.write(struct.pack("<i", len(data)))

        meta_positions = []

        for h in header:
            name = h.encode()
            f.write(struct.pack("<H", len(name)))
            f.write(name)

            sample = cols[h][0]
            if sample.isdigit():
                dtype = TYPE_INT
            else:
                try:
                    float(sample)
                    dtype = TYPE_FLOAT
                except:
                    dtype = TYPE_STRING

            f.write(struct.pack("B", dtype))
            meta_positions.append(f.tell())
            f.write(struct.pack("<QQQ", 0, 0, 0))

        for h in header:
            raw = b""
            sample = cols[h][0]

            if sample.isdigit():
                for v in cols[h]:
                    raw += struct.pack("<i", int(v))

            else:
                try:
                    for v in cols[h]:
                        raw += struct.pack("<d", float(v))
                except:
                    offsets = []
                    buf = b""
                    pos = 0
                    for v in cols[h]:
                        b = v.encode()
                        pos += len(b)
                        offsets.append(pos)
                        buf += b
                    for o in offsets:
                        raw += struct.pack("<i", o)
                    raw += buf

            compressed = zlib.compress(raw)
            start = f.tell()
            f.write(compressed)

            meta = meta_positions.pop(0)
            cur = f.tell()
            f.seek(meta)
            f.write(struct.pack("<QQQ", start, len(compressed), len(raw)))
            f.seek(cur)
