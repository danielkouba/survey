from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def survey():
	return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
	print "GOT POST INFO"
	session["name"] = request.form['name']
	session["location"] = request.form['location']
	session["language"] = request.form['language']
	session["comment"] = request.form['comment']




	return redirect('/result')

@app.route('/result')
def result():
	return render_template("submitted.html", name=session["name"], location = session["location"], language=session["language"], comment=session["comment"] )

app.run(debug=True)