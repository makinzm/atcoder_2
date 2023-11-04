b = int(input())
# たかだか 18^18 よりは小さいからloopでいける

def main():
    for i in range(1,19):
        if b == i**i:
            return i
    return -1

print(main())
