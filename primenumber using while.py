i=1
n=int(input("n:"))
count=0
while(i<=n+1):
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print(n,"is prime")
else:
    print(n,"is not prime")
        
