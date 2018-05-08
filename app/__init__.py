from flask import Flask

from flask_admin import Admin

app = Flask(__name__)

admin = Admin(app, name='admin', template_mode='bootstrap3')
# Add administrative views here

if __name__ == "__main__":
    app.run()