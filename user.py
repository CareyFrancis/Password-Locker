import pyperclip

class User:
    '''
    class that generates new instances of user
    '''
    user_list = []
    def __init__(self,user_name,password,email,):
        '''__init__ methods helps us define properties for out objects
        '''
        #this is an example of a comment
        self.user_name = user_name
        self.password = password
        self.email = email