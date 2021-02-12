name = input("Hi, what is ur name:  ").title()
income = int(input(f"hi {name}, what is your annual salary:  "))
#tax calculator
if income <= 12500:
    tax = 0
elif income <= 50000:
    tax = (income - 12500) * 0.20
elif income <= 150000:
    tax = (income - 50000) * 0.40 + 7500
elif income >= 150001:
    tax = (income - 150000) * 0.45 + 7500 + 40000
#asks if the user wants to use this calculator or not
q1 = int(input(f"So {name}, if you want to carry on using the tax and net salary calculator, type '1' and if you don't want to use it, type '2':  "))

if q1 == 1:
#asks the user if they want to know tax, net salary or both  
  q2 = int(input("if you want to ONLY KNOW YOUR TAXES, type '1'; if you want to ONLY KNOW YOUR NET SALARY, type '2'; if you want to know BOTH OF THEM, type '3':  "))
  if q2 == 1:
#asks the user what they want to know about their tax
    print("\nIf you want to know your daily tax, type '1' below; if you want to know your weekly tax, type '2' below; if you want to know your monthly tax, type '3' below; if you want to know all of them, type '4' below; if you want to know your yearly tax, type 5 below:  ")

    tax_amount = int(input("\nType which option you want here:  "))
#if statement for the option which they picked
    if tax_amount == 1:
      print("\nYour daily tax is £" + str(round(tax / 365, 2)))
    elif tax_amount == 2:
      print("\nYour weekly tax is £" + str(round(tax / 52, 2)))
    elif tax_amount == 3:
      print("\nYour monthly tax is £" + str(round(tax / 12, 2)))
    elif tax_amount == 4:
      print("\nYour tax per day is £" + str(round(tax / 365, 2)) +", your weekly tax is £" + str(round(tax / 52, 2)) +", your monthly tax is £" + str(round(tax / 12, 2)) +", your yearly tax is £" + str(round(tax, 2)))
    elif tax_amount == 5:
      print("\nYour yearly tax is £" + str(round(tax, 2)))
    else:
      print("\nInvalid Option!")
  elif q2 == 2:
#asks what they want to know about their net salary
    print("\nIf you want to know your daily net salary, type '1' below; if you want to know your weekly net salary, type '2' below; if you want to know your monthly net salary, type '3' below; if you want to know all of them, type '4' below; if you want to know your yearly net salary, type '5':  ")

    net=int(input("\nType which option you want here:  "))
#if statement for the option which they picked 
    if net == 1:
      print("\nYour daily net salary is £" + str(round((income-tax)/365, 2)))
    elif net == 2:
      print("\nYour weekly net salary is £" + str(round((income-tax)/52, 2)))
    elif net == 3:
      print("\nYour monthly net salary is £" + str(round((income-tax)/12, 2)))
    elif net == 4:
      print("\nYour net salary per day is £" + str(round((income-tax)/365, 2)) + ", your weekly net salary is £" + str(round((income-tax)/52, 2)) + ", your monthly net salary is £" + str(round((income-tax)/12, 2)) + " and your yearly net salary is £" + str(round(income-tax,  2)))
    elif net == 5:
      print("\nYour yearly net salary is £" + str(round(income-tax,  2)))
    else:
      print("\nInvalid Option!")
  elif q2 == 3:
#elif statement if they pick that they want to know about their taxes and net salary
    print("\nIf you want to know your daily tax, type '1' below; if you want to know your weekly tax, type '2' below; if you want to know your monthly tax, type '3' below; if you want to know all of them, type '4' below; if you want to know your yearly tax, type 5 below:  ")

    tax_amount = int(input("\nType which option you want here:  "))
#options which they picked for the taxes
    if tax_amount == 1:
      print("\nYour daily tax is £" + str(round(tax / 365, 2)))
    elif tax_amount == 2:
      print("\nYour weekly tax is £" + str(round(tax / 52, 2)))
    elif tax_amount == 3:
      print("\nYour monthly tax is £" + str(round(tax / 12, 2)))
    elif tax_amount == 4:
#prints everything for tax if they picked option 4
      print("\nYour tax per day is £" + str(round(tax / 365, 2)) +", your weekly tax is £" + str(round(tax / 52, 2)) +", your monthly tax is £" + str(round(tax / 12, 2)) +", your yearly tax is £" + str(round(tax, 2)))
    elif tax_amount == 5:
      print("\nYour yearly tax is £" + str(round(tax, 2)))
    else:
      print("\nInvalid Option!")

#asks what they want to know about their net salary
    print("\nIf you want to know your daily net salary, type '1' below; if you want to know your weekly net salary, type '2' below; if you want to know your monthly net salary, type '3' below; if you want to know all of them, type '4' below; if you want to know your yearly net salary, type '5':  ")

    net=int(input("\nType which option you want here:  "))
#option which they picked for their net salary
    if net == 1:
      print("\nYour daily net salary is £" + str(round((income-tax)/365, 2)))
    elif net == 2:
      print("\nYour weekly net salary is £" + str(round((income-tax)/52, 2)))
    elif net == 3:
      print("\nYour monthly net salary is £" + str(round((income-tax)/12, 2)))
    elif net == 4:
#prints everything for net salary if they picked option 4
      print("\nYour net salary per day is £" + str(round((income-tax)/365, 2)) + ", your weekly net salary is £" + str(round((income-tax)/52, 2)) + ", your monthly net salary is £" + str(round((income-tax)/12, 2)) + " and your yearly net salary is £" + str(round(income-tax,  2)))
    elif net == 5:
      print("\nYour yearly net salary is £" + str(round(income-tax,  2)))
    else:
      print("\nInvalid Option!")
#if they didn't pick any of the options for q2 it prints invalid option      
  else:
    print("\nInvalid Option!")
#prints thanks for coming anyways if they typed option 2 in q1
elif q1 == 2:
  print("\nThanks for coming anyways!")
#prints invalid option if they didn't pick any of the options in q1
else:
  print("\nInvalid Option!")
