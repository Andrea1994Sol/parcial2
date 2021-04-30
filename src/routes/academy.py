from src import app
from src.controllers.students import StudentsController, CourseController, SessionController
from flask import make_response, session, jsonify, request, render_template, redirect, flash, url_for

studentsController = StudentsController()
courseController = CourseController()
sessionController = SessionController()

# ---------- ROUTES HOME -----------------
@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

# ---------- ROUTES COURSES -----------------
@app.route('/course', methods=['POST', 'GET'])
def createCourse():

    names = request.form['names']
    semester = request.form['semester']

    courseController.createCourse(names, semester)

    return render_template('courses/create.html')

@app.route('/courses/list', methods=['POST', 'GET'])
def listCourses():
    courses = courseController.listCourses()
    return render_template('courses/list.html', courses=courses)


@app.route('/course/delete/<id>', methods=['POST', 'GET'])
def deleteCourse(id):
    courseController.deleteCourse(id)
    return redirect(url_for('listCourses'))

# ---------- ROUTES STUDENTS -----------------
@app.route('/createStudentPreview', methods=['POST', 'GET'])
def createStudentPreview():
    courses = courseController.listCourses()
    print(courses)
    return render_template('students/create.html', courses=courses)

@app.route('/student', methods=['POST', 'GET'])    
def createStudent():
    uid = request.form['uid']
    names = request.form['names']
    lastnames = request.form['lastnames']
    phone = request.form['phone']
    email = request.form['email']
    semester = request.form['semester']
    course = request.form['course']

    studentsController.createStudents(uid, names, lastnames, phone, email, semester, course)
    return redirect(url_for('createStudentPreview'))

@app.route('/student/list', methods=['POST', 'GET'])
def listStudent():
    students = studentsController.listStudents()
    return render_template('students/list.html', students=students)

@app.route('/delete/<id>', methods=['POST', 'GET'])
def deleteStudent(id):
    studentsController.deleteStudents(id)
    return redirect(url_for('listStudent'))


@app.route('/updatetemp/<id>', methods=['POST', 'GET'])
def updateStudentTemp(id):
    students = studentsController.listStudentsUnique(id)
    id = students[0]
    names = students[1]
    lastnames = students[2]
    phone = students[3]
    email = students[4]
    semester = students[5]
    print(id)
    print(names)
    print(lastnames)
    print(phone)
    print(email)
    print(semester)

    return render_template('students/update.html', id=id, names=names, lastnames=lastnames, phone=phone, email=email, semester=semester)


@app.route('/update', methods=['PUT', 'GET'])
def updateStudent():
    id = request.form['id']
    names = request.form['names']
    lastnames = request.form['lastnames']
    phone = request.form['phone']
    email = request.form['email']
    semester = request.form['semester']

    studentsController.updateStudents(
        names, lastnames, phone, email, semester, id)

    return render_template('students/create.html')

# ---------- ROUTES SESSIONS -----------------
@app.route('/session/create', methods=['POST', 'GET'])
def createSession():
    course = request.form['course']
    date = request.form['date']
    starttime = request.form['starttime']
    endtime = request.form['endtime']

    sessionController.createSession(course, date, starttime, endtime)

    return redirect(url_for('listSessionPreview'))

@app.route('/createSessionPreview', methods=['POST', 'GET'])
def createSessionPreview():
    courses = courseController.listCourses()
    return render_template('sessions/create.html', courses=courses)

@app.route('/sessions', methods=['POST', 'GET'])
def listSessionPreview():
    sessions = sessionController.listSessions()
    return render_template('sessions/list.html', sessions=sessions)

@app.route('/session/delete/<id>', methods=['POST', 'GET'])
def deleteSession(id):
    sessionController.deleteSession(id)
    return redirect(url_for('listSessionPreview'))
