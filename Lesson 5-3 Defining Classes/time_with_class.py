class Time:

    hours: int
    minutes: int
    
    def __init__(self, hours: int, minutes: int):
        self.hours = hours
        self.minutes = minutes

    def secondsSinceMidnight(self) -> int:
        return self.minutes * 60 + self.hours * 60 * 60

    def addMinutes(self, minutes: int):
        self.hours = (self.hours + (self.minutes + minutes) // 60)
        self.minutes = (self.minutes + minutes) % 60

    def addHours(self, hours: int):
        self.addMinutes(hours * 60)

    def getMinutes(self) -> int:
        return self.minutes

    def setMinutes(self, minutes: int):
        self.minutes = minutes

    def getHours(self) -> int:
        return self.hours

    def setHours(self, hours: int):
        self.hours = hours

    def __str__(self) -> str:
        return f"{self.hours}:{self.minutes:02}"


def test_Time_constructor():
    c = Time(5, 15)
    assert c.hours == 5
    assert c.minutes == 15

def test_Time_str():
    c = Time(10, 5)
    assert str(c) == "10:05"

def test_Time_addMinutes():
    c = Time(5, 45)
    c.addMinutes(120)
    assert c.hours == 7
    assert c.minutes == 45

def test_Time_secondsSinceMidnight():
    c1 = Time(2, 10)
    assert c1.secondsSinceMidnight() == 2 * 60 * 60 + 10 * 60

    c2 = Time(0, 30)
    assert c2.secondsSinceMidnight() == 30 * 60
