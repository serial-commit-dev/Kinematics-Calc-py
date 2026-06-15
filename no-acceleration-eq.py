# s = 0.5(u+v)t

u = int(input("Enter final velocity: "))
v = int(input("Enter initial velocity: "))
t = int(input("Enter time in seconds: "))

def calculate():
  sum = u + v  
  result = 0.5 * sum * t
  print(result,"m")

calculate()
