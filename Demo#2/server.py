from flask import Flask, render_template, request
app = Flask(__name__)

n ="5"

@app.route("/")
def number():
	return render_template("index.html", number=n)

@app.route("/change_number", methods = ["POST"])
def change_number():
	n = request.form['ner']
	return render_template('index.html', number = n)

@app.route("/display", methods = ["POST"])
def display():
	f = request.form['FirstName']
	return render_template('display.html', FirstName = f)

if __name__ == "__main__":
	app.run()

