#!/usr/bin/env python3

from sys import argv, exit, stderr
from helpers import do_magic


def run_exit(ls):
    def parse(ls):
        return ls

    ls = parse(ls)
    print("Global tendency switched {0:d} times\n{0:d} weirdest values are "
            .format(ls), ls)
    exit(0)


if __name__ == "__main__":
    try:
        if argv[1] == "-h":
            print("SYNOPSIS", "	./groundhog period", "", "DESCRIPTION",
                  "	period	the number of days defining a period", sep='\n')
            exit(0)
        else:
            T = int(argv[1])
    except Exception as e:
        print("Invalid arguments, try `-h`?", file=stderr)
        exit(84)

    vs = {'avg' : [],
          'sd'  : [],
          'pos' : [],
          'in'  : [],
         }
    while True:
        try:
            inp = input()
            if inp == "STOP":
                run_exit(vs)
            else:
                inp = float(inp)
        except ValueError:
            print("Invalid temperature numeral", file=stderr)
            exit(84)
        do_magic(T, vs, inp)
