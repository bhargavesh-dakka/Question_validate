from sql import *

def validate(user_name, passwd):
    if validate_user(user_name, passwd):
        user_answers = generate_questions()
        update_score(user_answers,user_name)
        print()
        print()
        display_score(user_name)

    else:
        print("Please enter valid credientials")
        print()

def main():
    while True:
        print()
        opt = input("Do you want to take quizz ?\na.Yes\tb.No\t:").lower()
        if opt not in "ab" or len(opt)>1:
            print("Please valid input ")
            print()

        elif opt == "a":
            while True:
                opt = input("Are you an Existing user ?\na.Yes\tb.No\t:").lower()
                if opt not in "ab" or len(opt)>1:
                    print("Please valid input ")
                    print()
#- -------------------Existing user -------------
                elif opt == "a":
                    print()
                    user_name = input("Enter your name : ")
                    passwd = input("Enter your password : ")
                    validate(user_name, passwd)
                    break
                    
#--------------------New user ---------------------
                else:
                    name = input("Please enter your name : ")
                    user_name = input("Enter username (note : username must be unique ) : ")
                    password = input("Enter password : ")
                    add_user(user_name, password, name)
                    validate(user_name, password)
                    break
                    
#------------------OPtion 'b' -----------------------              
        else:
            break
        
        
        

if __name__ == "__main__":
    print("fuck")

