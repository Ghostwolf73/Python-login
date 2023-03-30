while True:
    
    username = input("Enter a username:")
    password = input("Enter a password:")
    confirmPassword = input("Confirm your password:")

    if password == confirmPassword:
        print("Username " + username + " has been created")
        break
    else:
        print("Passwords do not match try again")

while True:
    loginUsername = input("Enter username to login:")
    loginPassword = input("Enter password to login:")

    if loginUsername == username and loginPassword == password:

        print("Welcome " + username + " you have access to the server.")
        break
    
    else:
        print("Access denied, try again")


        






