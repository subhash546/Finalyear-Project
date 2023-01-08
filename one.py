

from flask import Flask,render_template,request,redirect,session,url_for
import sqlite3
app = Flask(__name__)
app.secret_key = "500"
# --------------------------------indexpage---------------------------
@app.route('/')
def index():
    return render_template('index.html')


# --------------------------------registerpage---------------------------
@app.route('/reg',methods=['POST','GET'])
def register():
    if request.method == "POST":
# sqlite
        connection = sqlite3.connect("subhash.db")
        cursor = connection.cursor()

#Html form
        name=request.form['name']
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        confirmpassword=request.form['confirmpassword']
        data=[name,username,email,password,confirmpassword]
        #print(name,username,email,password,confirmpassword)

#login authentications

        query1="SELECT email FROM pro WHERE email='"+email+"'"
        cursor.execute(query1)
        results = cursor.fetchall()
        if len(results) != 0:
            return "user already exists"
        else:

#register data insert

            query="INSERT INTO pro(name,username,email,password,confirmpassword) VALUES (?,?,?,?,?)"
            cursor.execute(query,data)
            connection.commit()
            return redirect('/login2')
    return render_template('register.html')   




# --------------------------------loginpage---------------------------
@app.route('/login2',methods=['GET','POST'])
def login():
    if request.method == "POST":
# sqlite
        connection = sqlite3.connect("subhash.db")
        cursor = connection.cursor()

#Html form
        email = request.form['namelogin']
        password=request.form['passwordlogin']

       # print(username,password)
#query
        query = "SELECT email,password FROM pro where email='"+email+"' and password='"+password+"'"
        cursor.execute(query)

        results = cursor.fetchall()
#validation
        if len(results) == 0:
            return "userid and password is incorrect"
        else:
             session['user'] = email
             return redirect("/success")
    else:
        if "user" in session:
            return redirect("success")
        return render_template('login2.html')


# --------------------------------homepage---------------------------
@app.route('/success')
def home():
    if 'user' in session:
        user = session['user']
        return render_template('success.html')
    else:
      return redirect(url_for("login2"))


# --------------------------------logoutpage---------------------------
@app.route('/logout')
def logout():
    session.pop("user",None)
    return redirect(url_for("index"))
















@app.route('/abs')  
def abs():  
    session.pop("user",None)
    return redirect(url_for("index"))
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


 





    
  

# conn.execute('CREATE TABLE users (name TEXT, email TEXT, password TEXT)')
# print ("Table created successfully")
# conn.close()
  
  
  
 
if __name__=='__main__':
    app.run(debug=True)