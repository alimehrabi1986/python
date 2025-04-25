age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? Answer with yes or no: ")
if age >= 18 and has_id.lower() == "yes":
    print("✅You are eligible to vote.")
else:
    print("❌You are not eligible to vote.")
