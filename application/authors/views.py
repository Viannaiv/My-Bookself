from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from application.authors.models import Author

@app.route("/authors", methods=["GET"])
def authors_index():
    return render_template("authors/list.html", authors = Author.query.all())

@app.route("/authors/delete/<author_id>/", methods=["POST"])
@login_required(role="ADMIN")
def author_delete(author_id):
    a = Author.query.get(author_id)
    db.session.delete(a)
    db.session().commit()
    #If does not delete from secondary table use handing the object to like: delete(object)

    return redirect(url_for("authors_index"))

@app.route("/authors/<author_id>/", methods=["GET"])
@login_required()
def author_view(author_id):
    return render_template("authors/author.html", author = Author.query.get(author_id), works = Author.works_of_author(author_id))