n,m = map(int, input().split())

if n == 1:
    ans = m+1 
else:
    ans = 1 * (n**(m+1) -1 ) // (n-1)

if ans > 10 ** 9:
    print("inf")
else:
    print(ans)

