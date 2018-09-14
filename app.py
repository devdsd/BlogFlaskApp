from flask import Flask, render_template, url_for

app = Flask(__name__)

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


if __name__ == '__main__':
	app.run(debug=True)