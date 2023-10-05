from django.contrib.auth import authenticate

username = 'my_username'
password = 'my_password'

user = authenticate(username=username, password=password)

if user is not None:
    # The user is authenticated.
    print("user exist")
else:
    # The user is not authenticated.
    print("user not exist")