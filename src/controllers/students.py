from src.models.students import StudentsModel, CourseModel, SessionModel

studentsModel = StudentsModel()
courseModel = CourseModel()
sessionModel = SessionModel()

class StudentsController():
    
    def createStudents(self, uid, names, lastnames, phone, email, semester, course):
        studentsModel.createStudents(uid, names, lastnames, phone, email, semester, course)
    
    def listStudents(self):
        return studentsModel.listStudents()

    def deleteStudents(self, id):
        studentsModel.deleteStudents(id)

    def listStudentsUnique(self, id):
        return studentsModel.listStudentsUnique(id)
    
    def updateStudents(self, names, lastnames, phone, email, semester, id):
        return studentsModel.updateStudents(names, lastnames, phone, email, semester, id)

class CourseController():
    
    def createCourse(self, names, semester):
        courseModel.createCourse(names, semester)
    
    def listCourses(self):
        return courseModel.listCourses()

    def deleteCourse(self, id):
        courseModel.deleteCourse(id)

class SessionController():

    def createSession(self, course, date, starttime, endtime):
        sessionModel.createSession(course, date, starttime, endtime)
    
    def listSessions(self):
        return sessionModel.listSessions()
    
    def deleteSession(self, id):
        sessionModel.deleteSession(id)