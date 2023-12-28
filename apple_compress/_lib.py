import sys
from ctypes import cdll

if sys.platform != 'darwin':
    raise OSError('libcompression can only be used on macOS')

try:
    _lib = cdll.LoadLibrary('libcompression.dylib')
except OSError as error:
    raise OSError('libcompression.dylib not found') from error
