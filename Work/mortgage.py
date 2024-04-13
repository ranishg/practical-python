# mortgage.py
#
# Exercise 1.7, 1.8, 1.9 and 1.10

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
month = 1

while principal > payment:
    if extra_payment_start_month <= month <= extra_payment_end_month:
        principal = principal * (1 + rate / 12) - payment - extra_payment
        total_paid += payment + extra_payment
    else:
        principal = principal * (1 + rate / 12) - payment
        total_paid += payment

    print(month, round(total_paid, 2), round(principal, 2))
    month += 1

total_paid += principal
print(month, round(total_paid, 2), 0)

print(
    "Total payments of {} made over {} months".format(round(total_paid, 2), month - 1)
)
