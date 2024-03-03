import argparse
import signal
import sys


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Python version of the nl command')
    parser.add_argument('file',
                        default='-',
                        nargs='?',
                        type=argparse.FileType('r'),
                        help='Input file to number. If not provided, uses standard input.')
    parser.add_argument('-b', '--body-numbering',
                        default='t',
                        choices=['a', 't'],
                        help='Specify the type of line numbering to use.')
    parser.add_argument('-n', '--number-format',
                        default='rn',
                        choices=['ln', 'rn', 'rz'],
                        help='Specify the line numbering format to use.')
    parser.add_argument('-w', '--number-width',
                        default=6,
                        type=int,
                        help='Use a number of columns for the line numbers.')
    return parser


def main():
    signal.signal(signal.SIGINT, signal_handler)

    parser = get_parser()
    args = parser.parse_args()

    line_number = 0
    number_format = get_number_format(args)
    is_numbering_empty = True if args.body_numbering == 't' else False

    with args.file as f:
        for line in f:
            if not line.strip() and not is_numbering_empty:
                continue

            print(f'{line_number:{number_format}} {line}', end='')
            line_number += 1


def get_number_format(args: argparse.Namespace) -> str:
    number_format = ''
    if args.number_format[0] == 'r':
        number_format += '>'
    else:
        number_format += '<'

    if args.number_format[1] == 'n':
        number_format += f'{args.number_width}'
    else:
        number_format += f'0{args.number_width}d'
    return number_format


def signal_handler(sig, frame):
    print('^C')
    sys.exit(0)


if __name__ == '__main__':
    main()
