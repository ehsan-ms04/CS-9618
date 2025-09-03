import datetime as dt
class LibraryItem:
    def __init__(self, t, a ,i):
        self.__title = t
        self.__authorartist = a
        self.__itemid = i
        self.__onloan = False
        self.__duedate = dt.date.today()

    def gettitle(self):
        return(self.__title)

# other get methods go here

    def borrowing(self):
        self.__onloan = True
        self.__duedate = self.__duedate + dt.timedelta(weeks=3)

    def returning(self):
        self.__onloan = False

    def printdetail(self):
        print(self.__title,'',self.__authorartist)
        print(self.__itemid,'',self.__onloan,'',self.__duedate)

class book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i)
        self.__isrequested = False
        self.__requestedby = 0
    def getisrequested(self):
        return(self.__isrequested)
    def setrequested(self):
        self.__isrequested = True