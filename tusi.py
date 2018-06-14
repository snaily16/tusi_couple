import math as m

def d_to_r(th_d):
	th_r = m.pi / 180.0 * th_d
	return th_r
	
r = int(input('Enter the radius of inner circle: '))
R = 2*r
cord = []
d = int(input('Enter the distance of point from radius of inner circle: '))

for i in range(0,360,10):
	t = d_to_r(i)
	x = r*m.cos(t) + d*m.cos(t)
	y = r*m.sin(t) - d*m.sin(t)
	cord.append([x,y])
	
print(cord)
