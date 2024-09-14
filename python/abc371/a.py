s = input().split()

ages = {
    "A": 1,
    "B": 1,
    "C": 1,
}

if s[0] == "<":
    ages["B"] += ages["A"]
else:
    ages["A"] += ages["B"]

if s[1] == "<":
    ages["C"] += ages["A"]
else:
    ages["A"] += ages["C"]

if s[2] == "<":
    ages["C"] += ages["B"]
else:
    ages["B"] += ages["C"]

# who is the 2nd oldest?

sorted_ages = sorted(ages.items(), key=lambda x: x[1])

print(sorted_ages[1][0])

