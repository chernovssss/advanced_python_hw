import argparse
import re
import sys

WORD_PATTERN = re.compile(r'\w+')


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Python version of the wc command')

    parser.add_argument('files',
                        default='-',
                        nargs='*',
                        type=argparse.FileType('r'),
                        help='The file to display the last lines of')
    return parser


def count_lines_words_bytes(file) -> (int, int, int):
    lines_count, words_count, bytes_count = 0, 0, 0
    try:
        for line in file:
            lines_count += 1
            words_count += len(WORD_PATTERN.findall(line))
            bytes_count += len(line.encode('utf-8'))
    except (KeyboardInterrupt, EOFError):
        pass
    return lines_count, words_count, bytes_count


def print_wc_summary(total_lines_count, total_words_count, total_bytes_count, additional_info=None):
    print(
        f'{total_lines_count:>6} {total_words_count:>6} {total_bytes_count:>6} {additional_info if additional_info else ""}')


def main():
    parser = get_parser()
    args = parser.parse_args()
    total_lines_count, total_words_count, total_bytes_count = 0, 0, 0
    if args.files[0] == '-':
        total_lines_count, total_words_count, total_bytes_count = count_lines_words_bytes(sys.stdin)
        print_wc_summary(total_lines_count,
                         total_words_count,
                         total_bytes_count)
    else:
        for file in args.files:
            lines_count, words_count, bytes_count = count_lines_words_bytes(file)
            total_bytes_count += bytes_count
            total_words_count += words_count
            total_lines_count += lines_count
            print_wc_summary(lines_count,
                             words_count,
                             bytes_count,
                             file.name)
        if len(args.files) > 1:
            print_wc_summary(total_lines_count,
                             total_words_count,
                             total_bytes_count,
                             "total" if len(args.files) > 1 else "")


if __name__ == '__main__':
    main()
