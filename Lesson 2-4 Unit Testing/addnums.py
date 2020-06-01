def addNums(num: str) -> int:
    """Adds up all digits in `num`

    Preconditions: `num` contains only digits
    Postconditions: returns sum of digits in `num`
    """
    sum = 0
    for digit in num:
        sum += int(digit)

    return sum

def test_addNums():
    assert addNums('123') == 6

if __name__ == "__main__":
    # Add this to use debugger to step through unit test code
    test_addNums()

