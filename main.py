MENU = {
    "espresso": {       
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

order_total = 0
take_order = False
def coin():
  qcoins = float(input("how many quarters?: "))
  dcoins = float(input("how many dimes?: "))
  ncoins = float(input("how many nickles?: "))
  pcoins = float(input("how many pennies?: "))

  tqcoins = quarter * qcoins
  tdcoins = dime * dcoins
  tncoins = nickel * ncoins
  tpcoins = penny * pcoins

  total_coins = float(tqcoins + tdcoins + tncoins + tpcoins)
  return total_coins
  print(f"customer paid: {total_coins}")
  
def calculate_cost(order):
  '''Calculates the change by getting the total coins by the customer and subtracting it by the cost of the drink'''
  cust_order = MENU[order]
  cust_order['cost']
  #print(f"{cust_order['cost']}")
  change = coin_check - cust_order['cost']
  cust_change = "{:.2f}".format(change)
  if change > 0:
    global order_total
    print(f"Here is your ${cust_change} change")
    print(f"Here is your {order} ☕️. Enjoy!!!")
    order_total += cust_order['cost']
    return cust_change
  elif change < 0:
    print("You do not have enough coins")

def resource_balance(report):
  cust_order = MENU[order]
  drink_ing = cust_order['ingredients']
  
  for drinks in drink_ing:
    if resources[drinks] >= drink_ing[drinks]:
      resources[drinks] -= drink_ing[drinks]
    elif resources[drinks] < drink_ing[drinks]:
      print(f"Sorry, we don't have enough {drinks}")
      return
  return True

quarter = float(0.25)
dime = float(0.10)
penny = float(0.01)
nickel = float(0.05)

while not take_order:
  order = input(" What would you like? (espresso/latte/cappuccino): ").lower()
  
  if order == "report":    
    print(f" Water: {resources['water']}ml")
    print(f" Milk: {resources['milk']}ml")
    print(f" Coffee: {resources['coffee']}ml")
    print(f" Money: ${order_total}")

  elif order == "espresso" or order == "latte" or order =="cappuccino":    
    if resource_balance(order):
      coin_check = coin()
      calculate_cost(order)
  else:
    take_order = True
   




