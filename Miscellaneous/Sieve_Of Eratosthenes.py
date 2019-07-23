# Sieve Of Eratosthenes
# Print prime numbers from 2 to n

n= 200

prime = [True for i in range(0,n+1)]

prime[0]=False
prime[1]=False

p = 2

while(p*p<=n):
    if(prime[p]==True):
        for i in range(p*p,n+1,p):
            prime[i]=False
    p+=1
    
# Printing results
for i in range(0,n+1):
    if(prime[i]):
        print(str(i),"Prime")
    else:
        print(str(i),"Non-Prime")
