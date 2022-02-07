from flask import Flask,render_template,request
from pymongo import MongoClient



app = Flask(__name__)

#Database
client = MongoClient('localhost',27017)
db= client.shivsurya



@app.route('/input')
def my_form():
    return render_template("input.html")

@app.route('/input', methods=['GET','POST'])
def my_form_post():
    print(request.form)
    name = request.form['name']
    age = request.form['age']
    gender = request.form["gender"]
    mobile= request.form["mobile"]
    processed_text = {"name":name,"age":age,"gender":gender,"mobile":mobile}
    db.information.insert_one(processed_text)
    return render_template("input.html")



@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/Data')
def All_Data():
    users = db.information.find({})
    return render_template("Data.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)