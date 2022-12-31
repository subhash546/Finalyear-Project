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


    
  
conn = sqlite3.connect("subhash.db")  
print("Database opened successfully")  
  
# conn.execute('CREATE TABLE users (name TEXT, email TEXT, password TEXT)')
# print ("Table created successfully")
# conn.close()
  
  
  
@app.route("/savedetails",methods = ["POST","GET"])  
def savedetails():  
    msg = "demo"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]  
            password = request.form["password"]  
            with sqlite3.connect("subhash.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into pro (name, email, password) values (?,?,?)",(name,email,password))  
                con.commit()  
                msg = "User successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
if __name__=='__main__':
    app.run(debug=True)