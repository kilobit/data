#! /usr/bin/env python
# stats.py

"""Simple "from scratch" statistical package inspired by Joel Grus."""

import math

def average(data):
    return sum(data) / float(len(data))

# Define synonyms for the average function.
avg = average
mean = average

def median(data):
    s = sorted(data)
    if len(data) % 2 == 0:
        i = (len(data) / 2) - 1
        return (s[i] + s[i+1]) / 2.0
    else:
        return s[int(math.floor(len(data) / 2))]


if __name__ == '__main__':

    import sys
    import argparse

    commands = {
        'avg': average,
        'average': average,
        'mean': average,
        'median': median
    }


    parser = argparse.ArgumentParser(description='Run statistical calculations.')
    parser.add_argument('command', action='store', type=str, choices=commands.keys(), 
                       help="The statistical operation to perform.")
    parser.add_argument('-d', '--data', action='store', type=float, nargs='+', help='add data on the command line.')
    parser.add_argument('-i', '--input_file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-o', '--output_file', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()

    command = args.command
    infile = args.input_file
    outfile = args.output_file
    data = args.data or map(float, infile.readlines())

    outfile.write(str(commands[command](data)) + '\n')

    
