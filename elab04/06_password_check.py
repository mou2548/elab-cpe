PASSWORD = "I love Python"
attempt = 0
while attempt < 3:
    userInput = input("Enter the password: ")
    if userInput != PASSWORD:
        attempt += 1
        print(f"Wrong password, attempt #{attempt}")
        print("Access not allowed")
    else:
        print("Correct password")
        print("Access allowed")
        break
if attempt == 3:
    print("Maximum attempts exceeded")
    
