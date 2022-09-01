# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

ibm = round(weight / height**2)

if ibm >= 35:
  print(f"Your BMI is {ibm}, you are "+'\033[1m'+"clinically obese."+"\033[0m")
elif ibm >= 30:
  print(f"Your BMI is {ibm}, you are "+'\033[1m'+"obese."+"\033[0m")
elif ibm >= 25:
  print(f"Your BMI is {ibm}, you are slightly "+'\033[1m'+"overweight."+"\033[0m")
elif ibm >= 18.5:
  print(f"Your BMI is {ibm}, you have a "+'\033[1m'+"normal weight."+"\033[0m")
else:
  print(f"Your BMI is {ibm}, you are "+'\033[1m'+"underweight."+"\033[0m")
  




