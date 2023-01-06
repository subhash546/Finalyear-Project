print("Welcome")
print("Subhash")

import sqlite3
from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta


 
app = Flask(__name__)
app.secret_key = "hello"
 
 
@app.route("/")
def index():
    return render_template("index.html")


@app.route('/abs')  
def abs():  
    return render_template("abstract.html");  

@app.route('/team')  
def team():  
    return render_template("team.html"); 

@app.route('/info')  
def guide():    
    return render_template("guide.html");
@app.route('/dash')  
def dash():  
    return render_template("dashboard.html");  

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
            email = request.form["email"]  
            password = request.form["password"]
            cPassword = request.form["cPassword"]   
            with sqlite3.connect("subhash.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into pro ( email, password,cPassword) values (?,?,?)",(email,password,cPassword))  
                con.commit()  
                msg = "User successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
if __name__=='__main__':
    app.run(debug=True)