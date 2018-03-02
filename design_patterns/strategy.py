"""
The strategy pattern provides a way to dynamically decide behaviour during runtime
Since functions are first class varibles in python, this is easy to do!
In Java this behaviour is achieved slightly differently - the behaviours are in classes 
that implement a common interface, and are referred to from inside the class which is to be dynamically assigned a behavior.
"""
import types

class person:
    def __init__(self, name, speechType=None):
        self.name = name
        if speechType is not None:
            self.sayName = types.MethodType(speechType, self)
    def sayName(self):
        print(self.name)

def whisper(self):
    print(self.name.upper())

def shout(self):
    print(self.name.lower())

if __name__=='__main__':
    normalPerson = person('Aditya')
    quietPerson = person('Smit', speechType=whisper)
    loudPerson = person('Abhinav', speechType=shout)
    normalPerson.sayName()
    quietPerson.sayName()
    loudPerson.sayName()
