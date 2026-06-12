#displacement equation
#v = u + at

u = int(input("Enter Initial Velocity: "))
a = int(input("Enter Acceleration: "))
t = int(input("Enter Time in seconds: "))

def calculate(): 
   v = u + a * t
   print(f"{v} m/s")

calculate()  

