#!/usr/bin/env python
import os
import sys
import argparse

uniq_set = set()


def uniq_line():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        if ns.field is not None:
            process_fields(line)
            continue
        if line not in uniq_set:
            uniq_set.add(line)
            print(line, end='')


def process_fields(line: str):
    line = line.strip().split(ns.delimiter)
    if line and (len(line) - 1) >= ns.field:
        s = line[ns.field]
        if s not in uniq_set:
            uniq_set.add(s)
            print(s)


def check_pyversion():
    if sys.version_info.major < 2:
        print('version not supported:', sys.version)
        sys.exit(1)


def main():
    global ns
    if ns.delimiter is None:
        ns.delimiter = ' '
    if ns.field is not None:
        if ns.field <= 0:
            ns.field = None
        elif ns.field > 0:
            ns.field = ns.field - 1
    uniq_line()


if __name__ == '__main__':
    check_pyversion()
    ap = argparse.ArgumentParser('uniq.py')
    myname = os.path.basename(sys.argv[0])
    ap.usage = '<STDOUT> | {e} [-h] [-d DELIMITER] [-f FIELD]\n\n  e.g: cat 1.txt | {e}'.format(e=myname)
    ap.add_argument('-d', '--delimiter', dest='delimiter', type=str)
    ap.add_argument('-f', '--field', dest='field', type=int)
    ns = ap.parse_args()
    if sys.stdin.isatty():
        sys.exit()
    main()
