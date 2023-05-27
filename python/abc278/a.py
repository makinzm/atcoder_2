## You have to check the domain first.

n,k = list(map(int,input().split()))
a = input().split()

if n>k:
    zeros = ["0"] * k

    ans_lst = a[k:]+zeros

else:
    ans_lst = ["0"] * n

[print(i,end=" ") for i in ans_lst]
print()
