#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This module contains the RGB code


def main():
    counter1 = 0
    counter2 = 0
    counter3 = 0
    # this function show outpu

    # utput
    for counter1 in range(256):
        for counter2 in range(256):
            for counter3 in range(256):
                print("{0}, {1}, {2}".format(counter1, counter2, counter3))
    print("\nDone.")


if __name__ == "__main__":
    main()
