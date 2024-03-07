from market import app
from flask import render_template, redirect, url_for, flash
from market.model import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    # If the user has clicked on the Submit Button, and check for certain conditions and if all the conditions are satisfied the method returns true
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:  # If there are no errors from the validation
        for err_msg in form.errors.values():
            # The flash message generates the message in the session which is the captured by the template using get_flashed_messages()
            # flash(f"There was an error with creating a user: {err_msg}", category='danger')
            flash(f"{err_msg[0]}", category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = LoginForm()
    if login.validate_on_submit():
        attempted_user = User.query.filter_by(username=login.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=login.password.data
        ):
            login_user(attempted_user)
            flash(f"Login Successful. You are logged in as: {attempted_user.username}", category='success')
            return redirect(url_for('market_page'))
    else:
        flash(f"Username and Password did not match.Please try again", category='danger')

    return render_template('login.html', login=login)
