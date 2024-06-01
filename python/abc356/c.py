import itertools

def count_valid_combinations(n, k, tests):
    tests = [test.split() for test in tests]
    success_numbers = []
    failed_numbers = []
    appeared_numbers = set()

    for result in tests:
        numbers = list(map(int, result[1:-1]))
        appeared_numbers.update(numbers)
        if result[-1] == "x":
            failed_numbers.append(numbers)
        else:
            success_numbers.append(numbers)

    candidates = set()
    for candidate in success_numbers:
        for comb in itertools.combinations(candidate, k):
            str_comb = tuple(sorted(comb))
            candidates.add(str_comb)

    not_appeared_numbers = set(range(1, n + 1)) - appeared_numbers
    if not_appeared_numbers:
        for not_appeared_number in not_appeared_numbers:
            remaining_numbers = set(range(1, n + 1)) - {not_appeared_number}
            for comb in itertools.combinations(remaining_numbers, k - 1):
                true_comb = tuple(sorted((*comb, not_appeared_number)))
                candidates.add(true_comb)

    for candidate in failed_numbers:
        for comb in itertools.combinations(candidate, k):
            str_comb = tuple(sorted(comb))
            candidates.discard(str_comb)

    return len(candidates)

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    tests = [input() for _ in range(m)]

    final_count = count_valid_combinations(n, k, tests)
    print(final_count)

