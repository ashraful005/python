import math
m=int(input())
n=int(input())
a=int(input())
if n%a==0:
	p=n/a
else:
	p=int(n/a)+1
if m%a==0:
	q=m/a
else:
	q=int(m/a)+1
flagstones=math.ceil(p*q)
print(flagstones)