from flask import Flask, render_template, flash, redirect, url_for
#from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from webapp.forms import LoginForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        return 'Hello'
    

    @app.route('/login')
    def login():
        # if current_user.is_authenticated:
        #     return redirect(url_for('index'))
        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    return app