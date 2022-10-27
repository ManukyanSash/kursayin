"""
def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

def prime_number(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n//2+1):
            if (n%i) == 0:
                return False
        return True        

def digit_sum(n):
    sum = 0
    while(int(n) != 0):
        sum += n%10
        n = int(n/10)    
    return sum

if __name__ == "__main__":
    ml = []
    num = int(input("mutqagreq tiv: "))
    count = factorial(num)
    for i in range(count+1):
        if prime_number(digit_sum(i)) == True:
            ml.append(i) 
    for el in ml:
        print(el)        
        
"""

##############################

"""
num = int(input("mutqagreq tivy: "))
ml = []        
s = 1
for i in range(2,num+1):
    s *= i    

for i in range(2, s+1):
    prime = True
    ci = i
    summ = 0
    while int(ci) != 0:    
        summ += ci%10
        ci = int(ci/10)
    
    for j in range(2, summ//2+1):
        if summ%j == 0:
            prime = False
            break
    if prime:    
        ml.append(i)            

for el in ml:
    print(el)
    
"""    
import string


    