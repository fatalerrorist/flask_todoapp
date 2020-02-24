from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
#DATABASE LOCATION
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Ugur Akdogan/Desktop/coding/python/web/todoapp/todo.db'

db = SQLAlchemy(app)

#TABLE
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete= db.Column(db.Boolean)

#ROUTE-REDIRECT
@app.route("/")
def index():
    to_dos= Todo.query.all()
    return render_template("index.html",to_dos=to_dos)

@app.route("/add",methods=["POST"])
def addToDo():   
   title=request.form.get("title")
   newTodo= Todo(title=title,complete=False)
   db.session.add(newTodo)
   db.session.commit()
   return redirect(url_for("index"))

@app.route("/complete/<string:id>")
def completeTodo(id):
    todo= Todo.query.filter_by(id=id).first()
    todo.complete = not todo.complete
    
    db.session.commit()
    return redirect(url_for("index"))
    
@app.route("/delete/<string:id>")
def delete(id):
    todo= Todo.query.filter_by(id=id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


if __name__== "__main__":

    db.create_all()
    app.run(debug=True)

