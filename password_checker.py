# Write a function to generate a password that should have a combination of at least one number, one uppercase, one symbol and it is 6-20 char long.


password = input("Please enter a password with at least one number, one uppercase letter and one symbol. Password should be between 6 to 20 characters: ")


def password_checker(pswrd):
    check = False
    symbols = ["!", "@", "%", "&", "#", ".", "*", "/"]
    
    if len(pswrd) > 6 or len(pswrd) < 20:
        check = True
        
    if any(char.isdigit() for char in pswrd):
        check = True
    
    elif any(char.lower() for char in pswrd):
        check = True
        
    elif any(char.upper() for char in pswrd):
        check = True
        
    elif any(char in symbols for char in pswrd):
        check = True
        
    elif check == True:
        print("Valid password")
        
    else:
        print("Invalid password. You password must be between 6-20 characters long and it should have at least one number, one symbos, one uppercase character and one lowercase character")
        

print(password_checker(password))
    
        
        