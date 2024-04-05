import sys
from typing import BinaryIO

import click
from loguru import logger

from apple_compress import Algorithm, __version__, compress, decompress

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(message=f'acompress {__version__}')
@click.option(
    '-i',
    '--input',
    'input_',
    type=click.File('rb'),
    help='Input file.',
    required=True,
)
@click.option(
    '-o',
    '--output',
    'output',
    type=click.File('wb'),
    help='Output file.',
    required=True,
)
@click.option(
    '-c', '--compress', 'action_type', flag_value='compress', help='Compress the data.'
)
@click.option(
    '-d',
    '--decompress',
    'action_type',
    flag_value='decompress',
    help='Decompress the data.',
)
@click.option(
    '-l',
    '--lzfse',
    'compression_type',
    flag_value='LZFSE',
    help='LZFSE compress the data.',
)
@click.option(
    '-b',
    '--lzfse-iboot',
    'compression_type',
    flag_value='LZFSE_IBOOT',
    help='LZFSE compress the data (iBoot compatible).',
)
@click.option(
    '-z',
    '--zlib',
    'compression_type',
    flag_value='ZLIB',
    help='zlib compress the data.',
)
@click.option(
    '-v',
    '--verbose',
    'verbose',
    is_flag=True,
    help='Increase verbosity.',
)
def main(
    input_: BinaryIO,
    output: BinaryIO,
    action_type: str,
    compression_type: str,
    verbose: bool,
) -> None:
    """A Python CLI tool for compression using Apple's libcompression."""

    if verbose:
        logger.remove()
        logger.add(
            sys.stderr,
            level='DEBUG',
            format='[{time:MMM D YYYY - hh:mm:ss A zz}] {level} | {module}:{function}:{line} {message}',
        )
        logger.enable(__package__)
    else:
        sys.tracebacklimit = 0

    if sys.platform != 'darwin':
        click.echo('[ERROR] Only Darwin systems are supported. Exiting.')
        return

    if compression_type is None:
        raise click.BadParameter('Must specify a compression type.')

    if verbose:
        click.echo(f'Using compression type: {compression_type}')
    compression_type = getattr(Algorithm, compression_type)

    if action_type is None:
        raise click.BadParameter('Must specify either --compress or --decompress.')
    elif action_type == 'compress':
        output.write(compress(input_.read(), compression_type))
    elif action_type == 'decompress':
        output.write(decompress(input_.read(), compression_type))

    click.echo(
        f'{action_type.capitalize()}ed {compression_type.name} data to {output.name}.'
    )


if __name__ == '__main__':
    main()
