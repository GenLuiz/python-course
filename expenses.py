expenses = [10.5, 8, 5, 15, 20, 5, 3]
total = 0

for expense in expenses:
    total = total + expense
print(f"you spent: R$", total, sep="")

# or

total = sum(expenses)
print("you spent: R$", total, sep=" ")


total = 0
expenses = []
num_expenses= int(input("enter # of expenses to sum:\n"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:\n")))
total = sum(expenses)
print(f"You spent R$", total)






