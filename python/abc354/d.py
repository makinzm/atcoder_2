def retrieve_start_block_index(a):
    """Retrieve the start block index of the block that contains the a-th element."""
    return a // 4

def retrieve_end_block_index(c):
    """Retrieve the end block index of the block that contains the c-th element."""
    return ( c + 3 ) // 4

def retrieve_bottom_block_index(b):
    return b // 2

def retrieve_top_block_index(d):
    return (d + 1) // 2

def calculate_one_block(minus_vertical_block_counter, bottom_block_index, top_block_index):
    base = 3
    summation = base * (top_block_index - bottom_block_index)

    for k,v in minus_vertical_block_counter.items():
        if k == 0:
            summation -= 2 * v
        else:
            summation -= v

    return summation

def calculate_two_block(minus_block_counter, start_block_index, end_block_index):
    base = 3
    summation = base * (end_block_index - start_block_index)

    for k,v in minus_block_counter.items():
        if k == 0:
            summation -= v
        else:
            summation -= 2 * v

    return summation

def calculate_three_block(minus_vertical_block_counter, bottom_block_index, top_block_index):
    base = 1
    summation = base * (top_block_index - bottom_block_index)

    for k,v in minus_vertical_block_counter.items():
        if k == 1:
            summation -= v

    return summation

def calculate_four_block(minus_block_counter, start_block_index, end_block_index):
    base = 1
    summation = base * (end_block_index - start_block_index)

    for k,v in minus_block_counter.items():
        if k == 0:
            summation -= v

    return summation

BASE_NUMBER = 10 ** 10

def solve(a,b,c,d):
    start_block_index = retrieve_start_block_index(a)
    end_block_index = retrieve_end_block_index(c)

    bottom_block_index = retrieve_bottom_block_index(b)
    top_block_index = retrieve_top_block_index(d)

    a += BASE_NUMBER
    b += BASE_NUMBER
    c += BASE_NUMBER
    d += BASE_NUMBER

    minus_block_counter = {i:0 for i in range(4)}

    if a % 4 != 0:
        for i in range(a % 4):
            minus_block_counter[i] += 1
    if c % 4 != 0:
        for i in range(c % 4, 4):
            minus_block_counter[i] += 1
    minus_vertical_block_counter = {i:0 for i in range(2)}

    if b % 2 != 0:
        for i in range(b % 2):
            minus_vertical_block_counter[i] += 1
    if d % 2 != 0:
        for i in range(d % 2, 2):
            minus_vertical_block_counter[i] += 1

    one_block = calculate_one_block(minus_vertical_block_counter, bottom_block_index, top_block_index)
    two_block = calculate_two_block(minus_vertical_block_counter, bottom_block_index, top_block_index)
    three_block = calculate_three_block(minus_vertical_block_counter, bottom_block_index, top_block_index)
    four_block = calculate_four_block(minus_vertical_block_counter, bottom_block_index, top_block_index)

    summation = (one_block + two_block + three_block + four_block) * (end_block_index - start_block_index)

    for k,v in minus_block_counter.items():
        if k == 0:
            summation -= one_block * v
        elif k == 1:
            summation -= two_block * v
        elif k == 2:
            summation -= three_block * v
        else:
            summation -= four_block * v

    debug = False
    if debug:
        print("one_block: ", one_block)
        print("two_block: ", two_block)
        print("three_block: ", three_block)
        print("four_block: ", four_block)
        print("summation: ", summation)

        print("minus_block_counter: ", minus_block_counter)
        print("minus_vertical_block_counter: ", minus_vertical_block_counter)

        print("start_block_index: ", start_block_index)
        print("end_block_index: ", end_block_index)
        print("bottom_block_index: ", bottom_block_index)
        print("top_block_index: ", top_block_index)


    return summation


if __name__ == "__main__":
    a,b,c,d = map(int, input().split())
    print(solve(a,b,c,d))

