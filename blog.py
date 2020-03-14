from flask import Flask, render_template, url_for, flash, redirect
from forms import registrationform, Loginform

app = Flask(__name__)

app.config['SECRET_KEY'] = '7c31e3742ce51ea41dba0ef2d82c0a4f'

posts = [{
	'author':'Rohit Kumar',
	'title':'Blog post1',
	'content':'first content',
	'date':'feb 17,2020'

},
{

	'author':'Sunil Kumar',
	'title':'Blog post2',
	'content':'Second content',
	'date':'feb 18,2020'

}]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)


@app.route("/About")
def About():
	return render_template('about.html', title='About')


@app.route("/register", methods = ['GET', 'POST'])
def register():
	form = registrationform()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='register', form= form)


@app.route("/login", methods = ['GET', 'POST'])
def login():
	form = Loginform()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You Have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check your username and password','danger')
	return render_template('login.html', title='login', form= form)


if __name__ == ' __main__':
	app.run(debug = True) 
