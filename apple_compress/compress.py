from ctypes import create_string_buffer
from typing import Optional

from ._lib import _lib
from .errors import CompressionError
from .types import Algorithm


def compress(data: bytes, algorithm: Algorithm) -> bytes:
    dest_buf = create_string_buffer(len(data) + 256)

    size = _lib.compression_encode_buffer(
        dest_buf, len(data), data, len(data), None, algorithm.value
    )
    if size == 0:
        raise CompressionError('Failed to compress data')

    return dest_buf.raw[:size]


def decompress(
    data: bytes, algorithm: Algorithm, decmp_size: Optional[int] = None
) -> bytes:
    if decmp_size is None:
        decmp_size = len(data) * 2

    for _ in range(10):
        dest_buf = create_string_buffer(decmp_size)

        size = _lib.compression_decode_buffer(
            dest_buf, decmp_size, data, len(data), None, algorithm.value
        )
        if size == 0:
            raise CompressionError('Failed to decompress data')

        if size == decmp_size:
            # print('decode_buffer: buffer too small, running again with 1.5x larger buffer')
            size *= 1.5
            continue

        return dest_buf.raw[:size]

    raise CompressionError('Buffer too small, giving up')
