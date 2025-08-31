while True:
   try:
      a = int(input("Enter the first number:"))
      b = int(input("Enter the second number:"))
      print("What kind of operation do you want to perform?")
      print("Press + for addition\nPress - for subtraction\nPress * for multiplication\nPress / for division")

      o = input("Enter Operation: ")

      match(o):
          case "+":
           print(f"The result is: {a + b}")
          case "-":
            print(f"The result is: {a - b}")
          case "*":
            print(f"The result is: {a * b}")
          case "/":
            print(f"The result is: {a / b}")   
          case _:
            print("There was an error!")  
                   
      while(True):
        cont = input("Do you want to perform another calculation> (y/n):").lower()       
        if cont == 'n':
          print("Exiting Calculator, Good Bye!")
          exit()
        elif cont == 'y':
          break
        else:
           print("Please enter 'y' for yes or 'n' for no.")

   except ValueError:
        print("Invalid input! Please enter numbers only.")
   except Exception as e:
        print(f"An error occurred: {e}")


