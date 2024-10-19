from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'flask_final'
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///D:\Neat\Midterm/database.db'
db = SQLAlchemy(app)

import routes

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # This creates the database and tables if they don't exist
    app.run()
