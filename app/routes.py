from app import app, db, bcrypt
from flask import render_template, url_for, flash, redirect, request
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
	{
		'author': 'Diether Dayondon',
		'title': 'Blog Post 1',
		'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Est, qui nisi suscipit! Nesciunt, accusantium explicabo id totam quas rem pariatur quis temporibus porro ad tenetur qui, officiis libero. Alias, quis.t',
		'date_posted': 'September 14, 2018'
	},

	{
		'author': 'User 2',
		'title': 'Blog Post 2',
		'content': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sunt, omnis? Harum illum assumenda magnam quam, molestias eaque, nostrum odio provident iusto ea! Mollitia, atque, expedita corporis labore enim optio hic.',
		'date_posted': 'September 20, 2018'
	}
]

		
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', posts=posts)


@app.route('/about')
def about():
	return render_template('about.html', title="About")


@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username=form.username.data, email=form.email.data, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Account created successfully! You can now be able to log in!', 'success')
		return redirect(url_for('login'))

	return render_template('register.html', title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		# if form.email.data == 'admin@blog.com' and form.password.data == 'password':
		# 	flash('You have been logged in!', 'success')
		# 	return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username/email and password', 'danger')
	return render_template('login.html', title="Login", form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
	return render_template('account.html', title="Account")