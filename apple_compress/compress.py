from ctypes import create_string_buffer
from typing import Optional

from loguru import logger

from ._lib import _lib
from .errors import CompressionError
from .types import Algorithm


def compress(data: bytes, algorithm: Algorithm) -> bytes:
    """
    Compresses the given data using the specified algorithm.

    Args:
        data (bytes): The data to be compressed.
        algorithm (Algorithm): The compression algorithm to use.

    Returns:
        bytes: The compressed data.

    Raises:
        CompressionError: If the compression fails.
    """
    logger.info(
        f'Compressing data ({len(data)} bytes) with algorithm: {algorithm.name}'
    )
    logger.debug(f'Creating buffer of size: {len(data) + 256}')
    dest_buf = create_string_buffer(len(data) + 256)

    logger.debug('Calling compression_encode_buffer')
    size = _lib.compression_encode_buffer(
        dest_buf, len(data), data, len(data), None, algorithm.value
    )
    if size == 0:
        raise CompressionError('Failed to compress data')

    logger.success(
        f'Compression with algorithm: {algorithm.name} successful, returning {size} bytes'
    )
    return dest_buf.raw[:size]


def decompress(
    data: bytes, algorithm: Algorithm, decmp_size: Optional[int] = None
) -> bytes:
    """
    Decompresses the given data using the specified algorithm.

    Args:
        data (bytes): The compressed data to be decompressed.
        algorithm (Algorithm): The compression algorithm to use for decompression.
        decmp_size (Optional[int]): The expected size of the decompressed data. If not provided, it is twice the size of `data`. Providing this value is recommended on resource-limited systems.

    Returns:
        bytes: The decompressed data.

    Raises:
        CompressionError: If the decompression fails.
    """
    logger.info(
        f'Decompressing data ({len(data)} bytes) with algorithm: {algorithm.name}'
    )

    if decmp_size is None or decmp_size == 0:
        logger.debug(
            f'No decompressed size provided, assuming data length * 2 ({len(data) * 2})'
        )
        decmp_size = len(data) * 2

    while True:
        logger.debug(f'Creating buffer of size: {decmp_size}')
        dest_buf = create_string_buffer(decmp_size)

        logger.debug('Calling compression_decode_buffer')
        size = _lib.compression_decode_buffer(
            dest_buf, decmp_size, data, len(data), None, algorithm.value
        )
        if size == 0:
            raise CompressionError('Failed to decompress data')

        if size == decmp_size:
            logger.debug(
                'Buffer too small for decompressed data, running again with 1.5x larger buffer'
            )
            decmp_size = round(decmp_size * 1.5)
            continue

        logger.success(
            f'Decompression with algorithm: {algorithm.name} successful, returning {size} bytes'
        )
        return dest_buf.raw[:size]
