from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.authors.models import Author
from application.works.models import Work
from application.authors.forms import AuthorForm, AuthorAddWork, AuthorEditName

# Listing Authors
@app.route("/authors", methods=["GET"])
def authors_index():
    return render_template("authors/list.html", authors = Author.query.all())

# Deleting an Author
@app.route("/authors/delete/<author_id>/", methods=["POST"])
@login_required(role="ADMIN")
def author_delete(author_id):
    a = Author.query.get(author_id)
    db.session.delete(a)
    db.session().commit()

    return redirect(url_for("authors_index"))

# Showing the Works related to an Author
@app.route("/authors/<author_id>/", methods=["GET"])
def author_view(author_id):
    return render_template("authors/author.html", author = Author.query.get(author_id), works = Author.works_of_author(author_id))

# Adding a new Author
@app.route("/authors/new/", methods=["GET"])
@login_required()
def authors_form():
    return render_template("authors/new.html", form = AuthorForm())

@app.route("/authors/new/", methods=["POST"])
@login_required()
def authors_create():
    form = AuthorForm(request.form)

    if not form.validate():
        return render_template("authors/new.html", form = form)

    a = Author(form.name.data)

    db.session().add(a)
    db.session().commit()
    
    return redirect(url_for("authors_index"))

# Deleting a relation between a Work and an Author
@app.route("/authors/deletework/<author_id>/<work_id>/", methods=["POST"])
@login_required(role="ADMIN")
def author_work_delete(author_id, work_id):
    a = Author.query.get(author_id)
    w = Work.query.get(work_id)
    w.authors.remove(a)
    db.session().commit()

    return redirect(url_for("author_view", author_id=author_id))

# Editing name of an Author
@app.route("/authors/editname/<author_id>/", methods=["GET"])
@login_required(role="ADMIN")
def author_editnameform(author_id):  
    return render_template("authors/editname.html", form = AuthorEditName(), author_id=author_id)

@app.route("/authors/editname/<author_id>/", methods=["POST"])
@login_required(role="ADMIN")
def author_editname(author_id):
    form = AuthorEditName(request.form)
    
    if not form.validate():
        return render_template("authors/editname.html", form = form, author_id=author_id)

    a = Author.query.get(author_id)

    a.name = form.name.data

    db.session().commit()

    return redirect(url_for("author_view", author_id=author_id))

# Adding a relation to a Work to an Author
@app.route("/authors/addwork/<author_id>/", methods=["GET"])
@login_required()
def author_addworkform(author_id):
    form = AuthorAddWork()

    form.work.choices = [(work.id, work.name) for work in Work.query.filter(Work.id != 1)]

    return render_template("authors/addwork.html", form = form, author_id=author_id)

@app.route("/authors/addwork/<author_id>/", methods=["POST"])
@login_required()
def author_addwork(author_id):
    form = AuthorAddWork(request.form)
    
    form.work.choices = [(work.id, work.name) for work in Work.query.filter(Work.id != 1)]

    if not form.validate_on_submit():
        return render_template("authors/addwork.html", form = form, author_id=author_id)

    a = Author.query.get(author_id)
    w = Work.query.get(form.work.data)
    w.authors.append(a)

    db.session().commit()

    return redirect(url_for("author_view", author_id=author_id))
