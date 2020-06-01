# This example contains a function (roundIt) and some unit tests
#
# To experiment with this example, first install pytest using pip:
#
#    pip install pytest
#
# Then, run the unit tests:
#
#    pytest roundit.py

def roundIt(num: float) -> int:
    return int(num + .5)

def test_roundIt_rounds_up():
   assert roundIt(9.7) == 10

def test_roundIt_rounds_down():
   assert roundIt(8.2) == 8


if __name__ == "__main__":

    print('Here is the main program')
