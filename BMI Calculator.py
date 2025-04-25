weight = float(input("Tell me your weight in kg: "))
height = float(input ("Now tell me your height in meters: "))
bmi = weight / (height ** 2)
print (f"\nYour BMI is: {bmi:.2f}\n")
if bmi < 18.5:
    print ("😍 You are undeweight")
    print ("I recommend you to work out 🦾 and eat more protein 🥩")
elif (18.5 <= bmi < 24.9):
    print ("😊You have normal weight")
    print ("You better just work out and eat healthy food 🥗")
elif (24.9 <= bmi < 29.9):
    print ("🔴You are overweight")
    print ("You need to be more active and eat less junk food 🍔")
else: 
    print ("😥You are obese")
    print ("just work out and be more active and poop more 💩")