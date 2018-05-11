from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.formats.models import Format
from application.formats.forms import FormatForm

# Listing Formats
@app.route("/formats", methods=["GET"])
@login_required(role="ADMIN")
def formats_index():
    return render_template("formats/list.html", formats = Format.query.all())

# Adding a Format
@app.route("/formats/new/", methods=["GET"])
@login_required(role="ADMIN")
def formats_form():
    return render_template("formats/new.html", form = FormatForm())

@app.route("/formats/new/", methods=["POST"])
@login_required(role="ADMIN")
def formats_create():
    form = FormatForm(request.form)

    if not form.validate():
        return render_template("formats/new.html", form = form)

    f = Format(form.name.data)

    db.session().add(f)
    db.session().commit()
    
    return redirect(url_for("formats_index"))