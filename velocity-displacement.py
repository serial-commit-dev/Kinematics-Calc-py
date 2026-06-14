# velocity-displacement equation
#v^2 = u^2 + 2as

u = int(input("Enter final velocity: "))
a = int(input("Enter acceleration: "))
s = int(input("Enter displacement: "))

def calculate():
  velocity = u * u + 2 * a * s
  print(velocity,"m/s")

calculate()
