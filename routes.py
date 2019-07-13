from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, User
from forms import UsersForm
from flask_heroku import Heroku

app = Flask(__name__)
# heroku = Heroku(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/lab3_db'
db.init_app(app)
app.secret_key = "e14a-key"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    form = UsersForm()

    if request.method == "GET":
        return render_template('add_user.html', form=form)
    else:
        if form.validate_on_submit():
            first_name = request.form['first_name']
            age = request.form['age']
            new_user = User(first_name=first_name, age=age)
            db.session.add(new_user)
            db.session.commit()
            flash('Congrats. New user added: ' + first_name)
            return redirect(url_for('index'))

        flash('Invalid input')
        return render_template('add_user.html')

@app.route('/all_users')
def all_users():
    all_users = User.query.all()
    return render_template('all_users.html', all_users=all_users)

@app.route('/user_details/<int:user_id>')
def user_details(user_id):
    user = User.query.get(user_id)
    print('USER ::: ', type(user_id))
    return render_template('user_details.html', user=user)

@app.route('/delete/<int:user_id>')
def delete(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    print('USER :::: ', user.first_name)
    flash(user.first_name + ' was deleted from All Users')
    return render_template('index.html')

@app.route('/update/<int:user_id>', methods=["GET", "POST"])
def update(user_id):
    user = User.query.get(user_id)
    if request.method == "GET":
        return render_template('user_details.html', user=user)
    else:
        # if form.validate_on_submit():
        user.first_name = request.form['first_name']
        user.age = request.form['age']
        db.session.commit()
        flash('Successfully updated!')
        return render_template('user_details.html', user=user)


if __name__ == "__main__":
  app.run(debug=True)
