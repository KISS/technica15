from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/schools')
def schools():
	return render_template("schools.html")

@app.route('/school-results')
def school_results():
	return render_template("school-results.html")

@app.route('/scholarships')
def scholarships():
	return render_template("scholarships.html")

@app.route('/loans')
def loans():
	return render_template("loans.html")

@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/profile')
def profile():
	return render_template("profile.html")

@app.route('/profile/account-settings')
def account_settings():
	return render_template("account-settings.html")

@app.route('/profile/about')
def about():
	return render_template("about.html")

@app.route('/profile/fafsa')
def fafsa():
	return render_template("fafsa.html")

@app.route('/profile/friendfund')
def friendfund():
	return render_template("friendfund.html")



if __name__ == '__main__':
	app.run(debug=True)