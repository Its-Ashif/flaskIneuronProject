##first flask app

from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello World</h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to Flask Tutorial"

@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method =='GET':
        return render_template('calculate.html')
    else:
        maths = float(request.form['math'])
        science = float(request.form['science'])
        computer = float(request.form['computer'])
        avg_marks = (maths+science+computer)/3

        return render_template('result.html',result=avg_marks)
    
@app.route('/car_details',methods=['GET','POST'])
def car_details():
    if request.method=='GET':
        return render_template('car_details.html')
    else:
        car_d={
            'company' : request.form['company'],
            'model' : request.form['model'],
            'year' : request.form['year']
        }
        return render_template('car_details_show.html',carDetails = car_d)


if __name__ == '__main__':
    app.run(debug=True)