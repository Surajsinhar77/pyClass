from flask import Flask , render_template, request, session 
from sqlalchemy import false , null , true
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/project1form'
db = SQLAlchemy(app)
app.secret_key = "wertyui45678sdfer"

class details(db.Model):
    emil = db.Column(db.String(50), nullable =False, primary_key = True)
    password = db.Column(db.String(50), nullable =False)
    address = db.Column(db.String(100), nullable =False)
    address2 = db.Column(db.String(100), nullable =True)
    state = db.Column(db.String(50), nullable =False)
    city = db.Column(db.String(50), nullable =False)
    pincode = db.Column(db.Integer, nullable = False)

@app.route("/" , methods=['POST','GET'])
def formPage():
    return render_template('index.html') 

@app.route("/formsubmit" , methods = ['POST','GET']) 
def formSubmission():
    if request.method == 'POST':
        email = request.form.get('email')
        pswd = request.form.get('password')
        address = request.form.get('address')
        addresss2 = request.form.get('address2')
        state = request.form.get('state')
        city = request.form.get('city')
        pincode = request.form.get('pincode')
        enrty = details(emil = email, password = pswd, address = address, address2 = addresss2, state = state , city = city, pincode = pincode)
        db.session.add(enrty)
        db.session.commit()
        return "FORM SUCCESFULL SUBMITTED"
    return "Submittion fail"

@app.route('/viewdetailpage' ,methods=['POST', 'GET'])
def viwedetail():
    dtl = details.query.all()
    return render_template('details.html' ,details = dtl)

app.run(debug=True)
