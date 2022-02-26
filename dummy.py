from flask import Flask, render_template, request, url_for,redirect
from flask_sqlalchemy import SQLAlchemy
app= Flask(__name__)
db=SQLAlchemy(app)
class Task(db.Model):
    id=db.Column(db.Integer, primary_key= True)
    


@app.route('/')
def task_list():
    tasks=Task.query.all()
    return render_template('base.html', tasks)     

@app.route('/add_task', methods=['POST'])
def add_task():
    content=request.form.get['content']
    new_task=Task('content', complete=False)
    db.session.add(new_task)
    db.session.committ()
    return redirect(url_for('task_list'))
  
  
@app.route('/delete/<id:new_task_id>') 
def delete():
    new_task=Task.query.filter_by(id=new_task.id)
     