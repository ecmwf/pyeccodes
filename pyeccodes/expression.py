
# (C) Copyright 2020- ECMWF.

# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.

# In applying this licence, ECMWF does not waive the privileges and immunities granted to it by
# virtue of its status as an intergovernmental organisation nor does it submit to any jurisdiction.

E = {}


class Expression:

    def __truediv__(self, other):
        return E['/'](self, other)

    def __rsub__(self, other):
        return E['-'](other, self)

    def __sub__(self, other):
        return E['-'](self, other)

    def __gt__(self, other):
        return E['>'](self, other)

    def __ge__(self, other):
        return E['>='](self, other)

    def __add__(self, other):
        return E['+'](self, other)

    def __radd__(self, other):
        return E['+'](other, self)

    def __mul__(self, other):
        return E['*'](self, other)

    def __rmul__(self, other):
        return E['*'](other, self)

    def __mod__(self, other):
        return E['%'](self, other)


def evaluate(x, handle, kind=None):
    if isinstance(x, Expression):
        return x.evaluate(handle, kind)
    return x


class Get(Expression):

    def __init__(self, name, kind=None):
        self.name = name
        self.kind = kind

    def evaluate(self, handle, kind=None):
        return handle.get(self.name, kind if kind else self.kind)

    def __repr__(self):
        if self.kind:
            return "Get(%s,%s)" % (self.name, self.kind)
        else:
            return "Get(%s)" % (self.name,)


class Binop(Expression):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, handle, kind=None):
        left = evaluate(self.left, handle, kind)
        right = evaluate(self.right, handle, kind)
        if left is None or right is None:
            return None
        return self.op(left, right)


class Unop(Expression):

    def __init__(self, expr):
        self.expr = expr

    def evaluate(self, handle, kind=None):
        expr = evaluate(self.expr, handle, kind)
        if expr is None:
            return None
        return self.op(expr)


class SubExp(Binop):

    def op(self, a, b):
        return a - b


class AddExp(Binop):

    def op(self, a, b):
        return a + b


class MulExp(Binop):

    def op(self, a, b):
        return a * b


class DivExp(Binop):

    def op(self, a, b):
        return a // b


class ModExp(Binop):

    def op(self, a, b):
        return a % b


class GtExp(Binop):

    def op(self, a, b):
        return 1 if a > b else 0


class GeExp(Binop):

    def op(self, a, b):
        return 1 if a >= b else 0


class And(Binop):

    def op(self, a, b):
        return (a and b)


class Or(Binop):

    def op(self, a, b):
        return (a or b)


class Not(Unop):

    def op(self, a):
        return not a


E['%'] = ModExp
E['/'] = DivExp
E['-'] = SubExp
E['+'] = AddExp
E['*'] = MulExp
E['>'] = GtExp
E['>='] = GeExp
