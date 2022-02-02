from user import User


print("Users module")
def get_data():
    name = input("Enter your name: ")
    lname = input("Enter your lastname: ")
    return {'name':name, 'lname':lname}

