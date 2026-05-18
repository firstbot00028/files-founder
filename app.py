from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    files = os.listdir()

    found_file = ""

    if request.method == "POST":

        try:
            user_input = int(request.form["number"])

            if len(files) > 0:
                found_file = files[user_input]
            else:
                found_file = "No files found 🥺"

        except:
            found_file = "Invalid Number ❌"

    return render_template("index.html", result=found_file)

app.run(debug=True)
