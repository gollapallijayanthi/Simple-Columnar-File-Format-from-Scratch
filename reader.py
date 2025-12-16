import struct, zlib

def read_custom(file, columns=None):
    with open(file, "rb") as f:
        if f.read(4) != b"CSTM":
            raise ValueError("Invalid file")

        ncols = struct.unpack("<i", f.read(4))[0]
        nrows = struct.unpack("<i", f.read(4))[0]

        schema = []
        for _ in range(ncols):
            l = struct.unpack("<H", f.read(2))[0]
            name = f.read(l).decode()
            dtype = struct.unpack("B", f.read(1))[0]
            off, cs, us = struct.unpack("<QQQ", f.read(24))
            schema.append((name, dtype, off, cs, us))

        result = {}

        for name, dtype, off, cs, us in schema:
            if columns and name not in columns:
                continue

            f.seek(off)
            data = zlib.decompress(f.read(cs))

            if dtype == 1:
                result[name] = [struct.unpack("<i", data[i:i+4])[0]
                                for i in range(0, len(data), 4)]

            elif dtype == 2:
                result[name] = [struct.unpack("<d", data[i:i+8])[0]
                                for i in range(0, len(data), 8)]

            else:
                offsets = [struct.unpack("<i", data[i:i+4])[0]
                           for i in range(0, nrows*4, 4)]
                raw = data[nrows*4:]
                out = []
                s = 0
                for o in offsets:
                    out.append(raw[s:o].decode())
                    s = o
                result[name] = out

        return result
