from src.connection_db.db import mysql

class StudentsModel():

    def createStudents(self, uid, names, lastnames, phone, email, semester, course):
        cursor = mysql.get_db().cursor()
        cursor.execute('INSERT INTO students (uid, names,lastnames,phone,email,semester, course) VALUES (%s, %s,%s,%s,%s,%s,%s)',
                       (uid, names, lastnames, phone, email,semester,course,))
        mysql.get_db().commit()
        cursor.close()

    def deleteStudents(self, id):
        cursor = mysql.get_db().cursor()
        cursor.execute("DELETE FROM students WHERE id = %s", (id,))
        mysql.get_db().commit()
        cursor.close()

    def listStudents(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        cursor.close()
        return students
    
    def listStudentsUnique(self, id):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
        students = cursor.fetchone()
        cursor.close()
        return students

    def updateStudents(self, names, lastnames, phone, email, semester, id):
        cursor = mysql.get_db().cursor()
        cursor.execute("UPDATE students SET names = %s, lastnames = %s, phone = %s, email = %s, semester = %s WHERE id = %s", (names, lastnames, phone, email, semester, id,))
        mysql.get_db().commit()
        cursor.close()

class CourseModel():
    def createCourse(self, names, semester):
        cursor = mysql.get_db().cursor()
        cursor.execute('INSERT INTO courses (name,semester) VALUES (%s,%s)',
                       (names, semester,))
        mysql.get_db().commit()
        cursor.close()
    
    def listCourses(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM courses")
        courses = cursor.fetchall()
        cursor.close()
        return courses
    
    def deleteCourse(self, id):
        cursor = mysql.get_db().cursor()
        cursor.execute("DELETE FROM courses WHERE id = %s", (id,))
        mysql.get_db().commit()
        cursor.close()

class SessionModel():
    def createSession(self, course, date, starttime, endtime):
        cursor = mysql.get_db().cursor()
        cursor.execute('INSERT INTO session (course,date,start_time,end_time) VALUES (%s,%s,%s,%s)',
                       (course, date, starttime, endtime,))
        mysql.get_db().commit()
        cursor.close()
    
    def listSessions(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM session")
        sessions = cursor.fetchall()
        cursor.close()
        return sessions
    
    def deleteSession(self, id):
        cursor = mysql.get_db().cursor()
        cursor.execute("DELETE FROM session WHERE id = %s", (id,))
        mysql.get_db().commit()
        cursor.close()