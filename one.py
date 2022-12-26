print("Welcome")
print("Subhash")
from flask import Flask,render_template,request
 
app = Flask(__name__)
 
 
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login')  
def login():  
    return render_template("login.html");  

@app.route('/reg')  
def reg():  
    return render_template("register.html");  


@app.route('/', methods=['POST'])
def result():
    email=request.form['tf1']
    password=request.form['tf2']
   
    return render_template('pass.html',n=email,c=password)
 
 
if __name__ == "__main__":
    app.run()