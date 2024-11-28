sandwich_orders = ["pastrami", "pesto", "pastrami", 
                   "cheese", "pastrami", "turkey and cheese"]
finished_sandwiches = []

print("We have run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
for sandwich in sandwich_orders:   
    print(f"I made your {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)
