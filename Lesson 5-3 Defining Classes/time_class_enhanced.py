from typing import ClassVar

class Time:

    hours__: int
    minutes__: int

    tz_offset: ClassVar[int] = -5
    
    def __init__(self, hours: int, minutes: int):
        assert 0 <= minutes <= 59 and 0 <= hours <= 23 
        self.hours__ = hours
        self.minutes__ = minutes

    def secondsSinceMidnight(self) -> int:
        return self.minutes__ * 60 + self.hours__ * 60 * 60

    def addMinutes(self, minutes: int):
        self.hours__ = (self.hours__ + (self.minutes__ + minutes) // 60)
        self.minutes__ = (self.minutes__ + minutes) % 60

    def addHours(self, hours: int):
        self.addMinutes(hours * 60)

    def getMinutes(self) -> int:
        return self.minutes__

    def setMinutes(self, minutes: int):
        assert 0 <= minutes <= 59
        self.minutes__ = minutes

    def getHours(self) -> int:
        return self.hours__

    def setHours(self, hours: int):
        assert 0 <= hours <= 23 
        self.hours__ = hours

    def getTimezoneHour(self) -> int:
        return (self.hours__ + Time.tz_offset) % 24

    def __str__(self) -> str:
        return f"{self.hours__}:{self.minutes__:02}"


def test_Time_constructor():
    c = Time(5, 15)
    assert c.getHours() == 5
    assert c.getMinutes() == 15

def test_Time_str():
    c = Time(10, 5)
    assert str(c) == "10:05"

def test_Time_addMinutes():
    c = Time(5, 45)
    c.addMinutes(120)
    assert c.getHours() == 7
    assert c.getMinutes() == 45

def test_Time_secondSinceMidnight():
    c1 = Time(2, 10)
    assert c1.secondsSinceMidnight() == 2 * 60 * 60 + 10 * 60

    c2 = Time(0, 30)
    assert c2.secondsSinceMidnight() == 30 * 60

def test_Time_getTimezoneHour():
    Time.tz_offset = 0
    c = Time(3, 45)
    assert c.getTimezoneHour() == 3

    Time.tz_offset = -5
    c = Time(3, 45)
    assert c.getTimezoneHour() == 22
