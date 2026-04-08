import json
import sys
from datetime import datetime

user = None
max_budget = 100000
with open("data/user.json", "r") as file:
    user = json.load(file)
user_budget = user['budget'] + user['credit']
print(user_budget)
if(user_budget < 0 or user_budget > max_budget):
    print("Budzet ne sme da bude manji od 0 ili veci od 100.000")
    sys.exit()

print(f"Dobar dan. Dobrodosli nazad, Vas budzet iznosi {user_budget}")

expense = 0

while(expense <= 0 or expense>user_budget):
    expense = int(input("Unesite iznos Vaseg troska: "))

with open("logs/expense_log.txt", "a") as file:
    expense_log = None
    expense_log = f"Amount: {expense}, User: {user['id']}, DateTime: {datetime.now()}, Budget: {user_budget}, Remaining budget: {user_budget-expense}\n"
    file.write(expense_log)
