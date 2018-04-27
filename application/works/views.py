from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.works.models import Work
from application.works.forms import WorkForm, WorkEditName, WorkEditPublished, WorkEditDescription

@app.route("/works", methods=["GET"])
def works_index():
    return render_template("works/list.html", works = Work.query.all())

@app.route("/works/new/", methods=["GET"])
@login_required()
def works_form():
    return render_template("works/new.html", form = WorkForm())

#Add "Delete ....?" to avoid misclicks
# consider moving ths and editing attributes to the viewing of one Work. Decide later.
@app.route("/works/delete/<work_id>/", methods=["POST"])
@login_required()
def work_delete(work_id):

    Work.query.filter_by(id=work_id).delete()
    db.session().commit()
  
    return redirect(url_for("works_index"))

@app.route("/works/new/", methods=["POST"])
@login_required()
def works_create():
    form = WorkForm(request.form)

    if not form.validate():
        return render_template("works/new.html", form = form)

    w = Work(form.name.data, form.published.data, form.description.data)
    
    db.session().add(w)
    db.session().commit()
    
    return redirect(url_for("works_index"))

@app.route("/works/editname/<work_id>/", methods=["GET"])
@login_required()
def work_editnameform(work_id):  
    return render_template("works/editname.html", form = WorkEditName(), work_id=work_id)

@app.route("/works/editname/<work_id>/", methods=["POST"])
@login_required()
def work_editname(work_id):
    form = WorkEditName(request.form)

    if not form.validate():
        return render_template("works/editname.html", form = form, work_id=work_id)

    w = Work.query.get(work_id)
    w.name = form.name.data
    
    db.session().commit()
  
    return redirect(url_for("work_view", work_id=work_id))

@app.route("/works/editpublished/<work_id>/", methods=["GET"])
@login_required()
def work_editpublishedform(work_id):  
    return render_template("works/editpublished.html", form = WorkEditPublished(), work_id=work_id)

@app.route("/works/editpublished/<work_id>/", methods=["POST"])
@login_required()
def work_editpublished(work_id):
    form = WorkEditPublished(request.form)

    if not form.validate():
        return render_template("works/editpublished.html", form = form, work_id=work_id)

    w = Work.query.get(work_id)
    w.published = form.published.data
    
    db.session().commit()
  
    return redirect(url_for("work_view", work_id=work_id))

@app.route("/works/editdescription/<work_id>/", methods=["GET"])
@login_required()
def work_editdescriptionform(work_id):  
    return render_template("works/editdescription.html", form = WorkEditDescription(), work_id=work_id)

@app.route("/works/editdescription/<work_id>/", methods=["POST"])
@login_required()
def work_editdescription(work_id):
    form = WorkEditDescription(request.form)

    if not form.validate():
        return render_template("works/editdescription.html", form = form, work_id=work_id)

    w = Work.query.get(work_id)
    w.description = form.description.data
    
    db.session().commit()
  
    return redirect(url_for("work_view", work_id=work_id))

@app.route("/works/<work_id>/", methods=["GET"])
def work_view(work_id):
    return render_template("works/work.html", work = Work.query.get(work_id))