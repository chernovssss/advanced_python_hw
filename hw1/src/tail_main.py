import argparse
import io
import sys

to_be_printed = []


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Python version of the tail command')

    parser.add_argument('files',
                        default='-',
                        nargs='*',
                        type=argparse.FileType('r'),
                        help='The file to display the last lines of')
    parser.add_argument('-n', '--lines',
                        type=int,
                        default=10,
                        help='Number of lines to display')

    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.files[0] == '-':
        try:
            for line in sys.stdin:
                if len(to_be_printed) >= args.lines:
                    to_be_printed.pop(0)
                to_be_printed.append(line)
        except KeyboardInterrupt:
            for line in to_be_printed:
                print(line, end='')
            print('^C')
            sys.exit(0)
    else:
        for file in args.files:
            with file as f:
                f: io.TextIOWrapper
                print(f'==> {f.name} <==') if len(args.files) > 1 else None
                lines = f.readlines()
                last_lines = lines[-args.lines:]
                for line in last_lines:
                    print(line, end='')
            print() if len(args.files) > 1 else None


if __name__ == '__main__':
    main()
