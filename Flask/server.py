from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("Himal.html")
@app.route("/guess/<name>")
def guess(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = response.json()
    gender = gender_data["gender"]
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)



if __name__ == "__main__":
    app.run(debug=True)
