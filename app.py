from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my super secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mindpal.db'
db = SQLAlchemy(app)


db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
