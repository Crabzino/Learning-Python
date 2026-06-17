user_name = input("Enter Username:")
match user_name:  
    case "Dave":  
        print("Get off my computer Dave!")  
    case "angela_catlady_87":  
        print("I know it is you, Dave! Go away!")   
    case "Codecademy":  
        print("Access Granted.")  
    case default:  
        print("Username not recognized.")  



food_choice = input("Do you want Chicken or Beef?")
match food_choice:
    case "Chicken":
        print("Sure, I will bring the chicken.")
    case "Beef":
        print("Sure, I will bring the beef")
    case default:
        print("Not Recognised")