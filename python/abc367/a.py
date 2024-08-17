a,b,c = map(int, input().split())

if b < c and ( 0 <= a <= b or c <= a <= 24):
    print('Yes')
elif b > c and ( 0 <= a <= b and c <= a <= 24):
    print('Yes')
else:
    print('No')
