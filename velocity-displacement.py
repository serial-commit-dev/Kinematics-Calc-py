# velocity-displacement equation
#v^2 = u^2 + 2as

int u = int(input("Enter final velocity (m/s) : "))
int a = int(input("Enter acceleration (m/s^2) : "))
int s = int(input("Enter displacement(m): "))

def calculate():
  velocity = u * u + 2 * a * s
  print(velocity,"m/s")

calculate()
