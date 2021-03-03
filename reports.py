import os
import webbrowser

from fpdf import FPDF
from filestack import Client


class PdfReport():
    """
    Creates a PDF that contains data about the flatmate, such as
    their name, their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill=bill, other_mate=flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill=bill, other_mate=flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert icon
        pdf.image(name='files/house.png', w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', align='C', ln=1)

        # Insert Period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period: ')
        pdf.cell(w=150, h=40, txt=bill.period, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=20, txt=flatmate1.name)
        pdf.cell(w=150, h=20, txt=flatmate1_pay, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=100, h=20, txt=flatmate2.name)
        pdf.cell(w=150, h=20, txt=flatmate2_pay, ln=1)

        pdf.output(f"files/{self.filename}")

        # Automatically view a PDF file
        os.chdir('files')  # change the path of searching
        # webbrowser.open(self.filename) # if you are on Windows OS
        path_pdf = os.path.abspath(self.filename)  # if you are on Mac OS
        webbrowser.get('safari').open_new_tab(f'file:///{path_pdf}')


class FileSharer():
    """
    A generator that generates a URL of the file you choose to upload
    """

    def __init__(self, filepath, apikey='ArFQU9ogfQ5uoneGAZTHqz'):
        self.filepath = filepath
        self.apikey = apikey

    def share(self):
        client = Client(self.apikey)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
