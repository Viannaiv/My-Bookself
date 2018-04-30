from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.editions.models import Edition
from application.editions.forms import EditionForm, EditionEditName, EditionEditPrinted, EditionEditPublisher, EditionEditLanguage, EditionEditRead, EditionEditNotes
from flask_login import current_user, login_manager

@app.route("/editions", methods=["GET"])
@login_required()
def editions_index():
    return render_template("editions/list.html", editions = Edition.query.filter_by(account_id = current_user.id))

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
    e.format_id = 1 #this will be fixed later
    e.work_id = 1 #and this one as well

    db.session().add(e)
    db.session().commit()
    
    return redirect(url_for("editions_index"))

@app.route("/editions/<edition_id>/", methods=["GET"])
@login_required()
def edition_view(edition_id):
    return render_template("editions/edition.html", edition = Edition.query.get(edition_id))

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

@app.route("/editions/delete/<edition_id>/", methods=["POST"])
@login_required()
def edition_delete(edition_id):
    e = Edition.query.get(edition_id)

    if e.account_id != current_user.id: 
        return login_manager.unauthorized()

    Edition.query.filter_by(id=edition_id).delete()
    db.session().commit()
  
    return redirect(url_for("editions_index"))

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