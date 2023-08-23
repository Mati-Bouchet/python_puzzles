# Write a function to generate a password that should have a combination of at least one number, one uppercase, one symbol and it is 6-20 char long.


password = input("Please enter a password with at least one number, one uppercase letter and one symbol. Password should be between 6 to 20 characters: ")


def password_checker(pswrd):
    check = True
    symbols = ["!", "@", "%", "&", "#", ".", "*", "/"]
    
    if len(pswrd) < 6 or len(pswrd) > 20:
        check = False
        print("Your password should be between 6-20 characters")
        
    if not any(char.isdigit() for char in pswrd):
        check = False
        print("Your password should have at least one number")
    
    elif not any(char.lower() for char in pswrd):
        check = False
        print("Your password should have at least one lowercase character")
        
    elif not any(char.upper() for char in pswrd):
        check = False
        print("Your password should have at least one uppercase character")
        
    
    elif not any(char in symbols for char in pswrd):
        check = False
        print("Your password should have at least one symbol")
        
    if check:
        print("Your password is valid")
        

password_checker(password)
    
        
        