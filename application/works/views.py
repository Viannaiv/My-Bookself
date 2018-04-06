from application import app, db
from flask import redirect, render_template, request, url_for
from application.works.models import Work
from application.works.forms import WorkForm
from flask_login import login_required

@app.route("/works", methods=["GET"])
def works_index():
    return render_template("works/list.html", works = Work.query.all())

@app.route("/works/new/", methods=["GET"])
@login_required
def works_form():
    return render_template("works/new.html", form = WorkForm())

#Add "Delete ....?" to avoid misclicks
# consider moving ths and editig attributes to the viewing of one Work. Decide later.
@app.route("/works/delete/<work_id>/", methods=["POST"])
@login_required
def work_delete(work_id):

    Work.query.filter_by(id=work_id).delete()
    db.session().commit()
  
    return redirect(url_for("works_index"))

@app.route("/works/new/", methods=["POST"])
@login_required
def works_create():
    form = WorkForm(request.form)

    if not form.validate():
        return render_template("works/new.html", form = form)

    w = Work(form.name.data, form.published.data, form.description.data)
    
    db.session().add(w)
    db.session().commit()
    
    return redirect(url_for("works_index"))

