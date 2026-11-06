from collections.abc import Callable

def greet(name: str) -> str:
    """Greet the user"""
    return f"Hello {name}"

def calculate_tip(
        amount:float, tip_percentage: float, people: int
) -> tuple [float, float, float]:
    """Calculate the tip  payable"""

    if amount < 0:
        raise ValueError("The amount less  be zero")
    if tip_percentage < 0:
        raise ValueError("The   tip_perxcentage can't less zero")
    if people < 1:
        raise ValueError("The number of  people cant be less than one")

    tip = round(amount * tip_percentage / 100, 2)
    total = round(amount + tip, 2)
    per_person = round(total / people, 2)
    return tip , total, per_person


def run_calculator(
        ask: Callable[[str], str], say:Callable[[str], None]
) -> None:
    """ Accepting input to run the calculation"""
    name =  ask("Enter your name: ")
    say(greet(name))

    amount =float(ask("What is the amount: "))
    tip_percentage = float(ask("Enter the tip percentage: "))
    people = int(ask("Enter number of people: "))
    tip, total, per_person = calculate_tip( amount, tip_percentage, people)


    say(f"Tip: Tsh{tip: .2f}")
    say(f"Total: Tsh{total: .2f}")
    say(f"Per person:Tsh{per_person: .2f}")