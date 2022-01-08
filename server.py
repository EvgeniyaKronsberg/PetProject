from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from forms import LoginForm
from models import User

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

# @app.route('/process-login', methods=['POST'])
# def process_login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter(User.username == form.username.data).first()
#         if user and user.check_password(form.password.data):
#             login_user(user)
#             flash('Вы успешно вошли на сайт')
#             return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)