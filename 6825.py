w=float(input())
h=float(input())
bmi=w/(h**2)
print("Overweight" if bmi>25 else "Normal weight" if bmi>18.5 else "Underweight")