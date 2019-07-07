a = {'ana':'INDAN01','bna':'INDBN02','cna':'INDCN03'}
print("Welcome to the LifeTel Telecom")
c = input("Kindly enter your name: ")
if c in a:
    print("Hello", c, "kindly provide your reference id")
    e = input("Enter your reference ID")
    for e in a:
        print("Your SIM is ready")
        break
else:
    print("You are not authorized to buy a SIM")












