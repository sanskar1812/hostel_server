from flask import Flask,redirect, render_template, request

app=Flask(__name__) #turn my file into web application

students=[]

@app.route("/")   # listen to get request on '/'
def home():
    return render_template("index.html")

@app.route("/registrants")
def registrants():
    return render_template("registered.html",students=students)



@app.route("/register",methods=["POST"])
def register():
    name=request.form.get("name")
    dorm=request.form.get("dorm")

    if not name or not dorm:
        return "failure"
    students.append(f"{name} from {dorm}")
    return redirect("/registrants")
