from flask import Flask, render_template, request
import requests
import smtplib 


NAME = "biniamzemenfes2@gmail.com"
PASSWORD  = "exixmenetnhbgkzc"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact", methods=["POST"])
def messages():
    name = request.form["username"]
    email = request.form["email"]
    phone_number = request.form["phonenumber"]
    message = request.form["message"]

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=NAME, password=PASSWORD)

        connection.sendmail(
            from_addr=NAME,
            to_addrs="amitkidanu67@gmail.com",
            msg=f"""Subject: New Contact Message

NAME: {name}
EMAIL: {email}
PHONE NUMBER: {phone_number}
MESSAGE: {message}
"""
        )

    return render_template("contact.html")

    
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
