from collections.abc import Callable


def greet(name: str) -> str:
    """ Send a greeting to the  user"""
    return f"hello {name}"


def calculate_tip(
    amount: float, tip_percentage: float, people: int
)-> tuple[float, float, float]:
    """Calcualte tip amount payable"""
    if amount < 0:
        raise ValueError("Amoount can't  be  zero or less")
    if tip_percentage < 0:
        raise ValueError("Tip percentage can't be zero or less")
    if people < 1:
        raise ValueError("People cant be negative  oor zero")

    tip = round(amount * tip_percentage / 100 , 2)
    total = round( amount + tip , 2)
    per_person = round(total / people , 2)
    return tip,total,per_person


def run_calculator(
        ask: Callable[[str], str], say: Callable[[str], None]
) -> None:
    """Enter the required information"""

    name = ask("Enter your name: ")
    say(greet(name))

    amount = float(ask("Enter the billamount : "))
    tip_percentage = float(ask("Enter the tip_percentage: "))
    people = float(ask("Enter the number of people:"))
    tip, total, per_person = calculate_tip(amount,tip_percentage, people)

    say(f"Tip: Tsh{tip: .2f}")
    say(f"Total: Tsh{total: .2f}")
    say(f"Per person: Tsh{per_person: .2f}")    