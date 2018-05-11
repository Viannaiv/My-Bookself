from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.editions.models import Edition
from application.editions.forms import EditionForm, EditionEditName, EditionEditPrinted, EditionEditPublisher
from application.editions.forms import EditionEditLanguage, EditionEditRead, EditionEditNotes, EditionSelectWork, EditionSelectFormat
from application.works.models import Work
from application.formats.models import Format
from flask_login import current_user, login_manager

# Listing Editions
@app.route("/editions", methods=["GET"])
@login_required()
def editions_index():
    return render_template("editions/list.html", editions = Edition.query.filter_by(account_id = current_user.id))

# Adding a new Edition
@app.route("/editions/new/", methods=["GET"])
@login_required()
def editions_form():
    return render_template("editions/new.html", form = EditionForm())

@app.route("/editions/new/", methods=["POST"])
@login_required()
def editions_create():
    form = EditionForm(request.form)

    if not form.validate():
        return render_template("editions/new.html", form = form)

    e = Edition(form.name.data, form.printed.data, form.publisher.data, 
                    form.language.data, form.read.data)

    e.account_id = current_user.id
    e.format_id = 1
    e.work_id = 1

    db.session().add(e)
    db.session().commit()
    
    return redirect(url_for("editions_index"))

# Showing information of an Edition
@app.route("/editions/<edition_id>/", methods=["GET"])
@login_required()
def edition_view(edition_id):
    e = Edition.query.get(edition_id)
    work_id = e.work_id
    format_id = e.format_id
    return render_template("editions/edition.html", edition = e, work = Work.query.get(work_id), 
        format = Format.query.get(format_id), authors = Work.authors_of_work(work_id))


# Editing name of an Edition
@app.route("/editions/editname/<edition_id>/", methods=["GET"])
@login_required()
def edition_editnameform(edition_id):  
    return render_template("editions/editname.html", form = EditionEditName(), edition_id=edition_id)

@app.route("/editions/editname/<edition_id>/", methods=["POST"])
@login_required()
def edition_editname(edition_id):
    form = EditionEditName(request.form)
    
    if not form.validate():
        return render_template("editions/editname.html", form = form, edition_id=edition_id)

    e = Edition.query.get(edition_id)

    if e.account_id != current_user.id: 
        return login_manager.unauthorized()

    e.name = form.name.data

    db.session().commit()

    return redirect(url_for("edition_view", edition_id=edition_id))


# Editing printed of an Edition
@app.route("/editions/editprinted/<edition_id>/", methods=["GET"])
@login_required()
def edition_editprintedform(edition_id):  
    return render_template("editions/editprinted.html", form = EditionEditPrinted(), edition_id=edition_id)

@app.route("/editions/editprinted/<edition_id>/", methods=["POST"])
@login_required()
def edition_editprinted(edition_id):
    form = EditionEditPrinted(request.form)

    if not form.validate():
        return render_template("editions/editprinted.html", form = form, edition_id=edition_id)

    e = Edition.query.get(edition_id)

    if e.account_id != current_user.id: 
        return login_manager.unauthorized()

    e.printed = form.printed.data

    db.session().commit()

    return redirect(url_for("edition_view", edition_id=edition_id))

# Editing publisher of an Edition
@app.route("/editions/editpublisher/<edition_id>/", methods=["GET"])
@login_required()
def edition_editpublisherform(edition_id):  
    return render_template("editions/editpublisher.html", form = EditionEditPublisher(), edition_id=edition_id)

@app.route("/editions/editpublisher/<edition_id>/", methods=["POST"])
@login_required()
def edition_editpublisher(edition_id):
    form = EditionEditPublisher(request.form)

    if not form.validate():
        return render_template("editions/editpublisher.html", form = form, edition_id=edition_id)

    e = Edition.query.get(edition_id)

    if e.account_id != current_user.id: 
        return login_manager.unauthorized()

    e.publisher = form.publisher.data

    db.session().commit()

    return redirect(url_for("edition_view", edition_id=edition_id))

# Editing language of an Edition
@app.route("/editions/editlanguage/<edition_id>/", methods=["GET"])
@login_required()
def edition_editlanguageform(edition_id):  
    return render_template("editions/editlanguage.html", form = EditionEditLanguage(), edition_id=edition_id)

@app.route("/editions/editlanguage/<edition_id>/", methods=["POST"])
@login_required()
def edition_editlanguage(edition_id):
    form = EditionEditLanguage(request.form)

    if not form.validate():
        return render_template("editions/editlanguage.html", form = form, edition_id=edition_id)

    e = Edition.query.get(edition_id)

    if e.account_id != current_user.id: 
        return login_manager.unauthorized()

    e.language = form.language.data

    db.session().commit()

    return redirect(url_for("edition_view", edition_id=edition_id))

# Editing read of an edition
@app.route("/editions/editread/<edition_id>/", methods=["GET"])
@login_required()
def edition_editreadform(edition_id):  
    return render_template("editions/editread.html", form = EditionEditRead(), edition_id=edition_id)

@app.route("/editions/editread/<edition_id>/", methods=["POST"])
@login_required()
def edition_editread(edition_id):
    form = EditionEditRead(request.form)

    if not form.validate():
        return render_template("editions/editread.html", form = form, edition_id=edition_id)

    e = Edition.query.get(edition_id)

    if e.account_id != current_user.id: 
        return login_manager.unauthorized()
        
    e.read = form.read.data

    db.session().commit()

    return redirect(url_for("edition_view", edition_id=edition_id))

# Deleting an Edition
@app.route("/editions/delete/<edition_id>/", methods=["POST"])
@login_required()
def edition_delete(edition_id):
    e = Edition.query.get(edition_id)

    if e.account_id != current_user.id: 
        return login_manager.unauthorized()

    Edition.query.filter_by(id=edition_id).delete()
    db.session().commit()
  
    return redirect(url_for("editions_index"))

# Editing notes of an Edition
@app.route("/editions/editnotes/<edition_id>/", methods=["GET"])
@login_required()
def edition_editnotesform(edition_id):  
    return render_template("editions/editnotes.html", form = EditionEditNotes(), edition_id=edition_id)

@app.route("/editions/editnotes/<edition_id>/", methods=["POST"])
@login_required()
def edition_editnotes(edition_id):
    form = EditionEditNotes(request.form)
    
    if not form.validate():
        return render_template("editions/editnotes.html", form = form, edition_id=edition_id)

    e = Edition.query.get(edition_id)

    if e.account_id != current_user.id: 
        return login_manager.unauthorized()

    e.notes = form.notes.data

    db.session().commit()

    return redirect(url_for("edition_view", edition_id=edition_id))

# Changing the Work linked to the Edition
@app.route("/editions/editwork/<edition_id>/", methods=["GET"])
@login_required()
def edition_editworkform(edition_id):
    form = EditionSelectWork()

    form.work.choices = [(work.id, work.name) for work in Work.query.all()]

    return render_template("editions/editwork.html", form = form, edition_id=edition_id)

@app.route("/editions/editwork/<edition_id>/", methods=["POST"])
@login_required()
def edition_editwork(edition_id):
    form = EditionSelectWork(request.form)
    
    form.work.choices = [(work.id, work.name) for work in Work.query.all()]

    if not form.validate_on_submit():
        return render_template("editions/editwork.html", form = form, edition_id=edition_id)

    e = Edition.query.get(edition_id)

    if e.account_id != current_user.id: 
        return login_manager.unauthorized()

    e.work_id = form.work.data

    db.session().commit()

    return redirect(url_for("edition_view", edition_id=edition_id))

# Changing the Format linked to an Edition
@app.route("/editions/editformat/<edition_id>/", methods=["GET"])
@login_required()
def edition_editformatform(edition_id):
    form = EditionSelectFormat()

    form.format.choices = [(format.id, format.name) for format in Format.query.all()]

    return render_template("editions/editformat.html", form = form, edition_id=edition_id)

@app.route("/editions/editformat/<edition_id>/", methods=["POST"])
@login_required()
def edition_editformat(edition_id):
    form = EditionSelectFormat(request.form)
    
    form.format.choices = [(format.id, format.name) for format in Format.query.all()]

    if not form.validate_on_submit():
        return render_template("editions/editformat.html", form = form, edition_id=edition_id)

    e = Edition.query.get(edition_id)

    if e.account_id != current_user.id: 
        return login_manager.unauthorized()

    e.format_id = form.format.data

    db.session().commit()

    return redirect(url_for("edition_view", edition_id=edition_id))