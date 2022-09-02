# Does it divide

# https://www.hackerearth.com/practice/math/number-theory/primality-tests/practice-problems/algorithm/does-it-divide-3c60b8fb/

for i in range(int(input())):
    n=int(input())
    a=[]
    for i in range(1,n+1):
        a.append(i)
    sum_all=sum(list(a))
    product=1
    for j in a:
        product=product*j
    if product%sum_all==0:
        print("YES")
    else:
        print("NO")