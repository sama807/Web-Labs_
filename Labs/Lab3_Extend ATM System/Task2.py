
class Time:
    def __init__(self,hours=1,minutes=20,sec=10):
        self.hours=hours
        self.minutes=minutes
        self.seconds=sec
    @property
    def hours(self):
        return self.hours
    @hours.setter
    def hours(self,a):
        self.hours=a

    @property
    def minutes(self):
        return self.minutes

    @minutes.setter
    def minutes(self, a):
        self.minutes = a

    @property
    def seconds(self):
        return self.seconds

    @seconds.setter
    def seconds(self, a):
        self.seconds = a

    def addTime(self,t1,t2):
        if(t1.hours+t2.hours >12):
            self.hours = (t1.hours + t2.hours)%12
        else:
            self.hours = t1.hours + t2.hours
        if(t1.minutes + t2.minutes>60):
            self.minutes = (t1.minutes + t2.minutes)%12
        else:
            self.minutes = t1.minutes + t2.minutes
        if(t1.seconds+t2.seconds >60):
            self.seconds=t1.seconds+t2.seconds
        self.seconds = t1.seconds + t2.seconds
    def displayMinutes(self,t):
        print(t.minutes)

    def displayTwelve(self):
        if(self.hours>12):
            self.hours= self.hours%12
        if(self.minutes>60):
            self.minutes=self.minutes%60
        if(self.seconds>60):
            self.seconds=self.seconds%60
        print("Hours ",self.hours, "minutes ",self.minutes,"seconds ",self.seconds)
    def displayTwentyFour(self):
        print("Hours ",self.hours, "minutes ",self.minutes,"seconds ",self.seconds)





