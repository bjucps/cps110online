
def makeTime(hours: int, minutes: int) -> dict:
    return { "hours": hours, "minutes": minutes }

def getSeconds(c: dict) -> int:
    return c['minutes'] * 60 + c['hours'] * 60 * 60

def addMinutes(c: dict, minutes: int):
    c['hours'] = (c['hours'] + (c['minutes'] + minutes) // 60)
    c['minutes'] = (c['minutes'] + minutes) % 60

def addHours(c: dict, hours: int):
    addMinutes(c, hours * 60)

def toString(c: dict) -> str:
    return "{}:{:02}".format(c['hours'], c['minutes'])

# -------------- Unit tests --------------------

def test_makeTime():
    c = makeTime(5, 15)
    assert c['hours'] == 5
    assert c['minutes'] == 15

def test_addHours():
    c = makeTime(5, 45)
    addHours(c, 2)
    assert c['hours'] == 7
    assert c['minutes'] == 45

def test_addMinutes():
    c = makeTime(5, 45)
    addMinutes(c, 120)
    assert c['hours'] == 7
    assert c['minutes'] == 45

def test_toString():
    c = makeTime(10, 5)
    assert toString(c) == "10:05"

