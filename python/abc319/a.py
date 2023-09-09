s = """tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481"""

lst = list(map(lambda x: x.split(), s.split("\n")))

a_dict = {}

for items in lst:
    a_dict[items[0]] = int(items[1])

# print(a_dict)

inp = input()

print(a_dict[inp])
