s = input()

current = 0
current_index = 0

buttons = [
    "00",
] + list(map(str, range(10)))

while current_index < len(s):
    for button in buttons:
        if len(button) == 1:
            if s[current_index] == button:
                current_index += 1
                current += 1
                break
        else:
            if current_index + 1 < len(s) and s[current_index:current_index + 2] == button:
                current_index += 2
                current += 1
                break

print(current)

