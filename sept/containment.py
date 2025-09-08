class Lesson:
    #constructor
    def __init__(self, l, d, req,):
        self.__lessontitle = ""
        self.__durationmins = 0
        self.__requireslab = False

    def Outputlessondetails(self):
    print("Lesson Title:",self.__lessontitle)
    print("Duration (Mins):",self.__durationmins)
    print("Requires Lab:", self.__requireslab)

    def setlesTitle(self):
        self.__lessontitle = l
    def getlesTitle(self):
        return self.__lessontitle
    def setduration(self):
        self.__durationmins = d
    def getduration(self):
        return self.__durationmins
    def needlab(self):
        self.__requireslab = True
    def GetLabReq(self):
        return self.__requireslab

class Assessment:
    #constructor
    def __init__(self, astitle, maxmark):
        self.__assessmenttitle = ""
        self.__maxmark = 0
    def setTitle(self):
        self.__assessmenttitle = astitle
    def getTitle(self):
        return self.__assessmenttitle
    def setMark(self):
        self.__maxmark = maxmark
    def getMark(self):
        return self.__maxmark
    def Outputassessmentdetails(self):
        print("Assessment Title:",self.__assessmenttitle)
        print("Max Marks:",self.__maxmark)

class course:
    def __init__(self,coursetit, maxstud, students):
        self.__coursetitle = ""
        self.__maxstudents = 0
        self.__numberofstudents = students
        self.__courselesson = []
        self.__courseassessment = Assessment()

    def addlesson(self):

