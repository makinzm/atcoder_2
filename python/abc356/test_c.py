from c import count_valid_combinations

class TestCountValidCombinations:
    def test_case_1(self):
        n = 3
        k = 2
        tests = [
           "3 1 2 3 o",
           "2 2 3 x",
        ]
        assert count_valid_combinations(n, k, tests) == 2

    def test_case_2(self):
        n = 4
        k = 3
        tests = """3 1 2 3 o
3 2 3 4 o
3 3 4 1 o
3 4 1 2 o
4 1 2 3 4 x
        """.strip().split("\n")
        assert count_valid_combinations(n, k, tests) == 0

    def test_case_3(self):
        n = 11
        k = 9
        tests = """10 1 2 3 4 5 6 7 8 9 10 o
11 1 2 3 4 5 6 7 8 9 10 11 o
10 11 10 9 8 7 6 5 4 3 2 x
10 11 9 1 4 3 7 5 6 2 10 x
        """.strip().split("\n")
        assert count_valid_combinations(n, k, tests) == 8

    def test_case_4(self):
        n = 10
        k = 2 
        tests = ["1 1 x"]
        assert count_valid_combinations(n, k, tests) == 45

