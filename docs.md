# Documentation
`apple-compress` only provides 2 functions: `compress()` and `decompress()`. Both functions require an `Algorithm` value to be provided, to define what compression algorithm will be used.

## Compression
Simply call `apple_compress.compress()` with the data you wish to compress (must be of type `bytes`), and the `Algorithm` value:
```py
import apple_compress
data = b'This data will be compressed using apple-compress'
algorithm = apple_compress.Algorithm.ZLIB

compressed_data = apple_compress.compress(data, algorithm)
```

## Decompression
Similarly to compression, you only need to call `apple_compress.decompress()` with the data you wish to decompress (again, must be of type `bytes`), and the `Algorithm` value:
```py
import apple_compress
compressed_data = b'\x0b\xc9\xc8,VHI,IT(\xcf\xcc\xc9QHJUHIM\xce\xcf-(J-.NMQ(-\xce\xccKWH,(\xc8I\xd5\x85\t\x03\x00'
algorithm = apple_compress.Algorithm.ZLIB

data = apple_compress.decompress(data, algorithm)
```

If you know what the size of the decompressed data is, you can pass that into `decompress()` as the `decmp_size` argument, which may be beneficial in more resource-limited environments (By default, apple_compress will allocate 2x the size of the data as a buffer, and if necessary, increase by 1.5x every time until the buffer is large enough to hold the decompressed data).

## Supported Algorithms
`apple-compress` supports nearly every compression algorithm that `libcompression`'s `compression_encode_buffer()` function does:
- `LZFSE` - LZFSE compression
- `LZFSE_IBOOT` - LZFSE compression (iBoot-compatible)
- `LZMA` - LZMA compression (level 6)
- `LZ4` - LZ4 compression
- `LZ4_RAW` - LZ4 compression (no block headers)
- `ZLIB` - ZLIB compression (level 5)

Support for Brotli and LZBITMAP (de)compression will come in a later update.