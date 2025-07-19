s = input()

count_a = 0
count_b = 0

DEBUG = False

while count_a < len(s):
    current_char = s[-count_a - 1]
    current_int = (int(current_char) - count_b) % 10
    if DEBUG:
        print(f"Processing character: {current_char}, current_int: {current_int}, count_b: {count_b}")
    count_b += current_int
    count_a += 1

print(count_a + count_b)


