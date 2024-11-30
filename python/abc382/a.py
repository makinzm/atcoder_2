n,d = map(int,input().split())
s = input()

count_at_sign = s.count('@')
count_dot = s.count('.')

num_to_eat = min(count_at_sign,d)
print(count_dot + num_to_eat)
