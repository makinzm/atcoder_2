from arc173.a import (
    solve,
    _get_num_neq,
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
