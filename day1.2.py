
age = 17
age = int(input("enter the age"))

print("Welcome to Movie World!")

if age <=5:
     print("Your ticket is free!")

elif age < 13:
    print ("You get a 50% discount.")

elif age < 18:
    print ("You get a student discount.")

else:
    print("You have to pay the full ticket price.")

print("Enjoy your movie!")
