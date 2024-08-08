import pdb
def num_eights(n):
    if n % 10 == 8:
        return 1 + num_eights(n // 10)
    elif n < 10:
        return 0
    else:
        return num_eights(n // 10)

def digit_distance(n):
    if n < 10:
        return 0
    return abs(n % 10 - (n // 10) % 10)+digit_distance(n // 10)
#Alternate solution 1:
def digit_distance_alt(n):
    def helper(prev,n):
        if n == 0:
            return 0
        dist = abs(prev - n % 10)
        return dist + helper(n % 10,n // 10)
    return helper(n % 10,n//10)
def digit_distance_alt2(n):
    pdb.set_trace()
    def helper(dist,prev,n):
        if n == 0:
            return dist
        dist += abs(prev - n % 10)
        prev = n % 10
        n //= 10
        return helper(dist,prev,n)
    return helper(0,n % 10,n//10)
def is_even(n):
        if n == 0:
            return True
        else:
            if (n-1) == 0:
                return False
            else:
                return is_even((n-1)-1)
def Alice(n):
    if n == 0:  #如果终止条件设为1，当桌面上还剩两个时，bob会把剩下的都拿走，这时就没有终止条件了
        print ("Bob wins!")
    else:
        return Bob(n-1)
def Bob(n):
    if n == 0:
        print("Alice wins!")
    elif is_even(n):
         Alice(n-2)
    else:
         Alice(n-1)
def interleaved_sum(n, odd_func, even_func):
    def sum_from(k):
        if k > n:
            return 0
        elif k == n:
            return odd_func(k)
        else:
            return odd_func(k)+even_func(k+1)+sum_from(k+2)
    return sum_from(1)
def next_larger_coin(coin):
    if coin == 1
