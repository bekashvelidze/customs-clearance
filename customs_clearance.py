from datetime import date
import math
import time


def calculate():
    current_date = date.today()
    current_year = current_date.year
    print('Here you can calculate car import and Customs clearance fees.')
    # receive input data
    capacity = float(input('Enter car engine capacity (e.g. 2500): '))
    year = int(input('Enter car production year: '))
    transit_days = int(input('Enter Transit days (1 - 60): '))
    # calculate car age
    age = current_year - year
    # calculate import rate according to official calculation formula
    import_rate = (capacity * 0.05) + (capacity * age * 0.0025)
    # initial rate value
    rate = 0
# check excise rate with car production year
    if age > 14:
        rate = 2.4
    elif age == 14:
        rate = 2.1
    elif age == 13:
        rate = 1.8
    elif age == 12:
        rate = 1.5
    elif age == 11:
        rate = 1.3
    elif age == 10:
        rate = 1.1
    elif age == 9:
        rate = 0.9
    elif age == 8 or age == 7 or age == 6:
        rate = 0.8
    elif age == 5:
        rate = 1.0
    elif age == 4:
        rate = 1.2
    elif age == 3:
        rate = 1.4
    elif age == 2 or age == 1 or age == 0:
        rate = 1.5
# calculate excise and final clearance price
    excise = capacity * rate
# Customs fee = 150 GEL, Expert assessment = 20 GEL, Customs declaration = 30 GEL, Licence plate fee = 72 GEL
    final_price = import_rate + excise + 150 + 20 + 30 + 72 + transit_days
    print('Final price for your car import and Customs clearance is:', math.ceil(final_price))


calculate()
time.sleep(0.5)
# reset to make new calculation
reset = input("Enter 'yes' to make new calculation or 'no' to exit: - ")
if reset == 'yes':
    calculate()
else:
    time.sleep(1)
    print('Exiting')
    exit()
