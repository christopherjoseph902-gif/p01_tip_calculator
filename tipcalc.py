from collections.abc import Callable #noqa

from datetime import datetime, timezone



def greet(name: str) -> str:
    """ Send a greeting to the  user"""
    return f"Hello, {name}"


def calculate_tip(
    amount: float, tip_percentage: float, people: int
)-> tuple[float, float, float]:
    """Calculate tip amount payable"""
    
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
        ask: Callable[[str], str], 
        say: Callable[[str], None],
        save:Callable[[float, float, int, float, str], int]
) -> None:
    """Enter the required information"""

    name = ask("Enter your name: ")
    say(greet(name))

    amount = float(ask("Enter the Bill_amount : "))
    tip_percentage = float(ask("Enter the tip_percentage: "))
    people = float(ask("Enter the number of people:"))
    
    tip, total, per_person = calculate_tip(amount,tip_percentage, people)

    created_at = datetime.now(timezone.utc).isoformat(timespec="seconds")

    row_id = save(
        amount,
        tip_percentage,
        people,
        per_person,
        created_at,
    )

    say(f"""Saved successfully! \nRecord 
    ID: {row_id}""")
    say(f"Tip: Tsh {tip: .2f}")
    say(f"Total: Tsh {total: .2f}")
    say(f"Per person: Tsh {per_person: .2f}")   