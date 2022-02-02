from user import User


print("Users module")
def get_data():
    name = input("Enter your name: ")
    lname = input("Enter your lastname: ")
    return {'name':name, 'lname':lname}


if __name__ == "__main__":
    data = get_data()

    name = data['name']
    lname = data['lname']

    print(name, lname)