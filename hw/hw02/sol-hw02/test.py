def product(n,term):
  prod,k = 1,1
  while k<=n:
     prod,k=term(k)*prod,k+1
  return prod

def identity(n):
  return n
  result = product(3,identity)
  print(result)
