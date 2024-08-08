from operator import add,mul

square = lambda x: x * x

identity = lambda x: x
triple = lambda x: 3 * x

increment = lambda x: x + 1

def product(n,term):
  prod,k = 1,1
  while k<=n:
     prod,k=term(k)*prod,k+1
  return prod

def accumulate(fuse,start,n,term):
   total,k = start, 1
   while k<=n:
        total,k = fuse(total,term(k)),k+1
   return total     
def summation_using_accumulate(n, term):   
   return accumulate(add,0,n,term)
def product_using_accumulate(n, term):  
   return accumulate(mul,1,n,term)
def make_repeater(f,n):
   def repeater(x):
       k=1
       while k<=n:
            x=f(x) //函数要有输入值 f（f）不合法
            k=k+1
       return x
   return repeater    //返回定义好的repeater函数，实质上还是返回了x，嵌套return

