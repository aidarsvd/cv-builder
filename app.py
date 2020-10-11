from flask import Flask, render_template, request



app = Flask(__name__)

uname = ''
surname = ''
email = ''
tel = ''

occupation = ''
about = ''

work_title = ''
employer = ''
start_date = ''
end_date = ''

work_title1 = ''
employer1 = ''
start_date1 = ''
end_date1 = ''



edu1 = ''
spec1 = ''
edu_start_date1 = ''
edu_end_date1 = ''

edu2 = ''
spec2 = ''
edu_start_date2 = ''
edu_end_date2 = ''


languages = ''
lans = []

skills = ''
s_skill = []

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def getval():
    global uname
    global surname
    global email
    global tel
    uname = request.form['uname']
    surname = request.form['surname']
    email = request.form['email']
    tel = request.form['tel']
    return render_template('names.html', n = uname, s = surname, em = email, tel = tel)



@app.route('/about', methods=['POST', 'GET'])
def getval1():
    global uname
    global surname
    global email
    global tel
    global occupation
    global about
    global work_title
    global employer
    global start_date
    global end_date

    occupation = request.form['occupation']
    about = request.form['about']
    return render_template('about.html',n = uname, s = surname, em = email, tel = tel, occ = occupation, about=about)



@app.route('/workhistory', methods=['POST', 'GET'])
def getval2():
    global uname
    global surname
    global email
    global tel
    global occupation
    global about
    global work_title
    global employer
    global start_date
    global end_date
    global work_title1
    global employer1
    global start_date1
    global end_date1

    work_title = request.form['work']
    employer = request.form['employer']
    start_date = request.form['work_start_date']

    if request.form.get('check') != None:
        end_date = request.form['work_end_date']
    else:
        end_date = 'Present'
        

        
    return render_template('workhistory.html',n = uname, s = surname, em = email, tel = tel, occ = occupation, about=about,
    work_t = work_title, emplo = employer, start = start_date, end = end_date)


@app.route('/addwork', methods=['POST', 'GET'])
def addwork():
    global uname
    global surname
    global email
    global tel
    global occupation
    global about
    global work_title
    global employer
    global start_date
    global end_date
    global work_title1
    global employer1
    global start_date1
    global end_date1

    work_title1 = request.form['work1']
    employer1 = request.form['employer1']
    start_date1 = request.form['work_start_date1']

    if request.form.get('check') != None:
        end_date1 = request.form['work_end_date1']
    else:
        end_date1 = 'Present'

    return render_template('addwork.html', n=uname, s=surname, em=email, tel=tel, occ=occupation, about=about,
                           work_t=work_title, emplo=employer, start=start_date, end=end_date,
                           work_t1=work_title1, emplo1=employer1, start1=start_date1, end1=end_date1)




@app.route('/education', methods = ['POST'])
def getval3():
    return render_template('education.html')


@app.route('/addeducation', methods = ['POST'])
def addeducation():
    global edu1
    global spec1
    global edu_start_date1
    global edu_end_date1

    edu1 = request.form['edu1']
    spec1 = request.form['spec1']
    edu_start_date1 = request.form['edu_start_date1']
    edu_end_date1 = request.form['edu_end_date1']
    return render_template('addeducation.html', edu1 = edu1, spec1 = spec1, edu_start_date1 = edu_end_date1)


@app.route('/skills', methods = ['POST'])
def done():

    global languages
    global lans
    global skills
    global s_skill
    global edu2
    global spec2
    global edu_start_date2
    global edu_end_date2
    return render_template('skills.html')

@app.route('/addskills', methods = ['POST'])
def check():
    global uname
    global surname
    global email
    global tel
    global occupation
    global about

    global work_title
    global employer
    global start_date
    global end_date

    global work_title1
    global employer1
    global start_date1
    global end_date1

    global work_title2
    global employer2
    global start_date2
    global end_date2

    global edu1
    global spec1
    global edu_start_date1
    global edu_end_date1
    global edu2
    global spec2
    global edu_start_date2
    global edu_end_date2
    languages = request.form['languages']


    skills = request.form['skills']

    return render_template('splash.html', n=uname, s=surname, em=email, tel=tel, occ=occupation, about=about,
                           work_t=work_title, emplo=employer, start=start_date, end=end_date,
                           work_t1=work_title1, emplo1=employer1, start1=start_date1, end1=end_date1,
                           edu1=edu1, spec1=spec1, edu_start_date1=edu_end_date1,
                           edu2=edu2, spec2=spec2, edu_start_date2=edu_end_date2,
                           )





if __name__ == "__main__":
    app.run(debug=True)
