for i in range(1,100):
    i_status=1
    k=int(pow(i,0.5))
    if i==1:
        continue;
    elif i==2:
        print(i)
        continue;
    elif i%2==0:
        continue;
    else:
        for j in range(2,k+1):
            if i%j==0:
                i_status=0
                break;
        if i_status==1:
            print(i)
