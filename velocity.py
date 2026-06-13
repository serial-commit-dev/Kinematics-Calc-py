# Velocity Equation
# v = u + at

u = int(input("Enter initial velocity: "))
a = int(input("Enter acceleration: "))
t = int(input("Enter time(s): "))

def calculate():
  result = u + a * t
  print(result,"m/s")

calculate()
