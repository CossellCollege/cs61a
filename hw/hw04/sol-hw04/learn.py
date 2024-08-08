from math import gcd
def add_rationals(x,y):
    nx,dx = numer(x),denom(x)
    ny,dy = numer(y),denom(y)
    return rational(nx*dy+ny*dx,dx*dy)
def mul_rationals(x,y):
    return rational(numer(x)*numer(y),denom(x)*denom(y))
def print_rational(x):
    print(numer(x),'/',denom(x))
def rational_are_equal(x,y):
    return numer(x)*denom(y)==numer(y)*denom(x)

def rational(n,d):
    g =gcd(n,d)
    return [n//g,d//g]
def numer(x):
    return x[0]
def denom(x):
    return x[1]
def divisors(n):
    return [1]+[x for x in range(2,n) if n% x ==0]

def tree(label,branches = []):
    for branch in branches:
        assert is_tree(branch)
    return [label]+list(branches)
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
def is_leaf(tree):
    return not branches(tree)
"斐波那契数列"
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left,right = fib_tree(n-1),fib_tree(n-2)
        return tree(label(left)+label(right),[left,right])
def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        sum([count_leaves(b) for b in branches(t)])
def leaves(tree):
    "return a list of the leaf lebels of a tree"
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum(leave(b) for b in branches(tree),[])

