"""
From Wikipedia :The observer pattern is a software design pattern in which an object, 
called the subject, maintains a list of its dependents, called observers, and notifies 
them automatically of any state changes, usually by calling one of their methods.

It is used to implement event-driven architectures.
"""

class Observable():
    def __init__(self):
        self.__observers=[]
    def registerObserver(self, observer):
        self.__observers.append(observer)
    def unregisterObserver(self, observer):
        self.__observers.remove(observer)
    def notifyObservers(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)



class Observer():
    def __init__(self, observable):
        observable.registerObserver(self)
    def notify(self, observable, *args, **kwargs):
        print("got {0} and {1} from {2}".format(args, kwargs, observable))

mailingList = Observable()
recipient1 = Observer(mailingList)
recipient2 = Observer(mailingList)
mailingList.notifyObservers(1,2,3)
