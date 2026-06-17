def groundship_price(weight):
    if weight <= 2:
        return 1.5 * weight + 20
    if weight <= 6:
        return 3 * weight + 20
    if weight <= 10:
        return 4 * weight + 20
    else:
        return 4.75 * weight + 20
    
def droneship_price(weight):
    if weight <= 2:
        return 4.5 * weight
    if weight <= 6:
        return 9 * weight
    if weight <= 10:
        return 12 * weight
    else:
        return 14.25 * weight
    
statement = "Cost of shipping: $"

def cost():
    try:
        user_input = int(input("Choose a shipping option from the following: 1.Ground shipping 2.Ground shipping premium 3.Drone shipping: "))
        weight1 = float(input("Please state the weight of your package in LB: "))
        if user_input == 1:
            print(f"{statement}{groundship_price(weight1)}")
        elif user_input == 2:
            print(f"{statement}125.00")
        elif user_input == 3:
            print(f"{statement}{droneship_price(weight1)}")
        else:
            print("Invalid Shipping Option.")
    except ValueError:
        print("There is an error: Please make sure you have stated the weight correctly.")

cost()