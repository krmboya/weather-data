#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


class Day(object):

    def __init__(self, day_no, max_tmp, min_tmp):
        self.no = day_no
        self.max_tmp = max_tmp
        self.min_tmp = min_tmp

    def spread(self):
        return self.max_tmp - self.min_tmp


def clean_int(strn):
    """Returns integer representation of string `strn`"""

    # strip away character * if exists
    strn = strn.strip("*")
    return int(strn)


def get_data(filename):
    """Returns the relevant data from `filename`

    The data will be a list of tuples, each with 3 values:
    Dy, MxT, MnT
    """

    lines = []

    with open(filename) as data_file:
        for line in data_file:
            lines.append(line)

    # remove the first two, and last rows
    lines = lines[2:-1]

    # Convert lines to list of tuples of (Dy, Mxt, Mnt,)
    list_ = []
    for line in lines:
        values = line.split()
        list_.append((values[0],
                      clean_int(values[1]),
                      clean_int(values[2]),))

    return list_


def find_max_spread(data):
    """Finds the day with the maximum spread in data

    `data` - A list of tuples containing values (Dy, MxT, MnT,)

    Returns a tuple (Dy, max_spread,)"""

    first_day = Day(*data[0])
    dy, max_spread = first_day.no, first_day.spread()

    for values in data[1:]:
        day = Day(*values)
        day_spread = day.spread()
        if day_spread > max_spread:
            dy, max_spread = day.no, day_spread

    return dy, max_spread


def main(filename):

    data = get_data(filename)
    day, max_spread = find_max_spread(data)
    output = "{0} {1}\n".format(day, max_spread)
    sys.stdout.write(output)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.stderr.write("usage: python {0} <filename>\n".format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
