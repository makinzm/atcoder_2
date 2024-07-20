rate = int(input())

def solve(rate: int) -> int:
    if rate <= 99:
        return 100 - rate
    elif rate <= 199:
        return 200 - rate
    elif rate <= 299:
        return 300 - rate

print(solve(rate))

