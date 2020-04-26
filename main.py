
def again():
  yn = input("Factor again? (Y/N): ")
  if yn == 'y' or 'Y':
    factoring()
  if yn == 'n' or 'N':
    print("Goodbye.")
    exit()
  else:
    print("Not an option, please type either y or n.")
    again()

#Function that factors user input
def factoring():
  InputNumber = int(input("Type the number you want to factor: "));
  for i in range(1, InputNumber + 1):
    if InputNumber % i == 0:
      print(i)
  #Puts user back to the menu
  print("Operation complete.")
  again()

#Calls Menu Function on Start
factoring()
