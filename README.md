# Flask Article App

A simple web application built with Flask that allows users to create authors and publish articles linked to them. Live demo is deployed on Render. Create an account, add authors, and publish articles to see how it works!

🔗 **Live Demo:** [flask-article-app.onrender.com](https://flask-article-app.onrender.com)

---

## Features

- View all published articles on the home page
- Add new authors with a name and email
- Add new articles and link them to an existing author
- Click on any author's name to view all articles written by them

---

## Tech Stack

- **Backend:** Python, Flask
- **Database:** SQLite via Flask-SQLAlchemy
- **Frontend:** HTML, Jinja2 templates, Bootstrap 5
- **Deployment:** Render (using Gunicorn)

---

## Project Structure

```
flask-article-app/
│
├── main.py               # Main Flask application (routes, models)
├── requirements.txt      # Python dependencies
├── Procfile              # Render/Gunicorn entry point
├── testdb.sqlite3        # SQLite database
│
└── templates/
    ├── index.html        # Home page - lists all articles
    ├── article_by.html   # Articles filtered by author
    ├── create.html       # Form to add a new article
    └── create_author.html# Form to add a new author
```

---

## Database Models

**Author** — stores author name and email  
**Article** — stores article title and content  
**ArticleAuthor** — join table linking articles to authors (many-to-many relationship)

---

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/flask-article-app.git
   cd flask-article-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python main.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000`

---

## Deployment

This app is deployed on **Render** using Gunicorn. The `Procfile` tells Render how to start the server:

```
web: gunicorn main:app
```

---

## Dependencies

| Package | Version |
|---|---|
| Flask | 3.1.3 |
| Flask-SQLAlchemy | 3.1.1 |
| SQLAlchemy | 2.0.48 |
| Gunicorn | 25.1.0 |
| Jinja2 | 3.1.6 |
| Werkzeug | 3.1.6 |

---

## Author

Rounak Prasad. Feedback and contributions are welcome!