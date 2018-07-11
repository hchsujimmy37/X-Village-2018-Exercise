a=float(input('Input the power of second:'))
b=float(input('Input the power of single:'))
c=float(input('Input the power of zero:'))
print(a,'X^2+',b,'X+',c)
d=((-b)+pow(pow(b,2)-4*a*c,0.5))/(2*a)
e=((-b)-pow(pow(b,2)-4*a*c,0.5))/(2*a)
if d==e:
    print('The answer is ',d,'.')
elif (pow(b,2)-4*a*c)<0:
    print('Do not have real number.')
else:
    print('The answers are ',d,'and ',e,'.')
