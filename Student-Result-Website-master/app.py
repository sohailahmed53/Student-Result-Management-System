from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:%40Muzammil78%40@localhost/results'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usn = db.Column(db.String(15), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    college_name = db.Column(db.String(255), nullable=False)
    branch = db.Column(db.String(255)) 
    stream = db.Column(db.String(255))
    # Add columns for subject scores
    subject1 = db.Column(db.Float, nullable=True)
    subject2 = db.Column(db.Float, nullable=True)
    subject3 = db.Column(db.Float, nullable=True)
    subject4 = db.Column(db.Float, nullable=True)
    subject5 = db.Column(db.Float, nullable=True)
    subject6 = db.Column(db.Float, nullable=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_result', methods=['POST'])
def search_result():
    usn = request.form['usn']
    student = Student.query.filter_by(usn=usn).first()

    if student:
        return render_template('result.html', student=student)
    else:
        not_found_message = "Student with USN {} not found.".format(usn)
        return render_template('not_found.html', message=not_found_message)

if __name__ == '__main__':
    app.run(debug=True)
