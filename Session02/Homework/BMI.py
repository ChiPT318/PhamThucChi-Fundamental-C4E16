mass = int(input("How heavy are you in kg?"))
height = int(input("How tall are you in cm?"))
BMI = mass / ((height/100)**2)
if BMI < 16:
    print("Severely underweight")
else:
    if BMI < 18.5:
        print("Underweight")
    else:
        if BMI < 25:
            print("Normal")
        else:
            if BMI < 30:
                print("Overweight")
            else:
                print("Obese")
