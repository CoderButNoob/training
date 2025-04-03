def odd_even_sum(l,n):
    sum_even = 0 
    sum_odd = 0 
    res = []

    for num in l :
        if num%2 == 0  :
            sum_even += num
        else:
            sum_odd += num

    res = [sum_even,sum_odd]    
    print(res)


n = int(input())
l = [int(input()) for _ in range(n)]
odd_even_sum(l,n)
    