from flask import Flask,render_template
from werkzeug.datastructures import RequestCacheControl
app = Flask(__name__)

studentlist = [
    ["/static/dev.jpg","Devops Course", "Students"],
    ["/static/ml.jpg","Machine Learning Course", "Students"],
    ["/static/ai.jpg","Artificial Intelligence Course", "Students"],
    ["/static/robo.jpg","Robotics Course", "Students"],
     
]

courselist = [
    ["/static/python.jpg","Course1", "Python"],
    ["/static/django.jpg","course2", "Django"],
    ["/static/flask.jpg","course3", "Flask"],
    ["/static/dev.jpg","course4", "Devops"],
    ["/static/ml.jpg","course5", "Machine Learning"],
    ["/static/robo.jpg","course6", "Robotics"],
]

facultylist = [
    ["/static/fac1.jpg","Faculty: ", "Python"],
    ["/static/fac2.jpg","Faculty: ", "Django"],
    ["/static/fac3.jpg","Faculty: ", "Flask"],
    ["/static/fac4.jpg","Faculty: ", "Basics of python"],
    ["/static/fac5.jpg","Faculty: ", "Frameworks"],
    ["/static/fac6.jpg","Faculty: ", "Automation Testing"],
    
]

"""indexlist = [
    ["/static/elearn.jpg","Explore ", "Knowledge"],
    
]"""


@app.route('/')
def index():
    return render_template('index.html',len = len(studentlist), studentlist = studentlist)

@app.route('/student')
def student():
    return render_template('Students.html', len = len(studentlist), studentlist = studentlist)

@app.route('/institute')
def institute():
    return render_template('Institutions.html')

@app.route('/courses')
def courses():
    return render_template('courses.html',len = len(courselist), courselist = courselist)

@app.route('/faculty')
def faculty():
    return render_template('faculty.html',len = len(facultylist), facultylist = facultylist)





"""@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/twitter')
def twitter():
    return render_template('twitter.html')

@app.route('/facebook')
def facebook():
    return render_template('facebook.html')

@app.route('/instagram')
def instagram():
    return render_template('instagram.html')

@app.route('/career')
def career():
    return render_template('career.html')

@app.route('/testimony')
def testimony():
    return render_template('testimony.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if RequestCacheControl.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user)) """
    

if __name__ == '__main__':
   app.run(debug = True)