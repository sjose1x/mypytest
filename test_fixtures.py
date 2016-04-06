import pytest

class Person:
    def greet(self):
        print "greet called ..."
        return "Hello World"
@pytest.fixture
def person():
    return Person()
def test_fix(person):
    greeting = person.greet()
    assert greeting == "Hi World"