age = int(input("What is your age:  "))
height = float(input("\nWhat is your height in metres:  "))
weight = float(input("\nWhat is your weight in Kg:  "))
bmi= weight/height**2
if age < 2:
  print("Sorry, we can't calculate the BMI for this person")
elif age == 2:
    if bmi <= 14.9:
      print("You're underweight")
    elif bmi <=18:
      print("You're a healthy weight")
    elif bmi <=19.1:
      print("You're overweight")
    elif bmi >19.1:
      print("You're obese")
elif age == 3:
    if bmi <= 14.4:
      print("You're underweight")
    elif bmi <= 17.6:
      print("You're a healthy weight")
    elif bmi <=18.4:
      print("You're overweight")
    elif bmi >18.4:
      print("You're obese")
elif age == 4:
    if bmi <= 14:
      print("You're underweight")
    elif bmi <= 17:
      print("You're a healthy weight")
    elif bmi <=18:
      print("You're overweight")
    elif bmi >18:
      print("You're obese")
elif age == 5:
    if bmi <= 14.1:
      print("You're underweight")
    elif bmi <= 16.9:
      print("You're a healthy weight")
    elif bmi <=18.1:
      print("You're overweight")
    elif bmi >18.1:
      print("You're obese")
elif age == 6:
    if bmi <= 13.7:
      print("You're underweight")
    elif bmi <= 17:
      print("You're a healthy weight")
    elif bmi <=18.5:
      print("You're overweight")
    elif bmi >18.5:
      print("You're obese")
elif age == 7:
    if bmi <= 13.5:
      print("You're underweight")
    elif bmi <= 17.5:
      print("You're a healthy weight")
    elif bmi <=19:
      print("You're overweight")
    elif bmi >19:
      print("You're obese")
elif age == 8:
    if bmi <= 13.6:
      print("You're underweight")
    elif bmi <= 18:
      print("You're a healthy weight")
    elif bmi <=20:
      print("You're overweight")
    elif bmi >20:
      print("You're obese")
elif age == 9:
    if bmi <= 14:
      print("You're underweight")
    elif bmi <= 18.5:
      print("You're a healthy weight")
    elif bmi <=21:
      print("You're overweight")
    elif bmi >21:
      print("You're obese")
elif age == 10:
    if bmi <= 14.3:
      print("You're underweight")
    elif bmi <= 19.5:
      print("You're a healthy weight")
    elif bmi <=22.2:
      print("You're overweight")
    elif bmi >22.2:
      print("You're obese")
elif age == 11:
    if bmi <= 14.4:
      print("You're underweight")
    elif bmi <= 20.2:
      print("You're a healthy weight")
    elif bmi <=23.1:
      print("You're overweight")
    elif bmi >23.1:
      print("You're obese")
elif age == 12:
    if bmi <= 15:
      print("You're underweight")
    elif bmi <= 21:
      print("You're a healthy weight")
    elif bmi <=24.3:
      print("You're overweight")
    elif bmi >24.3:
      print("You're obese")
elif age == 13:
    if bmi <= 15.5:
      print("You're underweight")
    elif bmi <= 22:
      print("You're a healthy weight")
    elif bmi <=25:
      print("You're overweight")
    elif bmi >25:
      print("You're obese")
elif age == 14:
    if bmi <= 16:
      print("You're underweight")
    elif bmi <= 22.6:
      print("You're a healthy weight")
    elif bmi <=26:
      print("You're overweight")
    elif bmi >26:
      print("You're obese")
elif age == 15:
    if bmi <= 16.5:
      print("You're underweight")
    elif bmi <= 23.4:
      print("You're a healthy weight")
    elif bmi <=26.8:
      print("You're overweight")
    elif bmi >26.8:
      print("You're obese")
elif age == 16:
    if bmi <= 17:
      print("You're underweight")
    elif bmi <= 24.2:
      print("You're a healthy weight")
    elif bmi <=27.5:
      print("You're overweight")
    elif bmi >27.5:
      print("You're obese")
elif age == 17:
    if bmi <= 17.6:
      print("You're underweight")
    elif bmi <= 25:
      print("You're a healthy weight")
    elif bmi <=28.5:
      print("You're overweight")
    elif bmi >28.5:
      print("You're obese")
elif age == 18:
    if bmi <= 18.2:
      print("You're underweight")
    elif bmi <= 25.7:
      print("You're a healthy weight")
    elif bmi <=29:
      print("You're overweight")
    elif bmi >29:
      print("You're obese")
elif age == 19:
    if bmi <= 18.5:
      print("You're underweight")
    elif bmi <= 26.5:
      print("You're a healthy weight")
    elif bmi <=29.5:
      print("You're overweight")
    elif bmi >29.5:
      print("You're obese")
elif age == 20:
    if bmi <= 19:
      print("You're underweight")
    elif bmi <= 27:
      print("You're a healthy weight")
    elif bmi <=30.9:
      print("You're overweight")
    elif bmi >30.9:
      print("You're obese")
elif age > 20:
    if bmi < 18.50:
      print("You're underweight")
    elif bmi < 25:
      print("You're a healthy weight")
    elif bmi < 30:
      print("You're overweight")
    elif bmi > 30:
      print("You're obese")
