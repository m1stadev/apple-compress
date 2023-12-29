from enum import Enum


class Algorithm(Enum):
    LZ4 = 0x100
    LZ4_RAW = 0x101
    ZLIB = 0x205
    LZMA = 0x306
    LZBITMAP = 0x702
    LZFSE = 0x801
    LZFSE_IBOOT = 0x891
    BROTLI = 0xB02
