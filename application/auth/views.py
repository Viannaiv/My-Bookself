from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.editions.models import Edition #delete later?
from application.auth.forms import LoginForm, SigninForm, ChangeNameForm, ChangePasswordForm, ChangeUsernameForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    
    if not form.validate():
        return render_template("auth/loginform.html", form = form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "No such username or password")

    login_user(user)
    flash("You have been logged in.")
    return redirect(url_for("index"))

@app.route("/auth/logout")
@login_required()
def auth_logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("index"))  

@app.route("/auth/signin", methods = ["GET"])
def auth_signin_form():
    return render_template("auth/signinform.html", form = SigninForm())

@app.route("/auth/signin", methods = ["POST"])
def auth_signin():
    form = SigninForm(request.form)

    if not form.validate():
        return render_template("auth/signinform.html", form = form)

    #Checking if the username already exists
    user = User.query.filter_by(username=form.username.data).first()
    if user:
        return render_template("auth/signinform.html", form = form, error = "Username already in use!")

    user = User(form.name.data, form.username.data, form.password.data)
    if user.username == "Vianna":
        user.role_id = 1
    else:
        user.role_id = 2

    db.session().add(user)
    db.session().commit()

    login_user(user)
    flash("You have been registered and logged in.")
    return redirect(url_for("index"))

@app.route("/auth/userinfo/<user_id>/", methods=["GET"])
@login_required()
def user_view(user_id):
    user = User.query.get(user_id)
    
    if current_user.id != user.id:
        flash("You are not authorised to view this information")
        return redirect(url_for("index"))

    return render_template("auth/userinfo.html", user = user)

@app.route("/auth/editpassword/<user_id>/", methods = ["GET"])
@login_required()
def auth_editpassword_form(user_id):
    return render_template("auth/editpassword.html", form = ChangePasswordForm(), user_id=user_id)

@app.route("/auth/editpassword/<user_id>/", methods = ["POST"])
@login_required()
def auth_editpassword(user_id):
    form = ChangePasswordForm(request.form)

    user = User.query.get(user_id)

    if user.id != current_user.id:
        flash("You are not authorised to change this information.")
        return redirect(url_for("index"))

    if not form.validate():
        return render_template("auth/editpassword.html", form = form, user_id=user_id)

    user = User.query.get(user_id)
    user.password = form.password.data

    db.session().commit()

    flash("Your password has succesfully been changed.")
    return redirect(url_for("user_view", user_id=user_id))

@app.route("/auth/editusername/<user_id>/", methods = ["GET"])
@login_required()
def auth_editusername_form(user_id):
    return render_template("auth/editusername.html", form = ChangeUsernameForm(), user_id=user_id)

@app.route("/auth/editusername/<user_id>/", methods = ["POST"])
@login_required()
def auth_editusername(user_id):
    form = ChangeUsernameForm(request.form)

    user = User.query.get(user_id)

    if user.id != current_user.id:
        flash("You are not authorised to change this information.")
        return redirect(url_for("index"))

    if not form.validate():
        return render_template("auth/editusername.html", form = form, user_id=user_id)

    user = User.query.filter_by(username=form.username.data).first()
    if user:
        return render_template("auth/editusername.html", form = form, error = "Username already in use!", user_id=user_id)
    
    user = User.query.get(user_id)
    user.username = form.username.data

    db.session().commit()

    flash("Your username has succesfully been changed.")
    return redirect(url_for("user_view", user_id=user_id))

@app.route("/auth/editname/<user_id>/", methods = ["GET"])
@login_required()
def auth_editname_form(user_id):
    return render_template("auth/editname.html", form = ChangeNameForm(), user_id=user_id)

@app.route("/auth/editname/<user_id>/", methods = ["POST"])
@login_required()
def auth_editname(user_id):
    form = ChangeNameForm(request.form)

    user = User.query.get(user_id)

    if user.id != current_user.id:
        flash("You are not authorised to change this information.")
        return redirect(url_for("index"))

    if not form.validate():
        return render_template("auth/editname.html", form = form, user_id=user_id)
    
    user = User.query.get(user_id)
    user.name = form.name.data

    db.session().commit()

    flash("Your name has succesfully been changed.")
    return redirect(url_for("user_view", user_id=user_id))

@app.route("/auth/delete/<user_id>/", methods=["POST"])
@login_required()
def auth_delete(user_id):
    user = User.query.get(user_id)

    if user.id != current_user.id:
        flash("You are not authorised to delete this information.") 
        return redirect(url_for("index"))

    Edition.query.filter_by(account_id=user_id).delete()
    User.query.filter_by(id=user_id).delete()
    db.session().commit()

    #Do I have to log out the user?
    #Add a really delete? message so no misclicks are possible
    flash("Your account has succesfully been deleted.")
    return redirect(url_for("index"))