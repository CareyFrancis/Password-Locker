class Credentials:
    ''''
    class that generates instances of credentials
    '''
    credential_list = []
    def __init__(self,credential_detail,password,):
        '''__init__ methods helps us define properties for our objects
        '''
        #this is an example of a comment
        self.credential_detail = credential_detail
        self.password = password