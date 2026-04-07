import json

user = None
max_budget = 100000
with open("data/user.json", "r") as file:
    user = json.load(file)
user_budget = user['budget']
if(user_budget < 0 or user_budget > max_budget):
    print("Budzet ne sme da bude manji od 0 ili veci od 100.000")
