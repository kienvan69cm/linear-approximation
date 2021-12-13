from sympy import *
import numpy as np


def calc(fxyz, a, b, c):
    x = Symbol("x")
    y = Symbol('y')
    z = Symbol('z')
    fxyz = sympify(fxyz)
    fx = fxyz.diff(x)
    fy = fxyz.diff(y)
    fz = fxyz.diff(z)
    f = lambdify((x, y, z), fxyz)
    fx = lambdify((x, y, z), fx)
    fy = lambdify((x, y, z), fy)
    fz = lambdify((x, y, z), fz)
    Lxyz = f(a, b, c)+(x-a)*fx(a, b, c)+(y-b)*fy(a, b, c)+(z-c)*fz(a, b, c)
    return Lxyz


def main():
    with open("input.txt", "r") as f:
        inp = f.readline()
        inp = inp.split(", ")
        fxyz = inp[0]
        a = int(inp[1])
        b = int(inp[2])
        c = int(inp[3])
    with open("output.txt", "w") as f:
        f.write(str(calc(fxyz, a, b, c)).replace(".0", ""))


main()
