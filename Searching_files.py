
data = ['Name.py','DOB.py','Class.py','Age.py','Height.py']

file = input("Enter the file name you are looking for: ")

if file in data:
    print('The file you are looking for is present in data')
else:
    print('Sorry search somewhere else')
