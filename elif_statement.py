def hint_usename(username):
    if len(username) < 3:
        print("invalid username. must be atleast 3 characters long")
    elif len(username) > 15:
            print("invalid username. must be at most 15 characters long")
        else:
            print("valid username")
