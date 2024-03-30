from typing import Sequence

from pydantic import BaseModel
from pydantic.functional_validators import (
    AfterValidator,
)
from typing_extensions import Annotated


def check_between_one_and_hundred(n: int) -> bool:
    assert 1 <= n <= 100, f"n must be between 1 and 100, but got {n}"
    return n

class Input(BaseModel):
    n: Annotated[int, AfterValidator(check_between_one_and_hundred)]
    k: Annotated[int, AfterValidator(check_between_one_and_hundred)]
    a: Sequence[int]

def main(input_value: Input):
    base_ans_lst = list(
        map(
            lambda x: x // input_value.k,
            filter(lambda x: x % input_value.k == 0, input_value.a),
        ),
    )
    base_ans_lst.sort()
    [print(x, end=" ") for x in base_ans_lst]
    print()

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    input_value = Input.parse_obj(
        {
            "n": n,
            "k": k,
            "a": a,
        },
    )
    main(input_value)
