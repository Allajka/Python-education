from sympy import *
from sympy.plotting import plot
init_printing()

x = Symbol('x')
f = x + 2022
f.subs(x, -77)
f.subs(x,-210)
plot(f)
print(f)
g = sin(x+x)/x
plot(g)
print(g)