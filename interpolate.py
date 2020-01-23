#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import argparse, sys

def f(x, P):
    (x0, y0), (x1, y1), (x2, y2), (x3, y3) = P
    a1 = 2*(x2-x0)
    b1 = 2*(x2-x1)

    a2 = 2*(x2-x1)
    b2 = 2*(x3-x1)

    c1 = (6 / (x2-x1)) * (y2 - y1) + (6 / (x1-x0)) * (y0 - y1)
    c2 = (6 / (x3-x2)) * (y3 - y2) + (6 / (x2-x1)) * (y1 - y2)

    q = (a2*c1 - a1*c2) / (a2*b1 - a1*b2)
    p = (c2 - b2*q) / a2

    a = (p/(6*(x2-x1)))
    b = (q/(6*(x2-x1)))
    c = (y1/(x2-x1) - (p*(x2-x1))/6)
    d = (y2/(x2-x1) - (q*(x2-x1))/6)

    return a*(x2-x)**3 + b*(x-x1)**3 + c*(x2-x) + d*(x-x1)

parser = argparse.ArgumentParser()
parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="stdin if omitted or '-'.")
parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help="stdout if omitted or '-'.")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--resolution', '-r', type=float,
    help="Resolution of interpolated points.")
group.add_argument('--steps', '-s', type=int,
    help="Desired number of steps between two given points. Unlike resolution, steps does not take the distance between x_i and x_i+1 into account.")
parser.add_argument('--plot', '-p', action='store_true', help="Show plot when done.")
parser.add_argument('--dx', '-d', type=float, default=1.0,
    help="When no X given use DX as offset to the previous X.")
args = parser.parse_args()

fmt = "{: 2.6}, {: 2.6}\n"

AP = []
AX = []
AY = []
P = []
last_x = 0
for ln, line in enumerate(args.infile.readlines()):
    C = line.split(",")
    C = list(map(float, filter(str.strip, C)))
    if len(C) == 1:
        y = C[0]
        P.append((float(last_x+args.dx), float(y)))
        last_x += args.dx
    elif len(C) == 2:
        x = C[0]
        y = C[1]
        P.append((float(x), float(y)))
        if x <= last_x and len(P) > 1:
            raise(Exception(f"Data not continuous near line {ln}. (x={x}, previous x={last_x}) (implied dx={args.dx})"))
        last_x = x
    elif len(C) == 0:
        continue
    else:
        assert(len(C) == 0)

    ## START boundary condition
    if len(P) == 1 and args.plot:
        AP.append(P[0])
    if len(P) < 4: continue

    if args.resolution:
        resolution = args.resolution
    else:
        resolution = (P[2][0]-P[1][0])/args.steps
    X = np.arange(P[1][0], P[2][0], resolution)
    Y = f(X, P)
    for x, y in zip(X, Y):
        args.outfile.write(fmt.format(x, y))
    P = P[1:4]

    if args.plot:
        AP.append(P[0])
        AX.extend(X)
        AY.extend(Y)
## END boundary condition
args.outfile.write(fmt.format(P[1][0], P[1][1]))

if args.plot:
    AX.append(P[1][0])
    AY.append(P[1][1])
    AP.append(P[1]) ## endpoint
    AP.append(P[2]) ## endpoint
    plt.scatter(AX, AY, s=2)
    X, Y = zip(*AP)
    plt.scatter(X, Y, alpha=.5)
    plt.show()
