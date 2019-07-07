chars = 'abcdefghijklmnopqrstuvwxyz123456789!@#$%*()_'
import random
password = ''
pass_length = int(input("Enter the length of the password you want: "))
for m in range(pass_length):
     password += random.choice(chars)
print(password)
