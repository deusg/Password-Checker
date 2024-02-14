# Password Check

password = 'cavaliers2016'

# Get passworkd from user
user_password = input('Enter your password: ')

# While password is not correct
while user_password != password:
    print('Sorry that is incorrect')
    # Get password from user
    user_password = input('Enter your password: ')

# Print correct
print("Success: You are correct")
