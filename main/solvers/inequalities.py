from sympy.abc import x
from xympy import Poly
from sympy.solvers.inequalities import solve_rational_inequalities

solve_rational_inequalities([[
((Poly(-x + 1), Poly(1, x)), '>='),
((Poly(-x + 1), Poly(1, x)), '<=')]])

solve_rational_inequalities([[
((Poly(x), Poly(1, x)), '!='),
((Poly(-x + 1), Poly(1, x)), '>=')]])
Union(Interval.open(-oo, 0), Interval.Lopen(0, 1))