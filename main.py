user_choice = int(input("1. Register \n2. Login \n"))

#TODO: Use bcrypt for hashing the password

#model db
email = "Email:  "
password = "Password: "

def registerForm():
    user_email = input(str("Email: "))
    user_confirmEmail = input(str("Confirm Email: "))

    # if user_email exits, try to login
    with open(r"db.txt", "r") as f:
        for index, line in enumerate(f):
            if user_email in line:
                print("This email is already used! Please try to login!")

    # if user_email is not equal with user_confirmEmail then print error
    if user_email != user_confirmEmail:
        error_message_register_email = "Your email doesn't match!"
        print(error_message_register_email)

    user_password = input(str("Password: "))
    user_confirmPassword = input(str("Confirm Password: "))

    # if user_password is not equal with user_confirmPassword then print error
    if user_password != user_confirmPassword:
        error_message_register_password = "Your password doesn't match!"
        print(error_message_register_password)

    users = open("db.txt", "w")
    users.write(email + user_email + password + user_password)
    users.close()

    print("Congrats! Succesfully registered!")

def loginForm():
    user_email = input(str("Email: "))
    user_password = input(str(" Password: "))

    # read if the user credentials are correct, if not throw error
    with open(r"db.txt", 'r') as f:
        for index, line in enumerate(f):
            if user_email in line:
                print('You logged in!')
                break
            else:
                print("Sorry! Something went wrong!")

if user_choice == 1:
    registerForm()

elif user_choice == 2:
    loginForm()

else:
    print("Sorry! Yo
