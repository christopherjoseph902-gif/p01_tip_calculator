import pytest  # noqa: I001
from tipcalc import greet, calculate_tip, run_calculator


def test_for_greet_name_value() -> None:
    assert greet("Sabrina") == "Hello, Sabrina"

def test_if_calculator_return_value()-> None:
    assert calculate_tip(40.0, 15.0, 2) == (6.0, 46.0, 23.0)

def test_zero_tip_and_one_person()-> None:
    assert calculate_tip(25.0, 0.0, 1) == (0.0, 25.0, 25.0)

def test_negative_amount_is_rejected() -> None:
    with pytest.raises(ValueError, match="Amoount can't  be  zero or less"):
        calculate_tip(-0.1, 10.0, 1)

def test_negative_tip_is_rejected() -> None:
    with pytest.raises(ValueError, match="Tip percentage can't be zero or less"):
        calculate_tip(10.0, -0.1, 1)

def test_zero_people_is_rejected() -> None:
    with pytest.raises(ValueError, match="People cant be negative  oor zero"):
        calculate_tip(50.0, 20.0, 0 )

def test_nonnumeric_text_raise_value_error()-> None:
    with pytest.raises(ValueError, match="could not convert"):
        float("abc")

def test_interaction_use_injected_as_and_say() ->None:
    answer = iter(["Vao", "30", "20", "10", "2"])
    prompts: list[str] = []
    message: list[str] = []

    def ask(prompt: str) ->str:
        prompts.append(prompt)
        return next(answer)

    run_calculator(ask,message.append)

    assert len(prompts) == 4
    assert message == [
        "Hello, Vao",
        "Tip: Tsh  6.00",
        "Total: Tsh  36.00",
        "Per person: Tsh  3.60",
    ]