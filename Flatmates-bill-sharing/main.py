import webbrowser

from fpdf import FPDF

from flat import Bill, Flatmate


class PdfReport:
    """
    Creates a pdf file that contains data such as flatmate's name, their due amount
    and the period for the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays_bill(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays_bill(bill, flatmate1), 2))

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
        pdf.cell(w=100, h=40, txt='Period: ', border=0, align='L')
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Add name and due amount for first flatmate and second flatmate
        pdf.set_font('Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0, align='L')
        pdf.cell(w=150, h=25, txt=flatmate1_pay, border=0, ln=1)
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0, align='L')
        pdf.cell(w=150, h=25, txt=flatmate2_pay, border=0, ln=1)

        pdf.output(self.filename)

        # Open a default browser with the pdf
        webbrowser.open(self.filename)


amount = float(input("Hey user enter the bill amount: "))
period = input("What is the bill period? E.g. December 2022: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during bill period? "))
name2 = input("What is your name? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during bill period? "))

the_bill = Bill(amount, period)
flatmate_1 = Flatmate(name1, days_in_house1)
flatmate_2 = Flatmate(name2, days_in_house2)

print(f"{flatmate_1.name} pays: ", flatmate_1.pays_bill(the_bill, flatmate_2))
print(f"{flatmate_2.name} pays: ", flatmate_2.pays_bill(the_bill, flatmate_1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate_1, flatmate_2, the_bill)



