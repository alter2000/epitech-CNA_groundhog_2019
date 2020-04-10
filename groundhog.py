#!/usr/bin/env python3

from sys import argv, exit, stderr
from helpers import do_magic, run_exit


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
                run_exit(vs, T)
            else:
                inp = float(inp)
        except ValueError:
            print("Invalid temperature numeral", file=stderr)
            exit(84)
        except EOFError:
            exit(0)
        do_magic(T, vs, inp)
