from user import user

class faculty(user):

    def __init__(self,name,password,designation,sub):
        super().__init__(name,password)
        self.designation=designation
        self.subject=sub

