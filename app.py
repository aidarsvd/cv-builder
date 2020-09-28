from flask import Flask, render_template, request



#import pdfkit
#pdfkit.from_url('http://127.0.0.1:5000/workhistory', 'cv.pdf')

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

work_title2 = ''
employer2 = ''
start_date2 = ''
end_date2 = ''


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



@app.route('/about', methods=['POST'])
def getval1():
    global uname
    global surname
    global email
    global tel
    global occupation
    global about
    occupation = request.form['occupation']
    about = request.form['about']
    return render_template('about.html',n = uname, s = surname, em = email, tel = tel, occ = occupation, about=about)

@app.route('/workhistory', methods=['POST'])
def getval2():
    global uname
    global surname
    global email
    global tel
    global occupation
    global about
    return render_template('cv.html',n = uname, s = surname, em = email, tel = tel, occ = occupation, about=about)





if __name__ == "__main__":
    app.run(debug=True)
