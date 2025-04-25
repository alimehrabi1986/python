age = int (input("Enter uour age: "))
response = input("Do you have a valid ID? Answer with yes or no: ")

while response != "yes" and response != "no":
    print("⚡Please answer with 'yes' or 'no'.")
    response = input("Do you have a valid ID? Answer with yes or no: ").lower()

if age >= 18 and response == "yes":
    print("✅You are eligible to vote.")
else: 
    print("❌You are not eligible to vote.")