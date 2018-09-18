from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jqheryvv4cuxtsbd'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flaskblogapp' #My SQL URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)


	def __repr__(self):
		return "User({}, {}, {})".format(self.username, self.email, self.image_file)
		# return "User('{self.username}', '{self.email}', '{self.image_file}')".format(**locals())


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return "User({}, {})".format(self.title, self.date_posted)
		# return "Post('{self.title}', '{self.date_posted}')".format(**locals())

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
	form = RegistrationForm()
	if form.validate_on_submit():
		flash('Account created successfully!', 'success')
		return redirect(url_for('home'))

	return render_template('register.html', title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username/email and password', 'danger')
	return render_template('login.html', title="Login", form=form)


if __name__ == '__main__':
	app.run(debug=True)