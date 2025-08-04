n=5

if n==2 :
    print("prime")
else:
    for i in range(2,n+1):
        if n%i==0:
            print("prime")
            break
    else:  # this else belongs to for
     print("not prime")
