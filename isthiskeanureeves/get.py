def getUserDetails(userObject):
    user_dictionary = {}

    # Map a username to all the user's details
    user_dictionary[userObject.user.username] = {
        
        'email' : userObject.user.email,
     
      
        'picture' : userObject.picture if bool(userObject.picture) else False
       
    }

    return user_dictionary
