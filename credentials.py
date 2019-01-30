class Credentials:
    ''''
    class that generates instances of credentials
    '''
    pass
    credential_list = []
    def __init__(self,credential_detail,password,):
        '''__init__ methods helps us define properties for our objects
        '''
        #this is an example of a comment
        self.credential_detail = credential_detail
        self.password = password
    
    #credential_list = [] # Empty credential list
    def save_credential(self):
        '''save_credential method saves credentials objects into list
        '''
        Credentials.credential_list.append(self)