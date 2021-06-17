'''Price of a house is $1M.
If buyer has good credit,
they need to put down 10%
otherwise
they need to put down 20%.
Print the down payment.'''

price=1000000
good_credit=True
Bad_credit=False
g1=10/100*price
g2=20/100*price
if good_credit==g1:
    print(f"there downpayement is{g1}")
elif Bad_credit==g2:
    print(f"there downpayment is {g2}")