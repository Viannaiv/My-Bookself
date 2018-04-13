from application import app, db
from flask import redirect, render_template, request, url_for
from application.editions.models import Edition
# form imports here later
from flask_login import login_required

@app.route("/editions", methods=["GET"])
def editions_index():
    return render_template("editions/list.html", editions = Edition.query.all())

