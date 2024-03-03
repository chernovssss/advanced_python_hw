import argparse
import re
import sys


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Python version of the wc command')

    parser.add_argument('files',
                        default='-',
                        nargs='*',
                        type=argparse.FileType('r'),
                        help='The file to display the last lines of')
    return parser


word_pattern = re.compile(r'\w+')


def count_lines_words_bytes(file) -> (int, int, int):
    lines_count, words_count, bytes_count = 0, 0, 0
    for line in file:
        lines_count += 1
        words_count += len(word_pattern.findall(line))
        bytes_count += len(line.encode('utf-8'))
    return lines_count, words_count, bytes_count


def main():
    parser = get_parser()
    args = parser.parse_args()
    total_lines_count, total_words_count, total_bytes_count = 0, 0, 0
    if args.files[0] == '-':
        try:
            for line in sys.stdin:
                total_lines_count += 1
                total_words_count += len(word_pattern.findall(line))
                total_bytes_count += len(line.encode('utf-8'))
        except (KeyboardInterrupt, EOFError):
            pass
    else:
        for file in args.files:
            lines_count, words_count, bytes_count = count_lines_words_bytes(file)
            total_bytes_count += bytes_count
            total_words_count += words_count
            total_lines_count += lines_count
            print(f'{lines_count} {words_count} {bytes_count} {file.name}')
    print(f'{total_lines_count} {total_words_count} {total_bytes_count} {"total" if len(args.files) > 1 else ""}')


if __name__ == '__main__':
    main()
