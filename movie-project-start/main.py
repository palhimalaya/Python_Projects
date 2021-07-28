from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

MOVIE_API_URL = 'https://api.themoviedb.org/3/search/movie'
MOVIE_API_KEY = 'ff4cedfe04435d7f9c4b737bdfd2d781'
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie_sql.db'
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


# db.create_all()


class EditForm(FlaskForm):
    rating = FloatField(label='Your Ratting out of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField("Done")


class AddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movie_data=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_API_URL, params={"api_key": MOVIE_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", movie_data=data)

    return render_template("add.html", form=form)


@app.route('/select', methods=['GET', 'POST'])
def select():
    movie_id = request.args.get('id')
    if movie_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_id}"
        # The language parameter is optional, if you were making the website for a different audience
        # e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(movie_api_url,
                                params={"api_key": MOVIE_API_KEY, 'language': 'en-US'})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    edit_form = EditForm()
    movie_id = request.args.get("id")
    movie_to_update = Movie.query.get(movie_id)
    if edit_form.validate_on_submit():
        # UPDATE RECORD
        movie_to_update.rating = request.form["rating"]
        movie_to_update.review = request.form["review"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=edit_form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
