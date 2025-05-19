a=int(input("Enter first Value:"))
b=int(input("Enter Second Value:"))
c=int(input("Enter Third Value:"))
if((a>b)and(a>c)):
    print("biggest({},{},{})={}".format(a,b,c,a))
elif((b>a)and(b>c)):
    print("biggest({},{},{})={}".format(a,b,c,b))
elif((c>a)and(c>b)):
    print("biggest({},{},{})={}".format(a,b,c,c))
elif((a==b)and(a==c)):
    print("All values are equal")        