from flat import Bill, Flatmate
from reports import PdfReport, FileSharer

# building User Interface
while True:
    try:
        amount = float(input('Hey user, please enter the bill amount: '))
        break
    except(ValueError):
        print('Invalid bill amount input, please enter a number')

period = input('What month is the bill period ? E.g. December 2020 : ')

name1 = input("What is the first flatmate's name ? ")
while True:
    try:
        days_in_house_1 = int(input(f'How many days did {name1} stay during that period ? '))
        break
    except(ValueError):
        print('Invalid days input, please enter a number')


name2 = input("What is the second flatmate's name ? ")
while True:
    try:
        days_in_house_2 = int(input(f'How many days did {name2} stay during that period ? '))
        break
    except(ValueError):
        print('Invalid days input, please enter a number')


the_bill = Bill(amount=amount, period=period)
mate1 = Flatmate(name=name1, days_in_house=days_in_house_1)
mate2 = Flatmate(name=name2, days_in_house=days_in_house_2)

print(f"{name1} will pay: ", round(mate1.pays(bill=the_bill, other_mate=mate2), 2))
print(f"{name2} will pay: ", round(mate2.pays(bill=the_bill, other_mate=mate1), 2))

pdf = PdfReport('bill.pdf')
pdf.generate(flatmate1=mate1, flatmate2=mate2, bill=the_bill)
url = FileSharer(pdf.filename)
print(url.share())

