from website import app
from website import forms
from website import models

from flask import (
    render_template,
    url_for,
    redirect,
    request
    )
    
from flask_sqlalchemy import SQLAlchemy

@app.route("/index")
@app.route("/")
def landing():
    return render_template("pages/index.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    form = forms.RegForm()
    if form.validate_on_submit():
        print(f"Registered as {form.username.data}")
        return "Successful registration."
    return render_template("pages/register.html", form=form)