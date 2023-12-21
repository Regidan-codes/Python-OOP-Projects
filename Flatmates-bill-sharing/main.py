class Bill:
    """
    Object that contains data about bill, such as total amount and period of the bill
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate who pays the share of the bill
    """
    def __init__(self, name, days_in_house):
        self.days_in_house = days_in_house
        self.name = name

    def pays_bill(self):
        pass


class PdfReport:
    """
    Creates a pdf file that contains data such as flatmate's name, their due amount
    and the period for the bill
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass