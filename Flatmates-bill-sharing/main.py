import webbrowser

from fpdf import FPDF


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

    def pays_bill(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = weight * bill.amount
        return to_pay


class PdfReport:
    """
    Creates a pdf file that contains data such as flatmate's name, their due amount
    and the period for the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        # Add a PDF standard format
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image("house.png", w=30, h=30)

        # Add title
        pdf.set_font('Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates bill', border=0, align='C', ln=1)

        # Add Row headings
        pdf.set_font('Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period: ', border=0, align='L', ln=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Add name and due amount for first flatmate and second flatmate
        pdf.set_font('Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0, align='L', ln=1)
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0, align='L', ln=1)
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        webbrowser.open(self.filename)
