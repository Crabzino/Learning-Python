shipping_option = int(input("Choose one of the following shipping options:  1. Ground Shipping 2. Ground shipping premium, 3. Drone shipping"))
weight_of_package = float(input("What is the weight of your package in lb?"))

groundship_1 = 1.50 * weight_of_package + 20
groundship_2 = 3 * weight_of_package + 20
groundship_3 = 4 * weight_of_package + 20
groundship_4 = 4.75 * weight_of_package + 20

droneship_1 = 4.50 * weight_of_package
droneship_2 = 9.00 * weight_of_package
droneship_3 = 12.00 * weight_of_package
droneship_4 = 14.25 * weight_of_package

statement_1 = "Cost of shipping: $"

if shipping_option == 1 and weight_of_package <= 2:
  print(statement_1 + str(groundship_1))
elif shipping_option == 1 and weight_of_package <= 6:
  print(statement_1 + str(groundship_2))
elif shipping_option == 1 and weight_of_package <= 10:
  print(statement_1 + str(groundship_3))
elif shipping_option == 1 and weight_of_package > 10:
  print(statement_1 + str(groundship_4))
elif shipping_option == 2:
  print(statement_1 + "125.00")
elif shipping_option == 3 and weight_of_package <= 2:
  print(statement_1 + str(droneship_1))
elif shipping_option == 3 and weight_of_package <= 6:
  print(statement_1 + str(droneship_2))
elif shipping_option == 3 and weight_of_package <= 10:
  print(statement_1 + str(droneship_3))
elif shipping_option == 3 and weight_of_package > 10:
  print(statement_1 + str(droneship_4))
