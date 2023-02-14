from user import user

class student(user):
    def __init__(self,name,password,sem,cgpa,major):
        super().__init__(name,password)
        self.semester=sem
        self.cgpa=cgpa
        self.major=major

    