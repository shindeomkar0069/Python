print("-----------------------------")
print("----Ticket Pricing Softer----")
print("-----------------------------")

print("Plese enter your Age")
Age=int(input())

if(Age<=5):
    print("Your ticket is free")
elif(Age>5 and Age<=18):
    print("Your ticket price is : 900")
elif(Age>18 and Age<=40):
    print("Your ticket price is :1200")
else:
    print("Your ticket price is 400")