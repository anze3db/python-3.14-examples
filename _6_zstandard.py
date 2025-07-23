from compression import bz2, zlib, zstd

print("original", len(b"Hello, World!"))
res = zstd.compress(b"Hello, World!", level=3)
print(len(res), "zstd", zstd.decompress(res).decode())

res = bz2.compress(b"Hello, World!", compresslevel=3)
print(len(res), " bz2", bz2.decompress(res).decode())


res = zlib.compress(b"Hello, World!", level=3)
print(len(res), "zlib", zlib.decompress(res).decode())
