# apple-compress
Python bindings for Apple's libcompression.

Based on bindings from [Asahi Linux](https://github.com/AsahiLinux/asahi-installer/blob/8bbbb8ca5a347d99b243e10f24358573f1587df0/asahi_firmware/img4.py#L17-L27).

## Requirements
- Python 3.8 or higher
- An *OS system

## Usage
### Library
Read the [API usage](https://github.com/m1stadev/apple-compress/wiki/API-Usage).

### CLI
```
Usage: acompress [OPTIONS]

  A Python CLI tool for compression using Apple's libcompression.

Options:
  --version              Show the version and exit.
  -i, --input FILENAME   Input file.  [required]
  -o, --output FILENAME  Output file.  [required]
  -c, --compress         Compress the data.
  -d, --decompress       Decompress the data.
  -l, --lzfse            LZFSE compress the data.
  -b, --lzfse-iboot      LZFSE compress the data (iBoot compatible).
  -z, --zlib             zlib compress the data.
  -v, --verbose          Increase verbosity.
  -h, --help             Show this message and exit.
```

## Installation
- Install from [PyPI](https://pypi.org/project/apple-compress/):
    - ```python3 -m pip install apple-compress```
- Local installation:
    - `./install.sh`
    - Requires [Poetry](https://python-poetry.org)

## Support
For any questions/issues you have, [open an issue](https://github.com/m1stadev/apple-compress/issues).