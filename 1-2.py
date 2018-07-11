x=int(input('Input the value of X:'))
y=int(input('Input the value of Y:'))
if x>0 and y>0 :
    print('point(',x,',',y,') is on 1st dimension')
elif x<0 and y>0 :
    print('point(',x,',',y,') is on 2st dimension')
elif x<0 and y<0 :
    print('point(',x,',',y,') is on 3st dimension')
elif x>0 and y<0 :
    print('point(',x,',',y,') is on 4st dimension')
elif x==0 and y!=0:
    print('point(',x,',',y,') is on Line Y')
elif x!=0 and y==0:
    print('point(',x,',',y,') is on Line X')
elif x==0 and y==0:
    print('point(',x,',',y,') is on original point')
