
from flask import Flask, render_template, request,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app=Flask(__name__)

#database config
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
db = SQLAlchemy(app)

class Todo(db.Model):
    #creating a table in db: Id, title and complete columns
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100))
    complete=db.Column(db.Boolean) 
    date=db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/')
def index():
    #show all todos
    todo_list=Todo.query.all() #from Todo class above query to see db
    return render_template('base.html', todo_list=todo_list) #displays all entry from todo_list


@app.route('/add', methods=['POST'])
def add():
    #to add new items.
    title=request.form.get('title')
    new_todo=Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/update/<int:todo_id>')
def update(todo_id):
    #to update an item.
    todo =Todo.query.filter_by(id=todo_id).first()  
    todo.complete= not todo.complete
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    #to delete an item.
    todo =Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/edit', methods=['POST'])
def edit():
    #to edit an item.
    newtitle=request.form.get('newtitle')
    oldtitle=request.form.get('oldtitle')
    todo=Todo.query.filter_by(title=oldtitle).first()
    todo.title=newtitle
    db.session.commit()
    return redirect('/')







if __name__ == '__main__':
    db.create_all()
    
    
    
    app.run(debug=True)