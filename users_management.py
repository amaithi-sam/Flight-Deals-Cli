

class User_Management:
    def new_user(self):
        print("Welcome to Sam's Flight Club\n\t We find the best flight deals and email you..\n\n")
        f_name = input("What is your first name .? ")
        l_name = input("what is your Last name..? ")
        e_mail = input("what is your email..? ")
        r_email= input("Type your email again..? ")

        while not e_mail==r_email:
          print("email mis-match..! ")
          r_email = input("Type your email again..? ")

        print("You're in the club ")
        return f_name, l_name, e_mail

