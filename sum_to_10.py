"""Calculate the sum of a range of integers.

This script sums all integers from a starting value to an
ending value (both inclusive). If no values are provided,
it defaults to summing numbers from 1 to 10.
"""

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sum integers from start to end inclusive"
    )
    parser.add_argument(
        "-s",
        "--start",
        type=int,
        default=1,
        help="First value in the range",
    )
    parser.add_argument(
        "-e",
        "--end",
        type=int,
        default=10,
        help="Last value in the range",
    )
    args = parser.parse_args()

    if args.start > args.end:
        parser.error("start must not exceed end")

    total = sum(range(args.start, args.end + 1))
    print(total)


if __name__ == "__main__":
    main()
