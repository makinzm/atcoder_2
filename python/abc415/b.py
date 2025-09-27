s = input()

index = [i+1 for i, char in enumerate(s) if char == "#"]

for i in range(0, len(index),2):
    print(f"{index[i]},{index[i+1]}")

