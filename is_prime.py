def is_prime(n):
    if n<=1:
        return n
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
    
check=int(input("enetr number: "))
if is_prime(check):
    print("it is prime number")
else:
    print("it is not prime")