import random
import string

n = int(input("Enter the Password's Lenght: "))
c = string.ascii_letters + string.punctuation + string.digits
p = ""
for i in range(n):
    p = p+random.choice(c)
print("Your Generated Password is:",p)    
