#!/usr/bin/python3
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    total_file_size = 0
    status_code_counts = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

        # Parse the input line
            parts = line.strip().split()
            if len(parts) >= 6:
                status_code = parts[-2]
                file_size = int(parts[-1])

            # Update total file size
                total_file_size += file_size

            # Update status code counts
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
                else:
                    status_code_counts[status_code] = 1

        # Print metrics every 10 lines
            if line_count % 10 == 0:
                print_metrics()

    except KeyboardInterrupt:
        pass
