from flask import render_template, redirect, url_for, flash

from app import app
from app.api.spy_cloud import credentials_compromised
from app.forms import LoginForm, ResetForm
from app.helpers.exceptions import ApiError


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:

            if credentials_compromised(form.email.data, form.password.data):
                flash(f'Your password has been compromised. Please reset it!')
                return redirect(url_for('reset'))
            else:
                return redirect(url_for('success'))
        except ApiError as e:
            return redirect(url_for('spy_cloud_api_error'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/reset', methods=['GET', 'POST'])
def reset():
    form = ResetForm()
    if form.validate_on_submit():
        try:
            if credentials_compromised(form.email.data, form.new_password.data):
                flash(f'The password you entered is also compromised. Please try another.')
                return redirect(url_for('reset'))
            else:
                return redirect(url_for('success'))
        except ApiError as e:
            return redirect(url_for('spy_cloud_api_error'))

    return render_template('reset.html', title='Reset Password', form=form)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/spy_cloud_api_error')
def spy_cloud_api_error():
    return render_template('spy_cloud_api_error.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', title='404 Error'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', title='500 Error'), 500
