from flask import Flask, render_template, request
import requests
import smtplib

response = requests.get("https://api.npoint.io/263537392f9b90cc3d4b")
b_data = response.json()
blog_data = b_data[::-1]

my_email = "4testingcode@gmail.com"
password = "testingcode4@()"

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html", data=blog_data)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/posts/<string:index>")
def post_page(index):
    for post in blog_data:
        if post['title'] == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["POST", "GET"])
def get_contact():
    if request.method == "POST":
        data = request.form

        send_mail(data["username"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_mail(username, email, phone, message):
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="palhimalaya123@gmail.com",
                        msg=f"Subject:{username}\n\nName:{username}\n Email:{email}\nPhone:{phone}\nMessage:{message}")


if __name__ == "__main__":
    app.run(debug=True)
