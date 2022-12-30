print("Welcome")
print("Subhash")

import sqlite3
from flask import Flask,render_template,url_for,request

 
app = Flask(__name__)
 
 
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login2')  
def login():  
    return render_template("login2.html");  

@app.route('/reg')  
def reg():  
    return render_template("register.html");  


    


import sqlite3  
  
con = sqlite3.connect("my.db")  
print("Database opened successfully")  
  

  
  
  

@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:   
            email = request.form["email"]  
            password = request.form["password"] 
            cpassword = request.form["cpassword"] 
            with sqlite3.connect("my.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into subhash ( email,password,cpassword) values (?,?,?)",(email,password,cpassword))  
                con.commit()  
                msg = "Employee successfully Added"
               
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally: 
            print(msg); 
            return render_template("success.html",msg = msg)  
            con.close()  
if __name__=='__main__':
    app.run(debug=True)