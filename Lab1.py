import math
eps=0.01
x=0.1
z=1
s=0
z1=1
i=1
while math.fabs(z)>eps:
    z1=math.sin(x)**i
    z=(-1)**(i-1)*z1/i
    s=s+z
    i=i+1
s=s-1
print(s)