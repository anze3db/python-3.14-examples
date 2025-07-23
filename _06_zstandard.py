from compression import bz2, zlib, zstd

data = b"Hello world"
print("original", len(data))
res = zstd.compress(data, level=3)
print(len(res), "zstd")

res = bz2.compress(data, compresslevel=3)
print(len(res), " bz2")


res = zlib.compress(data, level=3)
print(len(res), "zlib")

# python3.14 _06_zstandard.py
