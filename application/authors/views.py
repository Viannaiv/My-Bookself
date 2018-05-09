from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.authors.models import Author
from application.works.models import Work

@app.route("/authors", methods=["GET"])
def authors_index():
    return render_template("authors/list.html", authors = Author.query.all())

@app.route("/authors/delete/<author_id>/", methods=["POST"])
@login_required(role="ADMIN")
def author_delete(author_id):
    a = Author.query.get(author_id)
    db.session.delete(a)
    db.session().commit()

    return redirect(url_for("authors_index"))

@app.route("/authors/<author_id>/", methods=["GET"])
def author_view(author_id):
    return render_template("authors/author.html", author = Author.query.get(author_id), works = Author.works_of_author(author_id))

@app.route("/authors/deletework/<author_id>/<work_id>/", methods=["POST"])
@login_required(role="ADMIN")
def author_work_delete(author_id, work_id):
    a = Author.query.get(author_id)
    w = Work.query.get(work_id)
    w.authors.remove(a)
    db.session().commit()

    return redirect(url_for("author_view", author_id=author_id))