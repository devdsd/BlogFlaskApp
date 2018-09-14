from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jqheryvv4cuxtsbd'

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