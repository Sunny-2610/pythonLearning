age = int(input("Enter your age "))
has_id = input("Do you have an ID? (yes/no) ")

if age >= 18 and has_id.lower() == "yes":
    print ("You can enter")
else:
    print("Entry denied")