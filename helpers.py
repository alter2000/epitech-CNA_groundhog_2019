#!/usr/bin/python3

from math import sqrt, fsum

switches: int = 0


def run_exit(vs, T):
    if len(vs['in']) < T:
        raise ValueError("something has gone horribly wrong")
    global switches
    print("Global tendency switched {} times".format(switches))
    allpos = [abs(x - .5) for x in vs['pos']]
    print("5 weirdest values are {}".format(
        [vs['in'][allpos.index(x) + T - 1] for x in sorted(allpos)[-5:]]
        [::-1]))
    exit(0)


def sd_multiple(inp = [], T = 0):
    if len(inp) < T:
        return None
    try:
        avg = fsum(inp[-T:]) / T
        std_dev = sqrt(fsum((x - avg)**2 for x in inp[-T:]) / T)
        return '{:.2f}'.format(std_dev)
    except (ValueError, FloatingPointError, ZeroDivisionError):
        return None


def mob_avg(inp = [], T = 0):
    if len(inp) < T:
        return None
    try:
        return fsum(inp[-T:]) / T
    except (ValueError, FloatingPointError, ZeroDivisionError):
        return None


def switch(vs, T):
    global switches
    if len(vs) <= T + 1:
        return ""
    try:
        cur = round((vs[-1] / vs[-(1 + T)] - 1) * 100)
        prev = round((vs[-2] / vs[-(2 + T)] - 1) * 100)
        if abs(prev + cur) != abs(prev) + abs(cur):
            switches += 1
            return "       a switch occurs"
        else:
            return ""
    except (IndexError, ValueError, FloatingPointError, ZeroDivisionError):
        return ""

def sd_single(vs, T):
    if len(vs) < T:
        return "nan"
    try:
        avg = fsum(vs[-T:]) / T
        std_deviation = sqrt(
                fsum([(x - avg) ** 2
                    for x in vs[-T:]])
                / T)
        return '{:.2f}'.format(std_deviation)
    except (ValueError, FloatingPointError, ZeroDivisionError):
        return "nan"

def rel_evo(vs, T):
    if len(vs) <= T:
        return "nan"
    try:
        value = round((vs[-1] / vs[-(1 + T)] - 1) * 100)
        return '{}'.format(value)
    except (ValueError, FloatingPointError, ZeroDivisionError):
        return "nan"

def inc_avg(vs, T):
    if len(vs) <= T:
        return "nan"
    try:
        return '{:.2f}'.format(fsum(
            [max(0, x - y) for (x, y) in
                zip(vs[-T:],
                    vs[-(T + 1):-1])])
            / T)
    except (ValueError, FloatingPointError, ZeroDivisionError):
        return "nan"


def do_magic(T, vals, cur):
    vals['in'].append(cur)

    print("g={}       r={}%       s={}{}".format(
          inc_avg(vals['in'], T),   rel_evo(vals['in'], T),
          sd_single(vals['in'], T), switch(vals['in'], T)))
    vals['sd'].append(sd_multiple(vals['in'], T))
    vals['avg'].append(mob_avg(vals['in'], T))

    vals['sd'] = list(filter(None, vals['sd']))
    vals['avg'] = list(filter(None, vals['avg']))
    vals['sd'] = list(filter(None, vals['sd']))
    try:
        low = vals['avg'][-1] - 2 * float(vals['sd'][-1])
        high = vals['avg'][-1] + 2 * float(vals['sd'][-1])
        vals['pos'].append((vals['in'][-1] - low) / (high - low))
    except (IndexError, ZeroDivisionError):
        pass
