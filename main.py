from user import User
from app import get_data

print("main file")

def create_user():
    data = get_data()
    user = User(data['name'], data['lname'])

    return user

user = create_user()
print(user)
