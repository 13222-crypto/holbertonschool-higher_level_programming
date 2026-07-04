#!/usr/bin/python3
"""
Log parsing script that reads stdin line by line and computes metrics.
Prints statistics every 10 lines and upon keyboard interruption (CTRL + C).
"""
import sys


def print_stats(total_size, status_codes):
    """
    Prints the accumulated statistics since the beginning.

    Args:
        total_size (int): The sum of all file sizes parsed.
        status_codes (dict): Dictionary with counts for each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {
        "200": 0, "301": 0, "400": 0, "401": 0,
        "403": 0, "404": 0, "405": 0, "500": 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            # Process metrics if line has enough elements
            if len(parts) >= 2:
                # File size is the last token
                try:
                    total_size += int(parts[-1])
                except ValueError:
                    pass

                # Status code is the second to last token
                status = parts[-2]
                if status in status_codes:
                    status_codes[status] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        # Print final metrics if stdin closes normally without error
        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Catch CTRL + C, print metrics accumulated so far, then re-raise
        print_stats(total_size, status_codes)
        raise
