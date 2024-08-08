def composite_identity(f,g):
    def h(x):
        return f(g(x)) == g(f(x))
    return h
def sum_digits(y):
   total = 0
   while(y>0):
       total,y=total + y % 10,y//10
   return total
def is_prime(n):
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True
def count_cond(condition):
    def counter(n):
        i = 1
        count = 0
        while i <= n:
            if condition(n,i):
                count += 1
            i += 1
        return count
    return counter
def multiple(a,b):
    result  = a * b
    while result:
        if result%a==0 and result%b==0:
            multiple = result
        result-=1
    return multiple
def cyele(f1,f2,f3)


