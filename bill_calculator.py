def calculate_tip(bill_amount, tip_percentage):
    tip = bill_amount * tip_percentage * 0.01
    return tip


def calculate_total(bill_amount):
    total_bill = bill_amount + tip_amount
    return total_bill


#def calculate_total(bill_amount):
    #tip_amount = calculate_tip(bill_amount, tip_percentage)
    #total_bill = bill_amount + tip_amount
    #return total_bill

def bill_splitter(number_guests):
    cost_per_person = total_amount / number_guests
    return cost_per_person


tip_amount = calculate_tip(150, 20)
print "Total tip amount is " + str(tip_amount)


total_amount = calculate_total(150)
print "The total bill is " + str(total_amount)

per_person_amount = bill_splitter(2)
print "The bill per person is " + str(per_person_amount)
