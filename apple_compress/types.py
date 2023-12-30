from enum import Enum


class Algorithm(Enum):
    """
    Enum representing different compression algorithms.

    Attributes:
        LZ4 (int): LZ4 compression algorithm.
        LZ4_RAW (int): LZ4 compression algorithm (no block headers).
        ZLIB (int): ZLIB compression algorithm.
        LZMA (int): LZMA compression algorithm.
        LZFSE (int): LZFSE compression algorithm.
        LZFSE_IBOOT (int): LZFSE compression algorithm (iBoot-compatible).
    """

    LZ4 = 0x100
    LZ4_RAW = 0x101
    ZLIB = 0x205
    LZMA = 0x306
    LZFSE = 0x801
    LZFSE_IBOOT = 0x891
    # These are only supported on newer libcompression versions, disabled for now.
    # LZBITMAP = 0x702
    # BROTLI = 0xB02
