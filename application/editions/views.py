from application import app, db
from flask import redirect, render_template, request, url_for
from application.editions.models import Edition
from application.editions.forms import EditionForm
from flask_login import login_required, current_user

@app.route("/editions", methods=["GET"])
@login_required
def editions_index():
    return render_template("editions/list.html", editions = Edition.query.filter_by(account_id = current_user.id))

@app.route("/editions/new/", methods=["GET"])
@login_required
def editions_form():
    return render_template("editions/new.html", form = EditionForm())

@app.route("/editions/new/", methods=["POST"])
@login_required
def editions_create():
    form = EditionForm(request.form)

    if not form.validate():
        return render_template("editions/new.html", form = form)

    e = Edition(form.name.data, form.printed.data, form.publisher.data, 
                    form.language.data, form.read.data)

    e.account_id = current_user.id

    db.session().add(e)
    db.session().commit()
    
    return redirect(url_for("editions_index"))