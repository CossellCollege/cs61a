"""def falling(n,k):
    result = 1
    while(k):
        result*= (n-k+1)
        k=k-1
   return result"""
def falling_alt(n,k):
    result,stop = 1,n-k
    while(n>stop):
        result,n = n*result,n-1 //通过改变n的值来控制终止条件
    return result
def divisible_by_k(n,k):
    count = 0
    i = 1
    while(i<=n):
        if(i%k)==0:
            print(i)
            count+=1
        i+=1
    return count
def sum_digits(y):
    total = 0
    while(y):
        total += y%10 //将数字的末尾相加
        y=y//10      //去掉末尾数字
    return total
def double_eights(n):
    prev_eight = False  //设置标志符
    count = 0
    while(n):
        if(n%10==8)://这道题理解有误，如果一个数字中有连续的两个八则返回ture，而不是统计一个数字中八的数量为2
          count+=1
        n=n//10
    if(count==2):
        prev_eight = True
    return prev_eight

