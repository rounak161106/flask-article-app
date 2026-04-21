from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, login_user, current_user, logout_user, UserMixin, login_required

path = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(path, "testdb.sqlite3")
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)

class Author(db.Model):
    __tablename__ = "authors"
    author_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)

class Article(db.Model):
    __tablename__ = "articles"
    article_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    authors = db.relationship("Author", secondary="article_authors")

class ArticleAuthor(db.Model):
    __tablename__ = "article_authors"
    author_id = db.Column(db.Integer, db.ForeignKey("authors.author_id"), primary_key=True, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey("articles.article_id"), primary_key=True, nullable=False)

@app.route("/", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username = username).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect('/articles')
            else:
                return "Invalid password"
        else:
            return "Username not found!!!"
        
    return render_template("login.html")

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User(username = username, password = password)
        db.session.add(user)
        db.session.commit()
        return render_template("login.html")
         
    return render_template("signup.html")

@login_required
@app.route('/articles')
def main():
    articles = Article.query.all() #or db.session.query(Article).all()
    return render_template("index.html", articles= articles)

@login_required
@app.route("/article_by/<user_name>")
def article_by(user_name):
    articles = Article.query.filter(Article.authors.any(name = user_name))
    return render_template("article_by.html", articles = articles, author = user_name)

@login_required
@app.route("/create", methods=["GET"])
def create():
    return render_template("create.html")

@login_required
@app.route("/create_author", methods=["GET"])
def create_author():
    return render_template("create_author.html")

@login_required
@app.route("/add", methods=["POST"])
def add():
    author_name = request.form.get("author").strip()
    title = request.form.get("title")
    content = request.form.get("content")
    # 1. Get author from DB
    author = Author.query.filter_by(name = author_name).first()
    if not author:
        return "Author not found"

    # 2. Create new article
    new_article = Article(title=title, content=content)

    # 3. Link author (this auto handles article_authors table)
    new_article.authors.append(author)

    # 4. Save to DB
    db.session.add(new_article)
    db.session.commit()

    return redirect("/")

@login_required
@app.route("/add_author", methods=["POST"])
def add_author():
    name = request.form.get("name")
    email = request.form.get("email")
    new_author = Author(name=name, email=email)
    db.session.add(new_author)
    db.session.commit()
    return redirect("/")

@login_required
@app.route('/search')
def search():
    query = request.args.get('q', '')
    articles = Article.query.filter(Article.content.like(f'%{query}%')).all()
    return render_template('search_results.html', articles=articles, query=query)

@login_required
@app.route('/feedback', methods = ["GET", "POST"])
def feedback():
    if request.method == "POST":
        feedback = request.form.get("feedback")
        return render_template("thank.html")
    
    return render_template("feedback.html")


@login_required
@app.route('/article/rating/<int:id>')
def rating(id):
    article_id = Article.query.get(id)
    print(f"Article with id {article_id} was clicked")
    return "OKK", 200

if __name__ == "__main__":
    app.run(debug=True)