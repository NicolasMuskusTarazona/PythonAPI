from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable = False) # nullable = Flase (No puedo estar vacio)
    author = db.Column(db.String(80), nullable = False)
    genre = db.Column(db.String(80), nullable = False)
    price = db.Column(db.Float, nullable = False)

    def to_dict(self):
        return{
            "id": self.id,
            "name": self.name,
            "author":self.author ,
            "genre": self.genre,
            "price": self.price ,
        }

with app.app_context():
    db.create_all()


# Routes
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Movie API"})

# GET ALL movies
@app.route("/movies",methods=["GET"])
def get_movies():
    movies = Movie.query.all()
    return jsonify([movie.to_dict() for movie in movies])

# GET BY ID movies
@app.route("/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    movie = movie.query.get(movie_id)
    if movie:
        return jsonify(movie.to_dict())
    else:
        return jsonify({"error":"Movie not found!"}), 404

# POST
@app.route("/movies", methods=["POST"])
def add_movies():
    data = request.get_json()

    new_movie = Movie(name=data["name"],
                        author=data["author"],
                        genre=data["genre"],
                        price=data['price'])
    db.session.add(new_movie)
    db.session.commit()
    return jsonify(new_movie.to_dict()), 201


# PUT 
@app.route("/movies/<int:movie_id>", methods=["PUT"])
def update_movies(movie_id):
    data = request.get_json()
    
    movie = Movie.query.get(movie_id)
    if movie:
        movie.name = data.get("name", movie.name)
        movie.author = data.get("author", movie.author)
        movie.genre = data.get("genre", movie.genre)
        movie.price = data.get("price", movie.price)

        db.session.commit()

        return jsonify(movie.to_dict())
    else:
        return jsonify({"error":"Movie not found!"}), 404

# DELETE
@app.route("/movies/<int:movie_id>", methods=["DELETE"])
def delete_movies(movie_id):
    movie = Movie.query.get(movie_id)
    if movie:
        db.session.delete(movie)
        db.session.commit()

        return jsonify({"message":"Movie was deleted!"})
    else:
        return jsonify({"error":"Movie not found!"}), 404


if __name__ == "__main__":
    app.run(debug=True)