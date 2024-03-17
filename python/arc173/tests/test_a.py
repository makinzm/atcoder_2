from arc173.a import (
    solve,
    _get_num_neq,
    _get_same_digits_neq_number,
    _get_less_digits_neq_number,
)

class TestSolve:
    def test_sample_1(self):
        assert solve(1) == 1
        assert solve(25) == 27
        assert solve(148) == 173
        assert solve(998244353) == 2506230721

class TestGetNumNeq:
    def test_my_sample(self):
        assert _get_num_neq(1) == 1
        assert _get_num_neq(9) == 9
        assert _get_num_neq(10) == 10
        assert _get_num_neq(11) == 10
        assert _get_num_neq(99) == 9 + 81 
        assert _get_num_neq(100) == 9 + 81
        assert _get_num_neq(999) == 9 + 81 + 729
        assert _get_num_neq(1000) == 9 + 81 + 729

class TestGetSameDigitsNeqNumber:
    def test_my_sample(self):
        assert _get_same_digits_neq_number(1) == 1
        assert _get_same_digits_neq_number(9) == 9
        assert _get_same_digits_neq_number(10) == 1
        assert _get_same_digits_neq_number(11) == 0
        assert _get_same_digits_neq_number(99) == 81
        assert _get_same_digits_neq_number(100) == 0
        assert _get_same_digits_neq_number(999) == 729
        assert _get_same_digits_neq_number(1000) == 0

class TestGetLessDigitsNeqNumber:
    def test_my_sample(self):
        assert _get_less_digits_neq_number(1) == 0
        assert _get_less_digits_neq_number(9) == 0
        assert _get_less_digits_neq_number(10) == 9
        assert _get_less_digits_neq_number(11) == 9
        assert _get_less_digits_neq_number(99) == 9
        assert _get_less_digits_neq_number(100) == 9 + 81
        assert _get_less_digits_neq_number(999) == 9 + 81
        assert _get_less_digits_neq_number(1000) == 9 + 81 + 729
