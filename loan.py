money_owed = float(input("How much money you owe, in dollars?\n"))
apr = float(input("How much is the annual percentage rate?\n"))
payment = float(input("what will your montly payment be, in dollars?\n"))
months = int(input("How many months you will pay?\n"))

monthly_rate = apr/100/12

for i in range(months):
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if(money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("you paid off the loan in", i+1, "months")
        break
    money_owed = money_owed - payment

    print("Paid", payment, "of which", interest_paid, "was interest", end=' ')
    print("Now I owe", money_owed)
