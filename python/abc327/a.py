n = int(input())
s = input()

def main():
    for i in range(n-1):
        if s[i:i+2] in ("ab","ba"):
            return "Yes"
    return "No"

print(main())
