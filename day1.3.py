
print("Welcome to Student Result System")

name = input("Enter your name: ")
marks = int(input("Enter your marks (0-100): "))
print("\nStudent Name:", name)
print("Your Marks:", marks)
if marks < 0 or marks > 100:
    print("Invalid Marks! Please enter marks between 0 and 100.")
elif marks >= 80:
    print("Grade: A")
    print("Excellent Performance!")
elif marks >= 60:
    print("Grade: B")
    print("Good Work!")

elif marks >= 40:
    print("Grade: C")
    print("You need more practice.")

else:
    print("Grade: Fail")
    print("Better luck next time!")

print("\nThank you for using Student Result System.")
