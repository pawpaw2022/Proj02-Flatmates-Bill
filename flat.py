class Bill:
    """
    Object that contains data of a bill, such as
    total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount  # 'option + enter + enter' for shortcut
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, other_mate):
        weight = self.days_in_house / (self.days_in_house + other_mate.days_in_house)
        to_pay = weight * bill.amount
        return to_pay


